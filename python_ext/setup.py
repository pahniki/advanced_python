from distutils.core import Extension
from distutils.core import setup

py_ext = Extension('ext_fibo', sources=['ext_fibo.c'])

setup(name='Extension PKG',
      version='1.0',
      description='This is a demo package',
      ext_modules=[py_ext])

# Run command: python setup.py install
