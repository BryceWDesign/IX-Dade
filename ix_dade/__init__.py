"""
IX-Dade Package Initialization

Sets up the IX-Dade module namespace.
"""

from .core.dade_core import DadeCore
from .core.dade_interface import run_dade_cli
from .core.gibson_adapter import GibsonAdapter

__all__ = [
    "DadeCore",
    "run_dade_cli",
    "GibsonAdapter"
]
