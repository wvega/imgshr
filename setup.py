# coding: utf-8

import os

from setuptools import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='ImgShr',
    version='0.0.1',
    author='Willington Vega',
    author_email='wvega@wvega.com',
    description=('A script to upload images to ImgShr.com service.'),
    long_description=read('README.md'),
    license='GPL',
    keywords='image upload imgshr.com',
    url='https://github.com/wvega/imgshr',
    packages=['imgshr'],
    package_data={},
    scripts=['bin/imgshr'],
    install_requires=['requests'],
    classifiers=["Development Status :: 3 - Alpha"],
    test_suite='tests.suite'
)
