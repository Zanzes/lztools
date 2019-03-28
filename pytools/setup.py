#!/usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='lztools.pytools',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='0.0.1',
    license='MIT License',
    description='A collection of useful utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙',
    requires=['click', 'pip'],
    install_requires=[],
    py_modules=[
        'pytools_cli',
        'class_tools',
        'mod_tools',
        'obj_tools',
        'pip_package',
        'utils'
    ],
    entry_points={
        'console_scripts': [
            'pytools = pytools_cli:main',
        ],
    },
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)

