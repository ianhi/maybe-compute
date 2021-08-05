from os import path

import setuptools

# extract version
VERSION_PATH = path.realpath("maybe_compute/_version.py")
version_ns = {}
with open(VERSION_PATH, encoding="utf8") as STREAM:
    exec(STREAM.read(), {}, version_ns)
version = version_ns["__version__"]


if __name__ == "__main__":
    setuptools.setup(
        version=version_ns["__version__"],
    )
