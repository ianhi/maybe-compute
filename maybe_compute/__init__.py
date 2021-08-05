try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
__author__ = 'Ian Hunt-Isaak'
__email__ = "ianhuntisaak@gmail.com"

from functools import wraps
from pathlib import Path
import xarray as xr

_maybe_compute_path = Path(".")


def set_maybe_compute_folder(folder_name, autocreate=True):
    global _maybe_compute_path
    p = Path(folder_name)
    if not p.exists() and not autocreate:
        raise FileNotFoundError("Folder does not exist and *autocreate* is False")
    p.mkdir(parents=True, exist_ok=True)
    _maybe_compute_path = p


def maybe_compute(function, disk_name):
    global _maybe_compute_path

    @wraps(function)
    def wrapper(*args, **kwargs):
        global _maybe_compute_path
        p = _maybe_compute_path.joinpath(disk_name)
        if p.exists():
            print(f"loading from {str(p)} instead of recomputing")
            return xr.load_dataset(p)
        ds = function(*args, **kwargs)
        ds.to_netcdf(p)
        return ds

    return wrapper


__all__ = [
    "set_maybe_compute_folder",
    "maybe_compute",
]
