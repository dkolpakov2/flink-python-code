#!/bin/bash
# Triggers a Flink job via Flink streaming python API

/opt/flink/bin/pyflink-stream.sh /app/src/hello_world.py

/opt/flink/bin/pyflink-stream.sh /opt/flink/examples/python/table/hello_world.py
