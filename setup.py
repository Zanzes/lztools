#!/usr/bin/env python3.7

from setuptools import setup

setup(
    name='lztools',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.2.18',
    license='MIT License',
    url="",
    description='A collection of useful utilities by Laz aka Zanzes',
    packages=[
        'cli',
        'lztools',
        'lztools.alarm',
        'lztools.enums',
        'lztools.file_rotator',
        'lztools.generator',
        'lztools.lzassert',
        'lztools.networking',
        'lztools.pytools'
        'lztools.sound',
        'lztools.types',
        'lztools.utils',
        'lztools.work_logger',
        'lzresources',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'scan-network = cli.utils:scan_network',
            'llzenv = cli.llzenv:main',
            'pytools = cli.pytools:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)

