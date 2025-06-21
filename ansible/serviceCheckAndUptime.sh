#!/bin/bash

serviceStatusCheck(){
        serviceStatus=`systemctl is-active $service`
        serviceEnable=`systemctl is-enabled $service`
        echo $service $serviceStatus
        if [ $serviceStatus != "active" ];
        then
                #echo $service $serviceStatus
                systemctl restart $service
                systemctl enable $service
        elif [ $serviceEnable != "enabled" ];
        then
                #echo $service $serviceStatus
                systemctl enable $service
        fi
}

serviceUptimeCheck(){
        ip=`hostname -I | awk '{print $1}'`
        opco="SC"
        serviceActiveTime=`systemctl show -p ActiveEnterTimestamp --value $service`
        serviceActiveTimeEpoch=`date -d "$serviceActiveTime" +"%s"`
        currentTime=`date +%s`
        serviceRestartedTime=$(( currentTime - serviceActiveTimeEpoch))
        #echo $ip $opco $service $serviceActiveTime $serviceActiveTimeEpoch $currentTime $serviceRestartedTime
        if [ $serviceRestartedTime -lt 120 ];
        then
                echo "restarted/crashing" $ip $opco $service $serviceRestartedTime
        #else
        #       echo "running" $ip $opco $service $serviceRestartedTime
        fi
}

for service in 'elasticsearch' 'logstash' 'kibana' 'grafana-server' 'metricbeat' 'heartbeat-elastic' 'kafka' 'zookeeper' 'influxdb' 'telegraf' 'filebeat'
do
        serviceCheck=`systemctl list-unit-files | grep -E  $service.service | wc -l`
        if [ $serviceCheck -gt 0 ];
        then
                serviceStatusCheck $service
                serviceUptimeCheck $service
        fi
done

####

#!/bin/bash

serviceStatusCheck(){
        serviceStatus=`systemctl is-active $service`
        serviceEnable=`systemctl is-enabled $service`
        echo $service $serviceStatus
        if [ $serviceStatus != "active" ];
        then
                #echo $service $serviceStatus
                systemctl restart $service
                systemctl enable $service
        elif [ $serviceEnable != "enabled" ];
        then
                #echo $service $serviceStatus
                systemctl enable $service
        fi
}

serviceUptimeCheck(){
        ip=`hostname -I | awk '{print $1}'`
        opco="KE"
        timestamp=$(date --utc "+%Y-%m-%dT%H:%M:%S")
        date=$(date '+%Y-%m-%d')
        serviceActiveTime=`systemctl show -p ActiveEnterTimestamp --value $service`
        serviceActiveTimeEpoch=`date -d "$serviceActiveTime" +"%s"`
        currentTime=`date +%s`
        serviceRestartedTime=$(( currentTime - serviceActiveTimeEpoch ))
        #echo $ip $opco $service $serviceActiveTime $serviceActiveTimeEpoch $currentTime $serviceRestartedTime
        if [ $serviceRestartedTime -lt 120 ];
        then
                echo "restarted/crashing" $ip $opco $service $serviceRestartedTime
                curl -k --noproxy '*' -XPOST "https://elastic:Elastic1234@172.23.0.51:9200/service_uptime-$date/_doc" -H 'Content-Type: application/json' -d'{"ip": "'$ip'","opco": "'$opco'","service": "'$service'","serviceRestartedTimeInSec": '$serviceRestartedTime',"@timestamp": "'$timestamp'"}'
        #else
        #       echo "running" $ip $opco $service $serviceRestartedTime
        fi
}
getService=$(curl -k --noproxy '*' -XGET -u elastic:Elastic1234 "https://172.23.0.51:9200/mom_service/_search" | jq -r '.hits.hits[]._source.service')
for service in $getService
do
        serviceCheck=`systemctl list-unit-files | grep -E  $service.service | wc -l`
        if [ $serviceCheck -gt 0 ];
        then
                serviceStatusCheck $service
                serviceUptimeCheck $service
        fi
done