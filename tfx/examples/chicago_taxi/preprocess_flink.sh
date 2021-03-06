#!/bin/bash
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
set -u

echo Starting distributed TFT preprocessing...

# Using absolute path to make data accessible to different process started by
# flink.
DATA_DIR=$(pwd)/data
OUTPUT_DIR=$DATA_DIR
SCHEMA_PATH=$DATA_DIR/local_tfdv_output/schema.pbtxt

echo Preprocessing train data...
rm -R -f data/train/local_chicago_taxi_output
$(pwd)/execute_on_flink.sh preprocess.py \
            --input $DATA_DIR/train/data.csv \
            --schema_file $SCHEMA_PATH \
            --output_dir $OUTPUT_DIR/train/local_chicago_taxi_output \
            --outfile_prefix train_transformed

echo Preprocessing eval data...
rm -R -f data/eval/local_chicago_taxi_output
$(pwd)/execute_on_flink.sh preprocess.py \
            --input $DATA_DIR/eval/data.csv \
            --schema_file $SCHEMA_PATH \
            --output_dir $OUTPUT_DIR/eval/local_chicago_taxi_output \
            --outfile_prefix eval_transformed \
            --transform_dir $OUTPUT_DIR/train/local_chicago_taxi_output
