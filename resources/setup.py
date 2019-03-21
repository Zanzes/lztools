#!/usr/bin/env python3.7

from setuptools import setup

setup(
    name='lztools.resources',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.0.15',
    license='MIT License',
    description='Template',
    url='',
    entry_points={
        'console_scripts': [
        ],
    },
    install_requires=[],
    packages=['resources'],
    zip_safe=False,
    include_package_data=True,
    package_data={'lztools': ['resources/*']},
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

