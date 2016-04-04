yanico
======

.. image:: https://img.shields.io/pypi/v/yanico.svg
    :target: https://pypi.python.org/pypi/yanico/
.. image:: https://img.shields.io/pypi/pyversions/yanico.svg
    :target: https://pypi.python.org/pypi/yanico/
.. image:: https://travis-ci.org/ma8ma/yanico.svg
    :target: https://travis-ci.org/ma8ma/yanico

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
* Python_ (バージョン3以降)
* pip_
* setuptools_
* サードパーティ製のHTTPライブラリ(予定)

.. _Python: https://www.python.org/
.. _pip: https://pip.pypa.io/
.. _setuptools: http://pythonhosted.org/setuptools/


Install
-------
PYPI_ のリリース版をインストールする::

    $ pip install yanico

`リポジトリ`_ の最新版をインストールする::

    $ pip install git+https://github.com/ma8ma/yanico

.. _PYPI: https://pypi.python.org/pypi/yanico/
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


What's New
----------

**v0.1.0a3 (2016-04-05)**

* ローダータイプとプロファイルからセッション情報を読み込む機能を追加しました。
* 設定解析オブジェクトからセッション情報を読み込む機能を追加しました。
* ユーザーが用意した設定ファイルを読み込む機能を追加しました。


**v0.1.0a2 (2016-02-06)**

* ソースパッケージにドキュメントを追加しました。
* Firefoxのプロファイルからニコニコのセッション情報をロードする機能を追加しました。


以前のバージョンでの変更は `CHANGES.ja.md`_ を見てください。

.. _`CHANGES.ja.md`: https://github.com/ma8ma/yanico/blob/master/CHANGES.ja.md


TODO
----
* 動画の情報を表示する **getflv** コマンドを追加 (v0.1.0)
* コマンドを追加する方法のドキュメントを書く (v1.0.0までには書く)


Copyright 2015-2016 Masayuki Yamamoto
