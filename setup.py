#!/usr/bin/env python3.7

from setuptools import setup
import post_setup

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
        'lztools.enums',
        'lztools.lzenv',
        'lztools.pytools',
        'lztools.types',
        'lztools.text',
        'remote_tools'
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'click',
        'ansiwrap',
        'psutil', 'requests'
    ],
    # dependency_links=[
    #     "git@bitbucket.org:zanzes/lzresources.git"
    # ],
    entry_points={
        'console_scripts': [
            'scan-network = cli.utils:scan_network',
            'pytools = cli.pytools:main',
            'scatter = cli.scatter:scatter',
            'sr = cli.server:sr',
            'server = cli.server:sr',
            'bash-tools = cli.bash_tools:main',
            'clipboard = cli.clipboard:main',
            'currency = cli.currency:main',
            'playlist = cli.playlist:main'
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

post_setup.run()