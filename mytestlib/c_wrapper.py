import ctypes
import os

# We can install the dylib side-by-side, but we'll need
# to find it ourselves.
lib_path = os.path.join(os.path.dirname(__file__), "libtestprojectc.dylib")

shared_c_library = ctypes.CDLL(lib_path)

shared_c_library.multiply_by_two.argtypes = [ctypes.c_int]
shared_c_library.multiply_by_two.restype = ctypes.c_int

def multiply_by_two(x: int):
    return shared_c_library.multiply_by_two(x)
