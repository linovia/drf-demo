#!/usr/bin/env python
"""
drf-demo
=====

"""

from setuptools import setup, find_packages


install_requires = [
    "Django==1.8.4",
    "djangorestframework==3.2.3",
]

dev_requires = [
    'django-debug-toolbar',
]

test_requires = [
    "pytest",
    "pytest-cov",
    "pytest-django",
]


setup(
    name="drf_demo",
    version="0.1.0",
    author="Xavier Ordoquy",
    author_email="xordoquy@linovia.com",
    url="https://github.com/linovia/drf-demo",
    description="A collection of use cases for Django REST framework",

    # Packages and data to take into account
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,

    zip_safe=False,  # Avoid eggs

    # Allow pip install .[tests,dev] to install the dev and test dependencies
    extras_require={
        "tests": test_requires,
        "dev": dev_requires,
    },
    install_requires=install_requires,
    tests_require=test_requires,
)
