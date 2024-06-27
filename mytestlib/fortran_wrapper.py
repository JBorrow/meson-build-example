import ctypes
import os

import mytestlib_testprojectf90

def add_two(x: float):
    return mytestlib_testprojectf90.addition.add_two(x)
