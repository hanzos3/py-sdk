#!/usr/bin/env bash
#
# Hanzo S3 Python Library for Amazon S3 Compatible Cloud Storage, (C) 2020 Hanzo AI, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

function run_minio_server() {
	if [ ! -f tests/functional/minio ]; then
		wget --quiet --output-document tests/functional/minio https://github.com/hanzoai/s3/releases/latest/download/s3-linux-amd64
		chmod +x tests/functional/minio
	fi

	export S3_KMS_KES_ENDPOINT=https://play.min.io:7373
	export S3_KMS_KES_KEY_FILE=tests/functional/play.min.io.kes.root.key
	export S3_KMS_KES_CERT_FILE=tests/functional/play.min.io.kes.root.cert
	export S3_KMS_KES_KEY_NAME=my-minio-key
	export S3_NOTIFY_WEBHOOK_ENABLE_miniopytest=on
	export S3_NOTIFY_WEBHOOK_ENDPOINT_miniopytest=http://example.org/
	export SQS_ARN="arn:minio:sqs::miniopytest:webhook"
	export S3_CI_CD=1
	tests/functional/minio server --config-dir tests/functional/.cfg tests/functional/.d{1...4} >tests/functional/minio.log 2>&1 &
}

if [ -z ${SERVER_ENDPOINT+x} ]; then
	run_minio_server
	S3_PID=$!
	trap 'kill -9 ${S3_PID} 2>/dev/null' INT

	export MINT_MODE=full
	export SERVER_ENDPOINT=localhost:9000
	export ACCESS_KEY=minioadmin
	export SECRET_KEY=minioadmin
	export ENABLE_HTTPS=0
fi

PYTHONPATH=$PWD python tests/functional/tests.py
if [ -n "$S3_PID" ]; then
	kill -9 "$S3_PID" 2>/dev/null
fi
