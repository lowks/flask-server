#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from flask_server import VERSION

setup(
    name = "flask-server",
    version = VERSION,
    url = 'http://ondrejsika.com/docs/flask-server',
    download_url = 'https://github.com/sikaondrej/flask-server',
    license = 'GNU LGPL v.3',
    description = "",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    requires = ["flask", ],
    include_package_data = True,
    zip_safe = False,
)
