yanico
======

.. image:: https://img.shields.io/pypi/v/yanico.svg
    :target: https://pypi.python.org/pypi/yanico/
.. image:: https://img.shields.io/pypi/pyversions/yanico.svg
    :target: https://pypi.python.org/pypi/yanico/
.. image:: https://github.com/ma8ma/yanico/workflows/CI/badge.svg
    :target: https://github.com/ma8ma/yanico

Yet Another Niconico-douga Command-line Interface


Description
-----------
**yanico** は `Apache 2.0`_ ライセンスで公開されている
`ニコニコ動画`_ にアクセスするためのCUIコマンドです。
メインコマンド **yan** (*yanico* の先頭3文字)に続けて
サブコマンドを指定することで機能を実行します。
**機能を集めることができる** CUIコマンドを目標にゆっくり開発していきます。
パッケージに含むREADME等のドキュメントは日本語で先に書いていきます。

.. _`ニコニコ動画`: http://www.nicovideo.jp/
.. _`Apache 2.0`: http://www.apache.org/licenses/LICENSE-2.0


Feature
-------
* **yan** コマンドの体系は git や mercurial のようなサブコマンドの集合です。
* ログインのセッション情報などはブラウザから取得します。

  * Firefoxのセッション情報を取得します。
  * 他のブラウザへの対応は未定です。
  * コマンドからログインする機能は今のところ未定です。

* Python と setuptools の知識が必要ですが、
  ユーザーが **独自にコマンドを追加** することができます。


Requirement
-----------
* Python_ (バージョン3.10以降)
* pip_ (バージョン10以降)
* setuptools_ (バージョン 61.0.0 以降)
* setuptools_scm_
* サードパーティ製のHTTPライブラリ(予定)

.. _Python: https://www.python.org/
.. _pip: https://pip.pypa.io/
.. _setuptools: https://setuptools.pypa.io/
.. _setuptools_scm: https://pypi.org/project/setuptools-scm/


Install
-------
PYPI_ のリリース版をインストールする::

    $ pip install yanico

`リポジトリ`_ の最新版をインストールする::

    $ pip install git+https://github.com/ma8ma/yanico

.. _PYPI: https://pypi.org/project/yanico/
.. _`リポジトリ`: https://github.com/ma8ma/yanico


Usage
-----
* ホームディレクトリに設定ファイル ``.yanico.conf`` を置きます。
  ``[session]`` セクションに実行時に使用するセッション情報を読み込む
  **ブラウザのタイプ** ``type`` と **プロファイルのパス** ``profile``
  を設定してください。

設定例::

    $ cat <<EOF >~/.yanico.conf
    [session]
    type = firefox
    profile = /home/user/path/to/firefox/profile
    EOF

コマンド例::

    $ yan subcommand arg1 arg2


Development
-----------
開発に使う追加のツールをインストールする::

    $ pip install yanico[dev]


Testing
-------
テストを行うには pytest_ を実行する::

    $ pytest

コードカバレッジ( coverage_ )を計測して結果を表示する::

    $ coverage run -m pytest
    $ coverage report


Code check
----------
コードをチェックするには pylint_ を実行する::

    $ pylint setup.py tests/ yanico/


Type check
----------
型をチェックするには mypy_ を実行する::

    $ mypy yanico/


Code formatting
---------------
ソースコードを整形するには black_ を実行する::

    $ black .


What's New
----------

**v0.3.0 (2025-12-23)**

* Python 3.9のサポートを終了しました。


**v0.2.0 (2024-12-31)**

* Python 3.8のサポートを終了しました。
* `user_session` を直接指定するセッションタイプ `__token__` を追加しました。


以前のバージョンでの変更は `CHANGES.ja.md`_ を見てください。

.. _`CHANGES.ja.md`: https://github.com/ma8ma/yanico/blob/master/CHANGES.ja.md


TODO
----
* コマンドを追加する方法のドキュメントを書く (v1.0.0までには書く)


Copyright (C) 2015-2025 Masayuki Yamamoto


.. References

.. _coverage: https://coverage.readthedocs.io/
.. _pytest: https://docs.pytest.org/
.. _pylint: https://pypi.org/project/pylint/
.. _mypy: http://mypy-lang.org/
.. _black: https://github.com/psf/black
