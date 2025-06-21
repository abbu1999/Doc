# importing pyspark libraries
# importing influxDB libraries
# importing the requests library
# importing the requests library
# importing the redis libraries
# importing influxDB libraries
# importing the redis libraries

import urllib
from influxdb import InfluxDBClient
import os
import sys
import requests
import statistics
import urllib3
import config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# importing hdfs libraries
# from pywebhdfs.webhdfs import PyWebHdfsClient
import datetime

dte = datetime.datetime.now() - datetime.timedelta(minutes=2)
req_time = dte.strftime("%Y-%m-%d %H:%M:00")
current_unixtime = dte.strftime("%s")
os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""

# The final json object which would have all the datapoints to write to influx in the end
influxJson = []
influxClient = InfluxDBClient(
    host=config.ANOMALY_INFLUX_HOST, port=config.ANOMALY_INFLUX_PORT
)


def rest_api_call(
    requestUrl,
    requestHeaders,
    requestParams=None,
    requestType="GET",
    requestBody=None,
    requestVerify=False,
):
    try:
        responseBody = ""
        if requestType == "GET":
            response = requests.get(
                url=requestUrl,
                headers=requestHeaders,
                params=requestParams,
                verify=requestVerify,
            )
        else:
            response = requests.post(
                url=requestUrl,
                data=requestBody,
                headers=requestHeaders,
                params=requestParams,
                verify=requestVerify,
            )
        response.raise_for_status()
        responseBody = response.json()

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        sys.exit(1)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        sys.exit(1)
    return responseBody


def calculate_response(INFLUX_APIPARAM_QUERY):
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    requestParams = {
        "db": config.INFLUX_APIPARAM_DB,
        "q": INFLUX_APIPARAM_QUERY,
        "epoch": config.INFLUX_APIPARAM_TIMEFORMAT,
    }
    responseBody = rest_api_call(
        config.INFLUX_API_ENDPOINT, headers, urllib.parse.urlencode(requestParams)
    )

    try:
        for metricData in responseBody["results"][0]["series"]:
            dataPointAvailable = "YES"
            value = metricData["values"][0][1]
            return round(value, 2), dataPointAvailable
    except KeyError:
        dataPointAvailable = "NO"
        value = 0.0
        return value, dataPointAvailable


def fetchCurrentDataPoint():
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    requestParams = {
        "db": config.INFLUX_APIPARAM_DB,
        "q": config.INFLUX_APIPARAM_CURRENTVALUE_QUERY,
        "epoch": config.INFLUX_APIPARAM_TIMEFORMAT,
    }
    # print(requestParams)
    responseBody = rest_api_call(
        config.INFLUX_API_ENDPOINT, headers, urllib.parse.urlencode(requestParams)
    )
    return responseBody


def fetchDay1DataPoint(impactedComponent, impactedDimension):
    query = config.INFLUX_APIPARAM_QUERY % (
        config.d1_start,
        config.d1_end,
        impactedComponent,
        impactedDimension,
    )
    metric_value = calculate_response(query)
    return metric_value


def fetchDay2DataPoint(impactedComponent, impactedDimension):
    query = config.INFLUX_APIPARAM_QUERY % (
        config.d2_start,
        config.d2_end,
        impactedComponent,
        impactedDimension,
    )
    metric_value = calculate_response(query)
    return metric_value


def fetchDay3DataPoint(impactedComponent, impactedDimension):
    query = config.INFLUX_APIPARAM_QUERY % (
        config.d3_start,
        config.d3_end,
        impactedComponent,
        impactedDimension,
    )
    metric_value = calculate_response(query)
    return metric_value


def fetchDay4DataPoint(impactedComponent, impactedDimension):
    query = config.INFLUX_APIPARAM_QUERY % (
        config.d4_start,
        config.d4_end,
        impactedComponent,
        impactedDimension,
    )
    metric_value = calculate_response(query)
    return metric_value


def fetchDay5DataPoint(impactedComponent, impactedDimension):
    query = config.INFLUX_APIPARAM_QUERY % (
        config.d5_start,
        config.d5_end,
        impactedComponent,
        impactedDimension,
    )
    metric_value = calculate_response(query)
    return metric_value


def fetchDay6DataPoint(impactedComponent, impactedDimension):
    query = config.INFLUX_APIPARAM_QUERY % (
        config.d6_start,
        config.d6_end,
        impactedComponent,
        impactedDimension,
    )
    metric_value = calculate_response(query)
    return metric_value


def fetchDay7DataPoint(impactedComponent, impactedDimension):
    query = config.INFLUX_APIPARAM_QUERY % (
        config.d7_start,
        config.d7_end,
        impactedComponent,
        impactedDimension,
    )
    metric_value = calculate_response(query)
    return metric_value


def checkForAnomaly(currentValue, upperThreshold, lowerThreshold):
    anomaly = "NO"
    if config.THRESHOLD_CHECK_TYPE == "B":
        if currentValue > upperThreshold or currentValue < lowerThreshold:
            anomaly = "YES"
    elif config.THRESHOLD_CHECK_TYPE == "U":
        if currentValue > upperThreshold:
            anomaly = "YES"
    elif config.THRESHOLD_CHECK_TYPE == "L":
        if currentValue < lowerThreshold:
            anomaly = "YES"

    return anomaly


def pushDataToInflux(
    impactedComponent,
    impactedDimension,
    currentValue,
    dataPointList,
    mean,
    stdDev,
    deviation,
    upperThreshold,
    lowerThreshold,
    anomaly,
):
    influxDataPoint, tags, fields = {}, {}, {}
    tags["opco"] = config.OPCO
    tags["application"] = config.DEFAULT_APPLICATION
    tags["businessServicePath"] = config.DEFAULT_BUSINESS_SERVICE_PATH
    tags["metricName"] = config.METRIC_NAME
    tags["description"] = config.METRIC_DESCRIPTION
    if impactedComponent in config.dpMap:
        tags["impactedComponent"] = config.dpMap[impactedComponent]
    else:
        tags["impactedComponent"] = impactedComponent
    tags["impactedDimension"] = impactedDimension
    tags["thresholdCheckType"] = config.THRESHOLD_CHECK_TYPE
    tags["anomaly"] = anomaly

    fields["currentValue"] = float(currentValue)
    for increment in range(0, 7):
        dateKey = "d" + str(increment + 1)
        fields[dateKey] = float(dataPointList[increment][0])
    fields["mean"] = float(mean)
    fields["stdDev"] = float(stdDev)
    fields["deviation"] = float(deviation)
    fields["upperThreshold"] = float(upperThreshold)
    fields["lowerThreshold"] = float(lowerThreshold)

    influxDataPoint["measurement"] = config.ANOMALY_MEASUREMENT
    influxDataPoint["tags"] = tags
    influxDataPoint["fields"] = fields
    # influxDataPoint['time'] = dte - datetime.timedelta(hours=5, minutes=30)  # current_milli_time()
    influxDataPoint["time"] = config.dcurrent_end
    influxJson.append(influxDataPoint)
    return True


if __name__ == "__main__":
    # webHDFSConn = PyWebHdfsClient(host='10.5.246.115', port=9870, user_name='admin')
    resultSet = fetchCurrentDataPoint()
    if resultSet is not None:
        try:
            for virtualServer in resultSet["results"][0]["series"]:
                dataPoints = []
                impactedComponent = virtualServer["tags"][config.IMPACTED_COMPONENT]
                impactedDimension = virtualServer["tags"][config.IMPACTED_DIMENSION]
                if impactedComponent == "":
                    continue
                else:
                    # print(impactedComponent)
                    mean = stdDev = upperThreshold = lowerThreshold = deviation = (
                        recordsObserved
                    ) = 0.0
                    anomaly = "NO"
                    currentValue = round(virtualServer["values"][0][1], 2)
                    day1Value = fetchDay1DataPoint(impactedComponent, impactedDimension)
                    day2Value = fetchDay2DataPoint(impactedComponent, impactedDimension)
                    day3Value = fetchDay3DataPoint(impactedComponent, impactedDimension)
                    day4Value = fetchDay4DataPoint(impactedComponent, impactedDimension)
                    day5Value = fetchDay5DataPoint(impactedComponent, impactedDimension)
                    day6Value = fetchDay6DataPoint(impactedComponent, impactedDimension)
                    day7Value = fetchDay7DataPoint(impactedComponent, impactedDimension)
                    dataPointList = [
                        day1Value,
                        day2Value,
                        day3Value,
                        day4Value,
                        day5Value,
                        day6Value,
                        day7Value,
                    ]
                    for dataPoint in dataPointList:
                        if dataPoint[1] == "YES":
                            dataPoints.append(dataPoint[0])
                        else:
                            pass
                    if (
                        day1Value[0] == 0
                        and day2Value[0] == 0
                        and day3Value[0] == 0
                        and day4Value[0] == 0
                        and day5Value[0] == 0
                        and day6Value[0] == 0
                        and day7Value[0] == 0
                    ):
                        pass
                    else:
                        mean = round(statistics.mean(dataPoints), 2)
                        if len(dataPoints) < 2:
                            stdDev = 0.0
                        else:
                            stdDev = round(statistics.stdev(dataPoints), 2)
                        deviation = round((((currentValue - mean) * 100) / mean), 2)
                        recordsObserved = len(dataPoints)
                        upperThreshold = round(
                            (mean + (config.STDDEV_FACTOR * stdDev)), 2
                        )
                        lowerThreshold = round(
                            (mean - (config.STDDEV_FACTOR * stdDev)), 2
                        )
                        anomaly = checkForAnomaly(
                            currentValue, upperThreshold, lowerThreshold
                        )
                    currentValue = float(currentValue)

                    print(
                        impactedComponent,
                        impactedDimension,
                        currentValue,
                        dataPointList,
                        mean,
                        stdDev,
                        deviation,
                        upperThreshold,
                        lowerThreshold,
                        anomaly,
                    )
                    if pushDataToInflux(
                        impactedComponent,
                        impactedDimension,
                        currentValue,
                        dataPointList,
                        mean,
                        stdDev,
                        deviation,
                        upperThreshold,
                        lowerThreshold,
                        anomaly,
                    ):
                        del dataPoints
                    else:
                        pass
            influxClient.switch_database(config.ANOMALY_DATABASE)
            # print(influxJson)
            influxClient.write_points(influxJson)

        except KeyError as err:
            print(err)
            sys.exit(1)
