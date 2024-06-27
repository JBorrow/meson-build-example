import ctypes
import os

from mytestlib import mytestlib_testprojectcython

def min_and_max(x: int, y: int):
    return mytestlib_testprojectf90.core.min_and_max(x, y)
