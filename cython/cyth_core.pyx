import cython
cimport cyth_core as core

def min_and_max(a, b):
    return core.min(a, b), core.max(a, b)
