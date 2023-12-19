"""Carculator_truck init file.

List of all submodules.

Submodules
==========

.. autosummary::
    :toctree: _autosummary


"""

from carculator_utils.array import fill_xarray_from_input_parameters

from .driving_cycles import get_driving_cycle
from .inventory import InventoryTruck
from .model import TruckModel
from .truck_input_parameters import TruckInputParameters

__all__ = (
    "TruckInputParameters",
    "fill_xarray_from_input_parameters",
    "TruckModel",
    "InventoryTruck",
    "get_driving_cycle",
)

# library version
__version__ = (0, 4, 0)
