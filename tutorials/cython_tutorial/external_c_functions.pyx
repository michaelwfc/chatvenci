"""
[Cython: Blend the Best of Python and C++ | SciPy 2015 Tutorial | Kurt Smith](https://www.youtube.com/watch?v=gMvkiQ-gOW8&t=4730s)


wrapping external C functions (existing C/cpp code to be used in python)  
1. cdef extern from "(the header file.h)"    (essentially the include in cython)
2. declare the interface of the C function (pick the function we need, no need for others), this function signature is checked against the C file to make sure it is correctly used
3. def a python function (wrapper) to call the C function
4. call that python wrapper from other python file/scope
(extra Q 1:41:00) cython declaration can be done in pxd file, so that there is no naming collision between a cython declaration (cimport) and a python function with the same name.
 (point 3 of https://cython.readthedocs.io/en/latest/src/tutorial/pxd_files.html). 
 in short pxd is a declaration file (so similar to .h), and pyx is a implementation file (so similar to .cpp). 
 more read here: https://cython.readthedocs.io/en/latest/src/userguide/sharing_declarations.html

"""

cdef extern from "string.h":
    int strlen(char *c)

def get_len(char *messages):
    return strlen(messages)