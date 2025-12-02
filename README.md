# maybe-compute

[![License](https://img.shields.io/pypi/l/maybe-compute.svg?color=green)](https://github.com/ianhi/maybe-compute/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/maybe-compute.svg?color=green)](https://pypi.org/project/maybe-compute)
[![Python Version](https://img.shields.io/pypi/pyversions/maybe-compute.svg?color=green)](https://python.org)
[![CI](https://github.com/ianhi/maybe-compute/workflows/ci/badge.svg)](https://github.com/ianhi/maybe-compute/actions)
[![codecov](https://codecov.io/gh/ianhi/maybe-compute/branch/master/graph/badge.svg)](https://codecov.io/gh/ianhi/maybe-compute)

To disk caching of computationally intensive functions.

## Usage

```python
from maybe_compute import maybe_compute, set_maybe_compute_folder
import xarray as xr
import numpy as np

def dataset_maker(a, b):
    "this docstring shows thanks to functools.wraps!"
    return xr.Dataset({"images":xr.DataArray(np.random.randn(10,20)*a +b, dims=('a','b'))})

set_maybe_compute_folder('sign-flip-cartoon')
maybe_compute(dataset_maker,  'yikes.nc')(4,5)

```

## Install

I strongly recommend pinning to a known version as the API may change dramatically until version 1.0 is published.

```bash
pip install maybe-compute==0.1.0
```
