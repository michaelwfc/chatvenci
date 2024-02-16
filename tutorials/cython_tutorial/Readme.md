# Tutorials
- https://pythonprogramming.net/introduction-and-basics-cython-tutorial/
- [Cythonizing your code for beginners](https://medium.com/@miguel.otero.pedrido.1993/cythonizing-your-code-for-beginners-6c7eba2b38ae)
- [Cython: Blend the Best of Python and C++ | SciPy 2015 Tutorial | Kurt Smith](https://www.youtube.com/watch?v=gMvkiQ-gOW8&t=4730s)


# Cython Syntax
## cdef declarations:
```python

cdef int x,y,z
cdef char *s
cdef float x = 5.2 (single precision)
cdef double x = 40.5 (double precision)
cdef list languages
cdef dict abc_dict
cdef object thing
```


# Build
$ python setup.py build_ext --inplace

% This should create a build directory, a C file (.c), and a Shared Object file (.so). 
% With this, we can import our C-extension.

% Compiling example_cython.pyx because it changed.
% [1/1] Cythonizing example_cython.pyx
% D:\projects\cslab\pyenv\Lib\site-packages\Cython\Compiler\Main.py:381: FutureWarning: Cython directive 'language_level' not set, using '3str' for now (Py3). This has changed from earlier releases! File: D:\projects\cslab\tutorials\cython_tutorial\example_cython.pyx
%   tree = Parsing.p_module(s, pxd, full_module_name)
% running build_ext
% building 'example_cython' extension
% creating build
% creating build\temp.win-amd64-cpython-311
% creating build\temp.win-amd64-cpython-311\Release
% "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.39.33519\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -ID:\projects\cslab\pyenv\include -IC:\Users\C4565\.conda\envs\py311\include -IC:\Users\C4565\.conda\envs\py311\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.39.33519\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /Tcexample_cython.c /Fobuild\temp.win-amd64-cpython-311\Release\example_cython.obj
% example_cython.c
% creating D:\projects\cslab\tutorials\cython_tutorial\build\lib.win-amd64-cpython-311
% "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.39.33519\bin\HostX86\x64\link.exe" /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO /LIBPATH:D:\projects\cslab\pyenv\libs /LIBPATH:C:\Users\C4565\.conda\envs\py311\libs /LIBPATH:C:\Users\C4565\.conda\envs\py311 /LIBPATH:D:\projects\cslab\pyenv\PCbuild\amd64 "/LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.39.33519\lib\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.22621.0\ucrt\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\\lib\10.0.22621.0\\um\x64" /EXPORT:PyInit_example_cython build\temp.win-amd64-cpython-311\Release\example_cython.obj /OUT:build\lib.win-amd64-cpython-311\example_cython.cp311-win_amd64.pyd /IMPLIB:build\temp.win-amd64-cpython-311\Release\example_cython.cp311-win_amd64.lib
%   正在创建库 build\temp.win-amd64-cpython-311\Release\example_cython.cp311-win_amd64.lib 和对象 build\temp.win-amd64-cpython-311\Release\example_cython.cp311-win_amd64.exp
% 正在生成代码
% 已完成代码的生成
% copying build\lib.win-amd64-cpython-311\example_cython.cp311-win_amd64.pyd ->



