#!/usr/bin/env python3.7
import codecs

from setuptools import setup

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)


setup(
    name='web',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='0.0.1',
    license='MIT License',
    description='A collection of useful utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙',
    url='',
    requires=["lztools"],
    entry_points={
        'console_scripts': [
            'lweb = cli.lweb:main',
        ],
    },
    packages=['web', 'cli', 'resources'],
    zip_safe=False,
    include_package_data=True,
    package_data={'web': ['resources/*']},
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
