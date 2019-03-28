#!/usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='lztools.lzenv',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='0.0.1',
    license='MIT License',
    description='A collection of useful utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙',
    packages=find_packages(),
    py_modules=['lzenv_cli', 'main_layout', 'lzenv'],
    install_requires=['prompt_toolkit', 'click'],
    entry_points={
        'console_scripts': [
            'lzenv = lzenv_cli:start'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ]
)