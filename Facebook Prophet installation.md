# Prophet Installation in Python
Prophet is on PyPI, so you can use pip to install it:

The major dependency that Prophet has is pystan. PyStan has its own installation instructions. http://pystan.readthedocs.io/en/latest/installation_beginner.html
 

## Windows
On Windows, PyStan requires a compiler so you’ll need to follow the instructions.  
https://pystan.readthedocs.io/en/latest/windows.html#


### Installing C++ compiler
There are several ways to install mingw-w64 compiler toolchain, but in these instructions install compiler with conda package manager which comes with the Anaconda package.

To install mingw-w64 compiler type:

conda install libpython m2w64-toolchain -c msys2

### Then install pystan and fbprophet

*Install pystan with pip before using pip to install fbprophet*  
$ conda install pystan  
$  
$ pip install fbprophet   
  