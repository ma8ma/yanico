"""Command entry point."""
#  Copyright 2015 Masayuki Yamamoto
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

import argparse
import pkg_resources

import yanico


def create_main_parser():
    """Return command argument parser."""
    parser = argparse.ArgumentParser(
        description=yanico.__description__,
        prog='yan',
    )
    parser.add_argument('--version', action='version',
                        version='yanico version ' + yanico.__version__)
    parser.set_defaults(run=lambda _: parser.print_help())
    return parser


def build_subparsers(parser):
    """Register command from setuptools plugins."""
    # pylint: disable=no-member
    subparsers = parser.add_subparsers(title='Commands')
    for entry in pkg_resources.iter_entry_points('yanico.commands'):
        register = entry.load()
        register(entry.name, subparsers)


def main():
    """Command entry point."""
    parser = create_main_parser()
    build_subparsers(parser)
    args = parser.parse_args()
    return args.run(args)
