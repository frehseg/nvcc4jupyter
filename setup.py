from distutils.core import setup

setup(
    name='NVCCPlugin',
    version='0.2',
    author='Andrei Nechaev / Goran Frehse',
    author_email='',
    py_modules=['nvcc_plugin'],
    url='htpps://github.com/frehseg/nvcc4jupyter',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++ code',
    long_description=open('README.md').read(),
)
