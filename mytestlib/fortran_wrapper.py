import ctypes
import os

from mytestlib import testprojectf90

def add_two(x: float):
    return testprojectf90.addition.add_two(x)
