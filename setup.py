#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "flask-server",
    version = "1.2.1",
    url = 'http://ondrejsika.com/docs/flask-server',
    download_url = 'https://github.com/sikaondrej/flask-server',
    license = 'GNU LGPL v.3',
    description = "",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    install_requires = ["flask", ],
    scripts = ["flask_server/bin/flask-server", ],
    include_package_data = True,
    zip_safe = False,
)
