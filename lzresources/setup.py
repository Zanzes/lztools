#!/usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='lzresources',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.0.15',
    license='MIT License',
    description='A collection of resources by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙',
    install_requires=[],
    py_modules=['resources'],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    package_data={'lzresources': ['lzresources/*']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)

