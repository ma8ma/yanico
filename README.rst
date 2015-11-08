yanico
======
Yet Another Niconico-douga Command-line Interface


Description
-----------
**yanico** は `Apache 2.0`_ ライセンスで公開されている
`ニコニコ動画`_ にアクセスするためのCUIコマンドです。
メインコマンド **yan** (*yanico* の先頭3文字)に続けて
サブコマンドを指定することで機能を実行します。(実装中)
**機能を集めることができる** CUIコマンドを目標にゆっくり開発していきます。
パッケージに含むREADME等のドキュメントは日本語で先に書いていきます。

.. _`ニコニコ動画`: http://www.nicovideo.jp/
.. _`Apache 2.0`: http://www.apache.org/licenses/LICENSE-2.0

Feature
-------
* **yan** コマンドの体系は git や mercurial のようなサブコマンドの集合です。
* ログインのセッション情報などはブラウザから取得します。(最初はFirefoxを予定)

  * コマンドからログインする機能は今のところ未定です。

* Python と setuptools の知識が必要ですが、
  ユーザーが **独自にコマンドを追加** することができます。(予定)


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
現在は準備中でまだインストールできません。

PYPI のリリース版をインストールする::

    $ pip install yanico

リポジトリの最新版をインストールする::

    $ pip install git+https://github.com/ma8ma/yanico


Usage
-----
入力例::

    $ yan subcommand arg1 arg2


TODO
----
* メインコマンド **yan** を実装しインストール可能にする (v0.1.0a1)
* PYPI_ に登録して公開する (v0.1.0a1)
* 利用するブラウザを紐付けする **attach** コマンドを追加 (v0.1.0a2)
* ブラウザの紐付けを解除する **detach** コマンドを追加 (v0.1.0a3)
* Firefoxからセッション情報を取り出す機能を実装 (v0.1.0a4)
* 動画の情報を表示する **getflv** コマンドを追加 (v0.1.0)
* コマンドを追加する方法のドキュメントを書く (v1.0.0までには書く)

.. _PYPI: https://pypi.python.org/pypi/


Copyright 2015 Masayuki Yamamoto