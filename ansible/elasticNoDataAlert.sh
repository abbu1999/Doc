#!/bin/bash
opco="KE"
date=$(date '+%Y-%m-%d')
processFile=/opt/index.txt
curl -k --noproxy '*' -XGET "https://elastic:Elastic1234@172.23.0.51:9200/_cat/indices" | awk '{print $3}' | grep -v '^\.' | awk -F '[-_][0-9]{4}\\.[0-9]{2}\\.[0-9]{2}|[-_][0-9]{4}\\-[0-9]{2}\\-[0-9]{2}$' '{print $1}' | uniq > /opt/index.txt
while IFS= read -r index
do
        timestamp=$(date --utc "+%Y-%m-%dT%H:%M:%S")
        docCount=$(curl -k --noproxy '*' -XGET "https://elastic:Elastic1234@172.23.0.51:9200/$index*/_search" -H 'Content-Type: application/json' -d' {"query":{"bool":{"must":[],"filter":[{"range":{"@timestamp":{"format":"strict_date_optional_time","gte":"now-15m","lte":"now"}}}],"should":[],"must_not":[]}}}'|jq '.hits.total.value')
        echo $index $docCount $opco
        if [ $docCount -lt 20 ];
        then
                curl -k --noproxy '*' -XPOST "https://elastic:Elastic1234@172.23.0.51:9200/elastic_no_data-$date/_doc" -H 'Content-Type: application/json' -d'{"index": "'$index'","docCount": '$docCount',"opco": "'$opco'","@timestamp": "'$timestamp'"}'
        fi
done < $processFile