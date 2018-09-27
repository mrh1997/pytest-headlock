#!python3.6
# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path


README_PATH = Path(__file__).parent / 'README.md'


setup(
    name='pytest-headlock',
    version='0.1.0',
    description='Some pytest plugins and helper modules to simplify using '
                'headlock with pytest',
    long_description=README_PATH.read_text(),
    long_description_content_type='text/markdown',
    author='Robert Hölzl',
    author_email='robert.hoelzl@posteo.de',
    url='https://github.com/mrh1997/pytest-headlock',
    packages=['pytest_headlock'],
    install_requires=['headlock >= 0.4.0,< 0.5.0', 'pytest >= 3.3.2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ],
    entry_points = {
        'pytest11': [
            'headlock-debug-support = pytest_headlock.plugin_headlock_debug',
            'headlock-report-error = pytest_headlock.plugin_headlock_report',
        ]
    },
)
