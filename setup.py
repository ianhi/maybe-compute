from os import path
from typing import Dict

import setuptools

# extract version
VERSION_PATH = path.realpath("maybe_compute/_version.py")
version_ns: Dict[str, str] = {}
with open(VERSION_PATH, encoding="utf8") as STREAM:
    exec(STREAM.read(), {}, version_ns)
version = version_ns["__version__"]


if __name__ == "__main__":
    setuptools.setup(
        version=version_ns["__version__"],
    )
