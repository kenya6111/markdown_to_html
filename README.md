# File-manipulator

## 🌱概要
markdownからhtmlファイルへ変換するアプリケーション

## ✨デモ


## 📝説明
コマンドラインから指定したmdファイルをhtml形式のファイルに変換します。
以下、入力コマンド例です。
 - python3 markdown_to_html.py markdown <inputpath>.txt <outputpath>.html
 
## 🧰前提条件

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```


### pip
pipは、Python用のパッケージマネージャで、パッケージのインストールと管理を行うことができます。

[pipのインストールガイド](https://pip.pypa.io/en/stable/installation/)に従って、pipをインストールしてください。

aptを使用してpipをインストールする場合は、下記手順でインストールしてください。

1. pipがインストールされているか確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示された場合は、pipがインストールされています。<br>以降の手順はスキップしてください。
```
pip3 --version
```

2. システムを更新する
```
sudo apt-get update
```

3. pipをインストールする
```
sudo apt install python3-pip
```

4. pipがインストールされたことを確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示されていれば、pipのインストールは完了です!
```
pip3 --version
```
## 🙋使用例
一通りの手順のイメージは[デモ](#デモ)を参考にしてください。

## 💾使用技術
<table>
<tr>
  <th>カテゴリ</th>
  <th>技術スタック</th>
</tr>
<tr>
  <td>開発言語</td>
  <td>Python</td>
</tr>
<tr>
  <td rowspan=2>インフラ</td>
  <td>Ubuntu</td>
</tr>
<tr>
  <td>VirtualBox</td>
</tr>
<tr>
  <td rowspan=2>その他</td>
  <td>Git</td>
</tr>
<tr>
  <td>Github</td>
</tr>
</table>

## 📜作成の経緯
⭐️後で記載する!!!

作成した理由を記載する。

## ⭐️こだわった点
 - 各ファイル操作を関数化し、再利用性を向上
 - with句を用いてファイルを安全に閉じるようにした
 - main関数内でコマンド引数の数をチェックし、必要な引数が不足している場合には適切なエラーメッセージを表示してプログラムの実行を停止
 - コマンド引数の処理をmain関数でまとめ、使いやすくしました。
テキストや参考にした記事などを再度読み返して技術の理解を深めてから書く。

ここがエンジニアに一番読んでもらいたい箇所なのでできるだけ詳細に書く。



## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)
- [コマンドライン引数の受取](https://qiita.com/taashi/items/07bf75201a074e208ae5)
- [ファイルの作成削除](https://www.javadrive.jp/python/file/index9.html)
- [ファイルの中身削除](https://teratail.com/questions/263025)
- [with句について](https://djangobrothers.com/blogs/with_statement_basic/#google_vignette)
