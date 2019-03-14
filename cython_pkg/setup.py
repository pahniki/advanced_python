from Cython.Build import cythonize
from distutils.core import setup

setup(
    ext_modules=cythonize("cython_fibo.pyx")
)

# Run command: python setup.py build_ext --inplace
