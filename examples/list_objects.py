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

from minio import Minio

client = Minio(
    endpoint="s3.hanzo.ai",
    access_key="YOUR-ACCESS-KEY",
    secret_key="YOUR-SECRET-KEY",
)

# List objects information.
objects = client.list_objects(bucket_name="my-bucket")
for obj in objects:
    print(obj)

# List objects information whose names starts with "my/prefix/".
objects = client.list_objects(bucket_name="my-bucket", prefix="my/prefix/")
for obj in objects:
    print(obj)

# List objects information recursively.
objects = client.list_objects(bucket_name="my-bucket", recursive=True)
for obj in objects:
    print(obj)

# List objects information recursively whose names starts with
# "my/prefix/".
objects = client.list_objects(
    bucket_name="my-bucket", prefix="my/prefix/", recursive=True,
)
for obj in objects:
    print(obj)

# List objects information recursively after object name
# "my/prefix/world/1".
objects = client.list_objects(
    bucket_name="my-bucket", recursive=True, start_after="my/prefix/world/1",
)
for obj in objects:
    print(obj)
