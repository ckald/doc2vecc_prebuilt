import tokenize
from setuptools import setup
from distutils.extension import Extension


try:
    _detect_encoding = tokenize.detect_encoding
except AttributeError:
    pass
else:
    def detect_encoding(readline):
        try:
            return _detect_encoding(readline)
        except SyntaxError:
            return 'latin-1', []

    tokenize.detect_encoding = detect_encoding


with open("README.md") as f:
    long_description = f.read()


source_files = [
    'doc2vecc/doc2vecc.c',
]

compile_opts = ['-lm', '-pthread', '-O3', '-march=native', '-funroll-loops']
libraries = []


ext = [
    Extension(
        '*',
        source_files,
        extra_compile_args=compile_opts,
        language='c++',
        libraries=libraries,
    )
]


setup(
    name='doc2vecc_prebuilt',
    ext_modules=ext,
    version='0.0.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mchen24/iclr2017',
    author='Chen, Minmin',
    author_email='m.chen@criteo.com',
    license='BSD',
    setup_requires=['wheel'],
    scripts=['doc2vecc/doc2vecc'],
    zip_safe=False,
    classifiers=[
     'Programming Language :: Python :: 2.7',
     'Programming Language :: Python :: 3.5',
     'Programming Language :: Python :: 3.6',
     'Programming Language :: Python :: 3.7',
     'Programming Language :: Python :: 3.8'
    ],
)
