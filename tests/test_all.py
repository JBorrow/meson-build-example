"""
Test the library works.
"""

import pytest
import ctypes


def test_import_c_wrapper():
    from mytestlib import c_wrapper


def test_c_wrapper_value():
    from mytestlib import c_wrapper

    assert c_wrapper.multiply_by_two(2) == 4

    with pytest.raises(ctypes.ArgumentError):
        c_wrapper.multiply_by_two(2.0)


def test_import_f_wrapper():
    from mytestlib import fortran_wrapper


def test_fortran_wrapper_value():
    from mytestlib import fortran_wrapper

    assert fortran_wrapper.add_two(2.0) == 4.0


def test_import_cython_wrapper():
    from mytestlib import cython_wrapper


def test_cython_wrapper_value():
    from mytestlib import cython_wrapper

    assert cython_wrapper.min_and_max(4, 3) == (3, 4)
