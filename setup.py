#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from unolog/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("unolog", "__init__.py")

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

setup(
    name='Unolog',
    version=version,
    description="""Un NOuveau LOgiciel de Gestion de patient """,
    author='Jimmy Girardet',
    author_email='ijkl@netc.fr',
    url='https://github.com/jgirardet/unolog',
    packages=[
        'unolog',
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='unolog',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python :: 3.5',
    ],
)
