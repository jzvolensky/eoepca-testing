#!/bin/bash

if [ -f "/config/custom_config.yaml" ]; then
    echo "Using custom configuration file."
    cp /config/custom_config.yaml /config/config.yaml
else
    echo "Custom config not found: Using default configuration file."
    cp /config/default_config.yaml /config/config.yaml
fi

