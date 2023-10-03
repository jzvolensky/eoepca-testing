#!/bin/bash


if [ -n "$CUSTOM_CONFIG_FILE" ]; then
  CONFIG_FILE="$CUSTOM_CONFIG_FILE"
else
  CONFIG_FILE="/default_config.json" 
fi

python script1.py --config "$CONFIG_FILE"
python script2.py --config "$CONFIG_FILE"