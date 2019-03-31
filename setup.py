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
        'lztools',
        'lztools.enums',
        'lztools.linux',
        'lztools.lztext',
        'lztools.pytools',
        'lztools.web'
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'pip',
        'click', 'selenium', 'urllib3'
    ],
    entry_points={
        'console_scripts': [
             'pytools = cli.pytools_cli:main',
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

