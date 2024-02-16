from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

"""
python setup.py build_ext --inplace
"""
# Use the cythonize method to tell Cython which files to be translated and compiled
# setup(name="example_cy", ext_modules = cythonize('example_cython.pyx'))

extensions = [
    Extension(
        name="example_cython",
        sources=["example_cython.pyx"],
        # language="c++",
        # extra_compile_args=["/utf-8"],
   ),
    Extension(
        name="fib_cython",
        sources=["fib_cython.pyx"],
   ),
   Extension(
        name="external_c_funcs",
        sources=["external_c_functions.pyx"],
   )
   ]

ext_modules = cythonize(extensions)

setup(name="cython_examples", ext_modules = ext_modules)