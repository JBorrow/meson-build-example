project('mytestlib', ['c', 'fortran', 'cython'])

py = import('python').find_installation(pure: false)

python_sources = [
    'mytestlib/__init__.py',
    'mytestlib/c_wrapper.py',
    'mytestlib/fortran_wrapper.py',
    'mytestlib/cython_wrapper.py',
]

# Python is _very_ simple!
py.install_sources(
    python_sources,
    subdir: 'mytestlib',
)

# C is a little more complex, but as we use
# ctypes in the wrapper is relatively simple
# (just build a dylib).
c_sources = ['c/multiplication.c']

shared_library(
    'testprojectc',
    c_sources,
    install: true,
    install_dir: py.get_install_dir() / 'mytestlib',
)

# Fortran requires f2py.
fortran_sources = ['fortran/addition.f90']

py_dep = py.dependency()

incdir_numpy = run_command(py,
    ['-c', 'import numpy; print(numpy.get_include())'],
    check : true
).stdout().strip()

incdir_f2py = run_command(py,
    ['-c', 'import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

inc_np = include_directories(incdir_numpy, incdir_f2py)

fortran_pyed = custom_target(
    input: fortran_sources,
    output: ['testprojectf90-f2pywrappers2.f90', 'testprojectf90module.c'],
    command: [py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'testprojectf90', '--lower']
)

py.extension_module(
    'testprojectf90',
    ['fortran/addition.f90', fortran_pyed],
    incdir_f2py / 'fortranobject.c',
    include_directories: inc_np,
    dependencies: py_dep,
    install: true,
    install_dir: py.get_install_dir() / 'mytestlib'
)

# Cython

# Need to build helper libraries separately and link them in.
c_helper_sources = ['cython/core.c']

c_helper_lib = shared_library(
    'testprojectsharedlibcython',
    c_helper_sources,
    install: true,
    install_dir: py.get_install_dir() / 'mytestlib'
)

cython_sources = ['cython/cyth_core.pyx']

py.extension_module(
    # Note that this MUST be the same name as the source file
    # or you won't be able to import the extension.
    'cyth_core',
    cython_sources,
    include_directories: ['cython'],
    dependencies: py_dep,
    link_with: [c_helper_lib],
    install: true,
    install_dir: py.get_install_dir() / 'mytestlib'
)
