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
"""Handle nicovideo.jp user_session."""

from importlib.metadata import entry_points


class LoaderNotFoundError(Exception):
    """Session loader is not found."""


class UserSessionNotFoundError(Exception):
    """Profile exists, but user_session is not found."""


def load(ltype, profile):
    """Return nicovideo.jp user session string.

    Args:
        ltype (str): loader type
        profile (str): file path for profile

    Returns:
        str: user session

    Raises:
        LoaderNotFoundError
        Error from loader
    """
    eps = entry_points(group="yanico.sessions", name=ltype)
    for entry in eps:
        load_func = entry.load()
        return load_func(profile)
    raise LoaderNotFoundError(f"{ltype} loader is not found.")


def load_from_config(conf):
    """Return nicovideo.jp user session string.

    Args:
        conf (ConfigMap): configuration of the user session loading
                          ConfigMap = Mapping[str, Mapping[str, str]]

    Returns:
        str: user session

    Raises:
        KeyError
        Error from load()
    """
    session = conf["session"]
    return load(session["type"], session["profile"])
