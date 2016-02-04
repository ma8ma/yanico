"""Handle Firefox session."""
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

import os.path
import sqlite3


def load(profile):
    """Return the nicovideo.jp user_session string.

    Arguments:
    profile : str -- path for Firefox profile direcotry

    Returns: str
    """
    conn = sqlite3.connect(os.path.join(profile, 'cookies.sqlite'))
    cur = conn.execute(
        "SELECT value FROM moz_cookies "
        "WHERE name = 'user_session' AND host = '.nicovideo.jp'")
    return cur.fetchone()[0]
