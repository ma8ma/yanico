"""Unittest of command entry point."""
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

import unittest
import unittest.mock as mock

import yanico
import yanico.command


class TestCreateMainParser(unittest.TestCase):
    """yanico.command.create_main_parser() test."""

    def test_version(self):
        """Parse '--version' option."""
        parser = yanico.command.create_main_parser()
        with mock.patch.object(parser, '_print_message') as print_message:
            self.assertRaises(SystemExit, parser.parse_args, ['--version'])
        print_message.assert_called_once_with('yanico version ' +
                                              yanico.__version__ + '\n',
                                              mock.ANY)
