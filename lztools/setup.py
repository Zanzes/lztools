#!/usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='lztools',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.2.18',
    license='MIT License',
    description='A collection of useful utilities by Laz aka Zanzes',
    packages=find_packages(),
    py_modules=[
        'file_rotator',
        'alarm',
        'work_logger',
        'network',
        'zlick',
        'pathing',
        'lzconstants'
    ],
    entry_points={
        'console_scripts': [
            '¤          = lztools:main',
            'parse-work = utils:parse_work',
            'log-work   = utils:log_work',
            'alarm      = utils:alarm',

        ],
    },
    install_requires=['pip', 'click'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)

