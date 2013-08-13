#!/usr/bin/env python3
import sys
from distutils.core import setup


PY3 = sys.version_info[0] >= 3
VERSION_FILE = "pifacecad_emulator/version.py"


def get_version():
    if PY3:
        version_vars = {}
        with open(VERSION_FILE) as f:
            code = compile(f.read(), VERSION_FILE, 'exec')
            exec(code, None, version_vars)
        return version_vars['__version__']
    else:
        execfile(VERSION_FILE)
        return __version__


setup(
    name='pifacecad_emulator',
    version=get_version(),
    description='The PiFace Control and Display Emulator.',
    author='Thomas Preston',
    author_email='thomas.preston@openlx.org.uk',
    license='GPLv3+',
    url='https://github.com/piface/pifacecad_emulator',
    packages=['pifacecad_emulator'],
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or "
        "later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords='piface digital emulator raspberrypi openlx',
    scripts=['bin/pifacecad-emulator'],
)
