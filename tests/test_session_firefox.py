"""Unittest of firefox session."""

#  Copyright (C) 2015-2025 Masayuki Yamamoto
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

import os.path
import sqlite3
import unittest
from importlib.metadata import entry_points
from unittest import mock

from yanico.session import firefox
from yanico.session import UserSessionNotFoundError


def _stub_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE moz_cookies (name, host, value)")
    return conn


class TestLoad(unittest.TestCase):
    """Test for yanico.session.firefox.load()."""

    def test_exist(self):
        """Expect user_session string."""
        conn = _stub_db()
        conn.execute(
            "INSERT INTO moz_cookies VALUES"
            "('user_session', '.nicovideo.jp', 'dummy_user_session')"
        )
        with mock.patch("sqlite3.connect") as mock_connect:
            mock_connect.return_value = conn
            ses = firefox.load("/path/to/profile")
        expect_path = os.path.join("/path/to/profile", "cookies.sqlite")
        mock_connect.assert_called_once_with(expect_path)
        self.assertEqual("dummy_user_session", ses)

    def test_not_exist(self):
        """If not exist user_session, raise Error."""
        conn = _stub_db()
        with mock.patch("sqlite3.connect") as mock_connect:
            mock_connect.return_value = conn
            self.assertRaises(
                UserSessionNotFoundError, firefox.load, "/path/to/profile"
            )
        expect_path = os.path.join("/path/to/profile", "cookies.sqlite")
        mock_connect.assert_called_once_with(expect_path)

    def test_not_directory(self):
        """If profile is not directory path, raise Error."""
        self.assertRaises(FileNotFoundError, firefox.load, "/NOT-DIRECTORY")

    def test_empty_string(self):
        """If profile is empty string, raise Error."""
        self.assertRaises(FileNotFoundError, firefox.load, "")


class TestEntryPoint(unittest.TestCase):
    """Test for `yanico.sessions` entry point."""

    def test_load_func(self):
        """Check whether loaeded function is firefox.load()."""
        (entry,) = entry_points(group="yanico.sessions", name="firefox")
        func = entry.load()
        self.assertIs(firefox.load, func)
