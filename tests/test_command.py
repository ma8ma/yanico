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

import argparse
import unittest
from unittest import mock

import yanico
import yanico.command


class TestCreateMainParser(unittest.TestCase):
    """yanico.command.create_main_parser() test."""

    def test_version(self):
        """Parse '--version' option."""
        parser = yanico.command.create_main_parser()
        with mock.patch.object(parser, "_print_message") as print_message:
            self.assertRaises(SystemExit, parser.parse_args, ["--version"])
        print_message.assert_called_once_with(
            "yanico version " + yanico.__version__ + "\n", mock.ANY
        )

    def test_help_long(self):
        """Parse '--help' option."""
        parser = yanico.command.create_main_parser()
        with mock.patch.object(parser, "print_help") as print_help:
            self.assertRaises(SystemExit, parser.parse_args, ["--help"])
        print_help.assert_called_once_with()

    def test_help_short(self):
        """Parse '-h' option."""
        parser = yanico.command.create_main_parser()
        with mock.patch.object(parser, "print_help") as print_help:
            self.assertRaises(SystemExit, parser.parse_args, ["-h"])
        print_help.assert_called_once_with()

    @staticmethod
    def test_without_argments():
        """Expect 'run' method that showing help."""
        parser = yanico.command.create_main_parser()
        args = parser.parse_args([])
        with mock.patch.object(parser, "print_help") as print_help:
            args.run(args)
        print_help.assert_called_once_with()


class TestBuildSubparsers(unittest.TestCase):
    """yanico.command.build_subparsers() test."""

    @staticmethod
    def _init_stub_command():
        """Return entry point having stub command."""

        def run(args):
            """Command body."""
            return args.n * 2

        def register(command_name, subparsers):
            """Command registrant."""
            parser = subparsers.add_parser(command_name)
            parser.add_argument("n", type=int)
            parser.set_defaults(run=run)

        entry_point = mock.Mock()
        entry_point.name = "stub"
        entry_point.load.return_value = register
        return entry_point

    @mock.patch("yanico.command.entry_points")
    def test_stub_command(self, entry_points):
        """Register command returning two times numbers."""
        entry_points.return_value = [self._init_stub_command()]

        parser = argparse.ArgumentParser()
        yanico.command.build_subparsers(parser)
        args = parser.parse_args(["stub", "21"])
        self.assertEqual(args.run(args), 42)
        entry_points.assert_called_once_with(group="yanico.commands")

    @mock.patch("yanico.command.entry_points")
    def test_without_arguments(self, entry_points):
        """Expect 'run' method that showing help."""
        entry_points.return_value = [self._init_stub_command()]

        parser = yanico.command.create_main_parser()
        yanico.command.build_subparsers(parser)
        args = parser.parse_args([])
        with mock.patch.object(parser, "print_help") as print_help:
            args.run(args)
        print_help.assert_called_once_with()
        entry_points.assert_called_once_with(group="yanico.commands")


class TestMain(unittest.TestCase):
    """yanico.command.main() test."""

    @staticmethod
    def _init_stub_parser():
        """Return parser having command that returns integer."""
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers()
        stub_parser = subparsers.add_parser("stub")
        stub_parser.add_argument("n", type=int)
        stub_parser.set_defaults(run=lambda args: args.n)
        return parser

    @mock.patch("yanico.command.create_main_parser")
    @mock.patch("yanico.command.build_subparsers")
    @mock.patch("sys.argv", new=["", "stub", "3"])
    def test_return_value(self, _, create_main_parser):
        """Except main function returns specified integer."""
        create_main_parser.return_value = self._init_stub_parser()
        self.assertEqual(yanico.command.main(), 3)
