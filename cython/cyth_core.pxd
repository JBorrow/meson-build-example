import cython

cdef extern from "core.h":
    int min(int a, int b)
    int max(int a, int b)
