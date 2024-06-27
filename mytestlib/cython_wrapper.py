import ctypes
import os

from mytestlib import testprojectcython

def min_and_max(x: int, y: int):
    return testprojectcython.min_and_max(x, y)
