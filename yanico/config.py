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
"""Handle yanico configuration."""

import configparser
import os.path


CONFIG_FILENAME = '.yanico.conf'


def user_path():
    """Return user configuration filepath.

    The filepath depends home directory and CONFIG_FILENAME constants.
    """
    return os.path.join(os.path.expanduser('~'), CONFIG_FILENAME)


def load(*filepaths):
    """Return configration object.

    Object parses home directory config file.

    Args:
        filepaths (Tuple[str]): configuration file paths

    Returns:
        ConfigParser: object expects some configurations are loaded.
    """
    parser = configparser.ConfigParser()
    parser.read((user_path(),) + filepaths)
    return parser
