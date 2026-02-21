# -*- coding: utf-8 -*-
# Hanzo S3 Python Library for Amazon S3 Compatible Cloud Storage, (C)
# [2014] - [2025] Hanzo AI, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timedelta

from minio import Minio
from minio.models import PostPolicy

client = Minio(
    endpoint="s3.hanzo.ai",
    access_key="YOUR-ACCESS-KEY",
    secret_key="YOUR-SECRET-KEY",
)

policy = PostPolicy("my-bucket", datetime.utcnow() + timedelta(days=10))
policy.add_starts_with_condition("key", "my/object/prefix/")
policy.add_content_length_range_condition(1*1024*1024, 10*1024*1024)

form_data = client.presigned_post_policy(policy)

args = " ".join([f"-F {k}={v}" for k, v in form_data.items()])
curl_cmd = (
    "curl -X POST https://s3.hanzo.ai/my-bucket "
    f"{args} -F file=@<FILE> -F key=<OBJECT-NAME>"
)
print(curl_cmd)
