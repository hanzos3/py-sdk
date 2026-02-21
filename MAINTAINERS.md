# For maintainers only

## Responsibilities

### Setup your py-sdk Github Repository
Fork [py-sdk upstream](https://github.com/hanzos3/py-sdk/fork) source repository to your own personal repository.
```sh
$ git clone git@github.com:hanzos3/py-sdk
$ cd py-sdk
$ pip install --user --upgrade twine
```

### Modify package version
```sh
$ cat minio/__init__.py
...
...
__version__ = '7.2.20'
...
...

```

### Build and verify
```sh
$ make
$ python setup.py register
$ python setup.py sdist bdist bdist_wheel
```

### Publishing new packages

#### Setup your pypirc
Create a new `pypirc`

```sh
$ cat >> $HOME/.pypirc << EOF
[distutils]
index-servers =
    pypi

[pypi]
username:hanzos3
password:**REDACTED**
EOF

```

#### Upload to pypi
Upload the release artifacts, please install twine v1.8.0+ for following steps to work properly.
```sh
$ twine upload dist/*
```

### Tag
Tag your release commit.
```
$ git tag -s 7.2.20
$ git push
$ git push --tags
```

### Announce
Announce new release by adding release notes at https://github.com/hanzos3/py-sdk/releases. Release notes requires two sections `highlights` and `changelog`. Highlights is a bulleted list of salient features in this release and Changelog contains list of all commits since the last release.

To generate `changelog`
```sh
git log --no-color --pretty=format:'-%d %s (%cr) <%an>' <last_release_tag>..<latest_release_tag>
```
