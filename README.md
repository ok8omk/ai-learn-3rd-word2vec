## AI勉強会第3回資料

### 参考URL

* 北海道大学HP
    * [URL](https://www.hokudai.ac.jp)
* 青空文庫 夏目漱石 - 夢十夜
    * [URL](http://www.aozora.gr.jp/cards/000148/card799.html)

### ファイル概要

* setup.sh
    * 今回用いるpythonの環境設定を行う
* install.sh
    * word2vec/wiki_sample.pyで用いるモデルをダウンロードする
    * 非常に時間がかかるので注意

#### crawler

* main.py
    * 北海道大学公式HPからロゴ画像をスクレイピングしlogo.pngとして保存する

#### mecab

* main.py
    * 入力した文章を形態素解析し出力する

#### word2vec

* wakati.py
    * resources/yume_juya_wakati.txtを生成する
    * resources/yume_juya.txtの形態素解析を行う
    * 単語数削減のため基本形に直して形態素解析を行う
* train.py
    * wakati.pyで生成したファイルを元にword2vecの学習を行う
    * 学習済みモデルをmodelsに保存する
    * ベクトルの次元数は25,50,75,100次元となっている
    * 学習設定はソースコード参照
* main.py
    * train.pyで生成された学習済みモデルを用いて形態素間の類似度を計算し、上位10件を表示する
    * 次元別の計算結果が出力される
* wiki_sample.py
    * install.shでダウンロードした、Wikipediaのダンプデータを用いて学習したモデルを用いて形態素間の類似度を計算する
    * install.shの実行には時間が掛かるので注意
