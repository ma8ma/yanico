"""Unittest of __token__ session."""

#  Copyright (C) 2024-2025 Masayuki Yamamoto
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
from importlib.metadata import entry_points

from yanico.session import token
from yanico.session import UserSessionNotFoundError


class TestLoad(unittest.TestCase):
    """Test for yanico.session.token.load()."""

    def test_exist(self):
        """Expect user_session string."""
        ses = token.load("user_session_hogefugamoge")
        self.assertEqual("user_session_hogefugamoge", ses)

    def test_not_exist(self):
        """If not exist user_session, raise Error."""
        self.assertRaises(UserSessionNotFoundError, token.load, "")


class TestEntryPoint(unittest.TestCase):
    """Test for `yanico.sessions` entry point."""

    def test_load_func(self):
        """Check whether loaeded function is firefox.load()."""
        (entry,) = entry_points(group="yanico.sessions", name="__token__")
        func = entry.load()
        self.assertIs(token.load, func)
