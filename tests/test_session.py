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
"""Unittest of handling for user session."""

import unittest
from unittest import mock

from yanico import session
from yanico.session import LoaderNotFoundError


class TestLoad(unittest.TestCase):
    """Test for yanico.session.load()."""

    @mock.patch("yanico.session.entry_points")
    def test_loader_exist(self, entry_points):
        """Expect to the load function returns user session."""
        entry = mock.Mock()
        loader = entry.load.return_value = mock.Mock(return_value="value")
        entry_points.return_value = [entry]

        ltype = "firefox"
        profile = "/path/to/profile"
        self.assertEqual(session.load(ltype, profile), "value")

        entry_points.assert_called_once_with(group="yanico.sessions", name=ltype)
        entry.load.assert_called_once_with()
        loader.assert_called_once_with(profile)

    @mock.patch("yanico.session.entry_points")
    def test_loader_not_exist(self, entry_points):
        """Expect to raise exception when the loader does not exist."""
        eps = entry_points.return_value
        eps.return_value = []

        ltype = "loader is not found"
        profile = "dummy"
        self.assertRaises(LoaderNotFoundError, session.load, ltype, profile)

        entry_points.assert_called_once_with(group="yanico.sessions", name=ltype)

    @mock.patch("yanico.session.entry_points")
    def test_loader_error(self, entry_points):
        """Expect to through error when the loader raises any error."""

        class _AnyError(Exception):
            pass

        entry = mock.Mock()
        loader = entry.load.return_value = mock.Mock(side_effect=_AnyError)
        entry_points.return_value = [entry]

        ltype = "loader is found"
        profile = "a profile"
        self.assertRaises(_AnyError, session.load, ltype, profile)

        entry_points.assert_called_once_with(group="yanico.sessions", name=ltype)
        entry.load.assert_called_once_with()
        loader.assert_called_once_with(profile)


class TestLoadFromConfig(unittest.TestCase):
    """Test for yanico.session.load_from_config()."""

    @mock.patch("yanico.session.load")
    def test_min_config(self, load_func):
        """Expect to return string using minimum configuration."""
        load_func.return_value = "value"

        min_config = {"session": {"type": "foobar", "profile": "/path/to/profile"}}
        self.assertEqual(session.load_from_config(min_config), "value")

        load_func.assert_called_once_with("foobar", "/path/to/profile")

    def test_without_session(self):
        """Expect to raise KeyError if the config without session."""
        without_session = {"type": "foobar", "profile": "/path/to/profile"}
        self.assertRaises(KeyError, session.load_from_config, without_session)

    def test_without_type(self):
        """Expect to raise KeyError if the config without type."""
        without_type = {"session": {"profile": "/path/to/profile"}}
        self.assertRaises(KeyError, session.load_from_config, without_type)

    def test_without_profile(self):
        """Expect to raise KeyError if the config without profile."""
        without_profile = {"session": {"type": "foobar"}}
        self.assertRaises(KeyError, session.load_from_config, without_profile)
