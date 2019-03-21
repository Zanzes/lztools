#!/usr/bin/env python3.7

from setuptools import setup

setup(
    name='lztools',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.2.18',
    license='MIT License',
    description='A collection of useful utilities by Laz aka Zanzes',
    url='',
    entry_points={
        'console_scripts': [
            'lztools    = cli.lztools:main',
            '¤          = cli.lztools:main',
            'parse-work = cli.utils:parse_work',
            'log-work   = cli.utils:log_work',
            'alarm      = cli.utils:alarm',
            'lzenv      = cli.lzenv:run',
            'pytools    = cli.pytools:main',

        ],
    },
    install_requires=[
        'flickrapi',
        'zope.proxy',
        'click',
        'pip',
        'ansiwrap',
        'prompt_toolkit', 'PyQt5'
    ],
    packages=[
        'cli',
        'core',
        'linux',
        'pytools',
        'text_tools',
        'third',
        'types',
        'utils',
        'web'
    ],
    zip_safe=False,
    include_package_data=True,
    package_data={},
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
)

