from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'an easier way to store data'
LONG_DESCRIPTION = 'A package that makes it eaiser to store data with datapacks..'

# Setting up
setup(
    name="xldata",
    version=VERSION,
    author="chanakya",
    author_email="<chanakyaramsai@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['dill'],
    keywords=['xldata'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
