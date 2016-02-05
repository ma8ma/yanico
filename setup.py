"""Setup script."""
#  Copyright 2015-2016 Masayuki Yamamoto
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import find_packages
from setuptools import setup

from yanico import __version__


with open('README.rst', 'r', encoding='utf-8') as file:
    README = file.read()

setup(
    name='yanico',
    version=__version__,
    author='Masayuki Yamamoto',
    author_email='ma3yuki.8mamo10@gmail.com',
    description='Yet Another Niconico-douga Command-line Interface',
    long_description=README,
    license='Apache 2.0',
    keywords='cli comment niconico video',
    url='https://github.com/ma8ma/yanico',
    packages=find_packages(exclude=['tests']),
    package_data={
        '': ['CHANGES.ja.md', 'LICENSE'],
    },
    test_suite='tests',
    install_requires=[],
    extras_require={
        'develop': ['hacking', 'flake8-docstrings', 'pep8-naming'],
    },
    entry_points={
        'console_scripts': ['yan = yanico.command.__init__:main'],
        'yanico.sessions': [
            'firefox = yanico.session.firefox:load',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Session',
    ],
)
