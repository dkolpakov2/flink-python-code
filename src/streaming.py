## REF:
# https://medium.com/@priyankbhandia_24919/apache-flink-for-data-enrichment-6118d48de04
# 1. 
# python -m pip install apache-flink
# 2.
#  tar -zxvf flink-*.tgz
#
##  log_setting=(-Dlog.file="$log" -Dlog4j.configuration="path\\to\\flink_home\\conf\\log4j-cli.properties" -Dlog4j.configurationFile="path\\to\\flink_home\\conf\\log4j-cli.properties" -Dlogback.configurationFile="path\\to\\flink_home\\conf\\logback.xml")
# 
# exec $JAVA_RUN $JVM_ARGS $FLINK_ENV_JAVA_OPTS "${log_setting[@]}" -classpath "`manglePathList "$CC_CLASSPATH"`" org.apache.flink.client.cli.CliFrontend "$@"
#
#
# run Start cluster:
# ./bin/start-cluster.sh
#  localhost:8081
#
   ###################################################################################
# shell to run:
# before that we need to get python DIR: 
# python3 -c "import sys; print('\n'.join(sys.path))"
# $ which python3
# output will be: /usr/bin/python3
# ~/flink-1.16.1/bin/flink run -py process_movies.py -pyclientexec “/usr/bin/python3.exe” -pyexec “/usr/bin/python3.exe” -—output “out.txt” --input "input.txt"./flink-1.14.3/bin/flink run -py streaming.py -pyclientexec “python3.exe” -pyexec “python3.exe” -—output “out.txt” --input "input.txt"
# ~/flink-1.16.1/bin/flink run -py process_movies.py -pyclientexec “/usr/bin/python3.exe” -pyexec “/usr/bin/python3.exe” -—output “out.txt” --input "input.txt"./flink-1.14.3/bin/flink run -py streaming.py -pyclientexec “python3.exe” -pyexec “python3.exe” -—output “out.txt” --input "input.txt"
#


import argparse
import logging
import sys

from pyflink.common import WatermarkStrategy, Encoder, Types
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors import (FileSource, StreamFormat, FileSink, OutputFileConfig,
                                           RollingPolicy)



def movie_transform(input_path, output_path):
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    # write all the data to one file
    env.set_parallelism(1)
    print("inside word_count")
    # define the source
    
    ds = env.from_source(
        source=FileSource.for_record_stream_format(StreamFormat.text_line_format(),
                                                    input_path)
                            .process_static_file_set().build(),
        watermark_strategy=WatermarkStrategy.for_monotonous_timestamps(),
        source_name="file_source"
    )
    

    def split(line):
        yield from line.split("\n")

    # compute word count
    ds = ds.flat_map(split) \
        .map(lambda i: i.replace("+"," "), output_type=Types.STRING())
        # .key_by(lambda i: i[0]) \
        # .reduce(lambda i, j: (i[0], i[1] + j[1]))
    print("sinking output")
    # define the sink
        
    ds.sink_to(
        sink=FileSink.for_row_format(
            base_path=output_path,
            encoder=Encoder.simple_string_encoder())
        .with_output_file_config(
            OutputFileConfig.builder()
            .build())
        .with_rolling_policy(RollingPolicy.default_rolling_policy())
        .build()
    )
    
    # submit for execution
    env.execute()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        required=False,
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        required=False,
        help='Output file to write results to.')

    argv = sys.argv[1:]
    known_args, _ = parser.parse_known_args(argv)

    movie_transform(known_args.input, known_args.output)