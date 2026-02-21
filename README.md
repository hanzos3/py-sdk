# Hanzo S3 Python SDK for Amazon S3 Compatible Cloud Storage [![Apache V2 License](https://img.shields.io/badge/license-Apache%20V2-blue.svg)](https://github.com/hanzos3/py-sdk/blob/main/LICENSE)

The Hanzo S3 Python SDK provides high-level APIs to access any Hanzo S3 object storage server or other Amazon S3 compatible service.

This quickstart guide covers how to install the SDK, connect to an object storage service, and create a sample file uploader.

The example below uses:
- [Python version 3.10+](https://www.python.org/downloads/)
- The Hanzo S3 server ([github.com/hanzoai/s3](https://github.com/hanzoai/s3))

For a complete list of APIs and examples, see the [Python SDK Documentation](https://hanzo.space/docs/sdk/python/).

## Install the Hanzo S3 Python SDK

The Python SDK requires Python version 3.10+.
You can install the SDK with `pip` or from the [`hanzos3/py-sdk` GitHub repository](https://github.com/hanzos3/py-sdk):

### Using `pip`

```sh
pip3 install minio
```

### Using Source From GitHub

```sh
git clone https://github.com/hanzos3/py-sdk
cd py-sdk
python setup.py install
```

## Create a Client

To connect to the target service, create a client using the `Minio()` method with the following required parameters:

| Parameter    | Description                                            |
|--------------|--------------------------------------------------------|
| `endpoint`   | URL of the target service.                             |
| `access_key` | Access key (user ID) of a user account in the service. |
| `secret_key` | Secret key (password) for the user account.            |

For example:

```py
from minio import Minio

client = Minio(
    endpoint="s3.hanzo.ai",
    access_key="YOUR-ACCESS-KEY",
    secret_key="YOUR-SECRET-KEY",
)
```

## Example - File Uploader

This example does the following:

- Connects to the Hanzo S3 server using the provided credentials.
- Creates a bucket named `python-test-bucket` if it does not already exist.
- Uploads a file named `test-file.txt` from `/tmp`, renaming it `my-test-file.txt`.

### `file_uploader.py`

```py
# file_uploader.py Hanzo S3 Python SDK example
from minio import Minio
from minio.error import S3Error

def main():
    # Create a client with the Hanzo S3 server, its access key
    # and secret key.
    client = Minio(
        endpoint="s3.hanzo.ai",
        access_key="YOUR-ACCESS-KEY",
        secret_key="YOUR-SECRET-KEY",
    )

    # The file to upload, change this path if needed
    source_file = "/tmp/test-file.txt"

    # The destination bucket and filename on the Hanzo S3 server
    bucket_name = "python-test-bucket"
    destination_file = "my-test-file.txt"

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name=bucket_name)
    if not found:
        client.make_bucket(bucket_name=bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name=bucket_name,
        object_name=destination_file,
        file_path=source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
```

To run this example:

1. Create a file in `/tmp` named `test-file.txt`.
   To use a different path or filename, modify the value of `source_file`.

2. Run `file_uploader.py` with the following command:

```sh
python file_uploader.py
```

If the bucket does not exist on the server, the output resembles the following:

```sh
Created bucket python-test-bucket
/tmp/test-file.txt successfully uploaded as object my-test-file.txt to bucket python-test-bucket
```

## More References

* [Python SDK Documentation](https://hanzo.space/docs/sdk/python/)
* [Examples](https://github.com/hanzos3/py-sdk/tree/main/examples)

## Explore Further

* [Hanzo S3 Server](https://github.com/hanzoai/s3)
* [Hanzo Space](https://hanzo.space)

## Contribute

[Contributors Guide](https://github.com/hanzos3/py-sdk/blob/main/CONTRIBUTING.md)

## License

This SDK is distributed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0), see [LICENSE](https://github.com/hanzos3/py-sdk/blob/main/LICENSE) and [NOTICE](https://github.com/hanzos3/py-sdk/blob/main/NOTICE) for more information.

[![PYPI](https://img.shields.io/pypi/v/minio.svg)](https://pypi.python.org/pypi/minio)
