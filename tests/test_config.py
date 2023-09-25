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
"""Unittest of configuration loading."""

import os
import unittest
from unittest import mock

from yanico import config


class TestUserPath(unittest.TestCase):
    """Test for yanico.config.user_path()."""

    @mock.patch.dict(os.environ, {"HOME": "spam"})
    def test_path(self):
        """Expect filepath joinning '.yanico.conf' under $HOME."""
        expect = None
        if os.sep == "\\":
            expect = "spam\\.yanico.conf"
        elif os.sep == "/":
            expect = "spam/.yanico.conf"
        result = config.user_path()
        self.assertEqual(result, expect)

    @mock.patch("yanico.config.CONFIG_FILENAME", new="ham.egg")
    def test_dependence_constants(self):
        """Expect to depend filename by 'CONFIG_FILENAME' constants."""
        result = config.user_path()
        self.assertEqual(os.path.basename(result), "ham.egg")


class TestLoad(unittest.TestCase):
    """Test for yanico.config.load()."""

    @mock.patch("configparser.ConfigParser")
    def test_without_args(self, parserclass):
        """Expect config object that tried to parse user config file."""
        mock_conf = parserclass.return_value
        result = config.load()
        self.assertIs(result, mock_conf)
        mock_conf.read.assert_called_once_with((config.user_path(),))

    @mock.patch("configparser.ConfigParser")
    def test_with_args(self, parserclass):
        """Expect arguments pass to the parser after user config file."""
        mock_conf = parserclass.return_value
        result = config.load("spam", "ham", "eggs")
        self.assertIs(result, mock_conf)
        mock_conf.read.assert_called_once_with(
            (config.user_path(), "spam", "ham", "eggs")
        )
