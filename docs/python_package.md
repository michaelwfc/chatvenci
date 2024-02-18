# Reference
[花了两天，终于把 Python 的 setup.py 给整明白了](https://zhuanlan.zhihu.com/p/276461821)
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/#packaging-python-projects)
[Packaging and distributing projects](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)

[An Introduction to Distutils](https://docs.python.org/3.10/distutils/introduction.html)

# Python package tools
## distutils 
distutils 是 Python 的一个标准库，从命名上很容易看出它是一个分发（distribute）工具（utlis），它是 Python 官方开发的一个分发打包工具，所有后续的打包工具，全部都是基于它进行开发的。
distutils 的精髓在于编写 setup.py，它是模块分发与安装的指导文件

## setuptools
setuptools 是 distutils 增强版，不包括在标准库中。其扩展了很多功能，能够帮助开发者更好的创建和分发 Python 包。大部分 Python 用户都会使用更先进的 setuptools 模块


# 源码包与二进制包
## 源码包
- 源码包安装的过程，是先解压，再编译，最后才安装，所以它是跨平台的，由于每次安装都要进行编译，相对二进包安装方式来说安装速度较慢。

## 二进制包
二进制包的安装过程省去了编译的过程，直接进行解压安装，所以安装速度较源码包来说更快。
由于不同平台的编译出来的包无法通用，所以在发布时，需事先编译好多个平台的包。
 - egg
 - wheel




# Python Packaging and distributing projects

## 1. 编写 setup.py 文件


### ext_modules

ext_modules 参数用于构建 C 和 C++ 扩展扩展包。其是 Extension 实例的列表，每一个 Extension 实例描述了一个独立的扩展模块，扩展模块可以设置扩展包名，头文件、源文件、链接库及其路径、宏定义和编辑参数等。



## 2. MANIFEST.in 的文件
控制文件的分发
MANIFEST.in 需要放在和 setup.py 同级的顶级目录下，setuptools 会自动读取该文件

```in
include *.txt
recursive-include examples *.txt *.py
prune examples/sample?/build

```

# 如何使用 setup.py 构建包
## 1. 构建源码发布包。
用于发布一个 Python 模块或项目，将源码打包成 tar.gz （用于 Linux 环境中）或者 zip 压缩包（用于 Windows 环境中）
```shell
$python setup.py sdist
```
## 2.构建二进制分发包。
- 在windows中我们习惯了双击 exe 进行软件的安装，Python 模块的安装也同样支持 打包成 exe 这样的二进制软件包。
```shell
$ python setup.py bdist_wininst
```

- 在 Linux 中，大家也习惯了使用 rpm 来安装包，对此你可以使用这条命令实现 rpm 包的构建
```shell
$ python setup.py bdist_rpm
```


- 若你喜欢使用 easy_install 或者 pip 来安装离线包。你可以将其打包成 egg 包
```shell
$ python setup.py bdist_egg
```


- 若你的项目，需要安装多个平台下，既有 Windows 也有 Linux，按照上面的方法，多种格式我们要执行多次命令，为了方便，你可以一步到位，执行如下这条命令，即可生成多个格式的进制
```shell
$ python setup.py bdist
```


## 如何使用 setup.py 安装包
- 将你的模块安装至系统全局环境中
$ python setup.py install  

- 如若你的项目还处于开发阶段，频繁的安装模块，也是一个麻烦事。
这时候你可以使用这条命令安装，该方法不会真正的安装包，而是在系统环境中创建一个软链接指向包实际所在目录。这边在修改包之后不用再安装就能生效，便于调试。
$ python setup.py develop


## 如何发布包到 PyPi
如果要发布自己的包，需要先到 pypi 上注册账号。然后创建 ~/.pypirc 文件，此文件中配置 PyPI 访问地址和账号。如的.pypirc文件内容请根据自己的账号来修改。

典型的 .pypirc 文件

[distutils]
index-servers = pypi

[pypi]
username:xxx
password:xxx


然后使用这条命令进行信息注册，完成后，你可以在 PyPi 上看到项目信息。
$ python setup.py register

注册完了后，你还要上传源码包，别人才使用下载安装
$ python setup.py upload

###  twine 工具
或者也可以使用 twine 工具注册上传，它是一个专门用于与 pypi 进行交互的工具，详情可以参考官网



# Packaging with Cython and C/C++ libs
[Packaging binary extensions](https://packaging.python.org/en/latest/guides/packaging-binary-extensions/)
[Extension Module](https://packaging.python.org/en/latest/glossary/#term-Extension-Module)

