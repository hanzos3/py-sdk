# Hanzo S3 Python SDK - Amazon S3 Compatible Cloud Storage

Hanzo S3 Python SDK provides simple APIs to access any Amazon S3 compatible object storage service.

For complete APIs and examples, see [Python Client API Reference](https://hanzo.space/docs/sdk/python/).

## Requirements

- Python 3.10+

## Install with pip

```sh
pip install minio
```

## Install from source

```sh
git clone https://github.com/hanzos3/py-sdk
cd py-sdk
python setup.py install
```

## Initialize Client

```py
from minio import Minio

client = Minio(
    "s3.hanzo.ai",
    access_key="YOUR-ACCESS-KEY",
    secret_key="YOUR-SECRET-KEY",
    secure=True,
)
```

## Example - File Upload

```py
from minio import Minio
from minio.error import S3Error

client = Minio(
    "s3.hanzo.ai",
    access_key="YOUR-ACCESS-KEY",
    secret_key="YOUR-SECRET-KEY",
    secure=True,
)

# Create bucket
client.make_bucket("my-bucket")

# Upload file
client.fput_object("my-bucket", "my-file.log", "/tmp/my-file.log")
```

## API Documentation

* [Python SDK API Reference](https://hanzo.space/docs/sdk/python/)

## Examples

* [Examples](https://github.com/hanzos3/py-sdk/tree/main/examples)

## Contribute

[Contributors Guide](https://github.com/hanzos3/py-sdk/blob/main/CONTRIBUTING.md)

[![PYPI](https://img.shields.io/pypi/v/minio.svg)](https://pypi.python.org/pypi/minio)
