import cx_Oracle
from elasticsearch import Elasticsearch
from datetime import datetime, timezone
import config
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get the current date
current_date = datetime.now()

# Format the date as 'YYYY.MM.DD'
formatted_date = current_date.strftime("%Y.%m.%d")

# Elastic connection string
es = Elasticsearch(
    [
        {
            "host": config.elastic_host,
            "port": config.elastic_port,
            "scheme": config.elastic_scheme,
        }
    ],
    http_auth=(config.elastic_username, config.elastic_password),
    verify_certs=config.elastic_certs_verify,
)

# Elasticsearch index format
ES_INDEX = f"{config.elastic_index_name}-{formatted_date}"

# Iterate over each database configuration
for db_config in config.databases:
    try:
        # Construct the DSN
        db_dsn = f"{db_config['db_host']}:{db_config['db_port']}/{db_config['db_service_name']}"

        connection = cx_Oracle.connect(
            user=db_config["db_user"], password=db_config["db_password"], dsn=db_dsn
        )

        # Obtain a cursor
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(config.db_query)

        # Loop over the result set
        for row in cursor:
            if row[0] is None:
                db_ac_type = "Never_Expiry"
                expiry_days = 0
                expiry_date = "N/A"
            else:
                db_ac_type = "Expiry"
                expiry_days = (row[0] - current_date).days
                expiry_date = row[0].strftime("%Y.%m.%d")
                db_ac_type = "Expiry"

            elastic_date_time = datetime.now(timezone.utc)
            elastic_data = {
                "@timestamp": elastic_date_time,
                "expiry_days": expiry_days,
                "expiry_date": expiry_date,
                "opco": config.opco,
                "db_user": db_config["db_user"],
                "db_host": db_config["db_host"],
                "db_service_name": db_config["db_service_name"],
                "db_port": db_config["db_port"],
                "db_ac_type": db_ac_type,
                "app_name": db_config["app_name"],
            }

            # Send data into elasticsearch
            response = es.index(index=ES_INDEX, document=elastic_data)
            print(response)

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except Exception as e:
        print(e)
