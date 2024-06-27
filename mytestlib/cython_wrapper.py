import ctypes
import os

from mytestlib import cyth_core

def min_and_max(x: int, y: int):
    return cyth_core.min_and_max(x, y)
