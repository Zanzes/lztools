import codecs
import os

from setuptools import setup

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

orig = os.getcwd()
np = os.path.dirname(os.path.realpath(__file__))

os.chdir(np)
scripts = []
for x in os.listdir("Commands"):
    scripts.append("Commands/{}".format(x))

setup(
    name='PowerUtils',
    version='1.0.4',
    packages=['PowerUtils', 'PowerUtils.Managers'],
    scripts=scripts,
    url='',
    license='MIT License',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    description='A collection of useful utilities by Laz aka Zanzes',
    zip_safe=False,
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
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7'  # ,
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
os.chdir(orig)
