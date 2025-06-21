###
elastic_host = "172.24.30.85"
elastic_port = 9200
elastic_username = "elastic"
elastic_password = "Elastic1234"
elastic_index_name = "test_db_password_expiry"
elastic_certs_verify = False
elastic_scheme = "https"
###
opco = "NGPSB"
###
db_query = "select expiry_date from user_users"
###
databases = [
    {
        "db_user": "GRAFANAUSR",
        "db_password": "JulyOra#123456789",
        "db_host": "NGLPPSBCBDBP-SCAN.africa.airtel.itm",
        "db_port": 1524,
        "db_service_name": "NGCBSPRD",
        "app_name": "CBS",
    },
    {
        "db_user": "GRAFANAUSR",
        "db_password": "JulyOra#123456789",
        "db_host": "172.24.30.165",
        "db_port": 1521,
        "db_service_name": "AGENCYDB",
        "app_name": "CEVA",
    },
    {
        "db_user": "GRAFANAUSR",
        "db_password": "August#123456789",
        "db_host": "172.24.30.193",
        "db_port": 1908,
        "db_service_name": "NGPSBPRD",
        "app_name": "MOBIQUITY",
    },
    # Add more database configurations here
]
