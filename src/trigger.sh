#!/bin/bash
# Triggers a Flink job via Flink streaming python API

/opt/flink/bin/pyflink-stream.sh /app/src/trigger.py

# /app/src/hello_world.py
# export PATH=$PATH: /app/src/
# /opt/flink/bin/pyflink-shell.sh