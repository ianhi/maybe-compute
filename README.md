# maybe-compute

[![License](https://img.shields.io/pypi/l/maybe-compute.svg?color=green)](https://github.com/ianhi/maybe-compute/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/maybe-compute.svg?color=green)](https://pypi.org/project/maybe-compute)
[![Python Version](https://img.shields.io/pypi/pyversions/maybe-compute.svg?color=green)](https://python.org)
[![CI](https://github.com/ianhi/maybe-compute/workflows/ci/badge.svg)](https://github.com/ianhi/maybe-compute/actions)
[![codecov](https://codecov.io/gh/ianhi/maybe-compute/branch/master/graph/badge.svg)](https://codecov.io/gh/ianhi/maybe-compute)

to disk caching of computationally intensive functions. 

I think this may be a bad idea - probably don't use this. But if you want to then use it like this:


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

```bash
pip install git+https://github.com/ianhi/maybe-compute
```
