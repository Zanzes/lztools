#!/usr/bin/env python3.7

from setuptools import setup

setup(
    name='lztools.utils',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='0.0.1',
    license='MIT License',
    description='A collection of useful utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙',
    url='',
    py_modules=[
        'lztools.alarm',
        'lztools.file_rotator',
        'lztools.generator',
        'lztools.lzassert',
        'lztools.networking',
        'lztools.sound',
        'lztools.utils',
        'lztools.work_logger',
    ],
    entry_points={
        'console_scripts': [
            'scan-network = cli.utils:scan_network'
        ],
    },
    packages=['cli', 'lztools.'],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'click'
    ]
)

