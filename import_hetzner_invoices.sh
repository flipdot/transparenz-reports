#!/bin/bash

SCRIPT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
OUTPUT_PATH="$SCRIPT_PATH/data/running_expenses/hcloud"

if [ -z "$1" ]; then
    echo "Usage: $0 <DIRECTORY_PATH>"
    exit
fi;

for csv_path in $1/Hetzner_*.csv; do
    timestamp=$(echo $csv_path | grep -Po "(?<=Hetzner_)\d{4}-\d{2}-\d{2}");
    echo "Converting $csv_path..."
    poetry run hetzner-fix-report $csv_path -o "$OUTPUT_PATH/$timestamp.csv"
done

