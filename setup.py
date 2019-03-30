#!/usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='lztools',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.2.18',
    license='MIT License',
    url="",
    description='A collection of useful utilities by Laz aka Zanzes',
    packages=['lztools', 'lztools.linux', 'lztools.lztext'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'pip',
        'click'
    ],
    entry_points={
        # 'console_scripts': [
        #     '¤          = lztools:main',
        #     'parse-work = utils:parse_work',
        #     'log-work   = utils:log_work',
        #     'alarm      = utils:alarm',
        #
        # ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)

