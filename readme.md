"""
現行、Mecab(-Overboseできるもの)(https://taku910.github.io/mecab/)、
CRF++(https://taku910.github.io/crfpp/)のpathが通っていることが動作条件です。

また、Mecab辞書としてunidic-cwj-2.3-2.0(https://unidic.ninjal.ac.jp/download#unidic_bccwj)を
使用します。このreadmeと同じディレクトリに(unidic-cwj-2.3-2.0)という名前で置いて下さい。
(システム辞書のデフォルトに設定する必要はありません。)

Mecabespresso/Mecabespresso.py でMecabのコマンドを、
CRFsyori/CRFsyori.py および CRFsyori2/CRFsyori2.py でCRF++のコマンドを呼び出しています。
コマンドラインの返却値を利用するので、pythonでのコマンドライン結果を取得できるpython環境でご利用ください。
(pyenvで指定されている場合は該当ディレクトリで設定されているpythonのパスと同じものを使用してください。)

"""
ターミナルで
do.pyでCUI版を
GUI.pyでGUI版を実行できます。

本研究は、
第83回情報処理学会全国大会(https://www.gakkai-web.net/gakkai/ipsj/83/program83.html#t4)
学生セッション［7N会場］（3月20日（土）　13:10〜15:10）
音声言語情報処理（2）
7N-02
アクセント単位形の推測を用いた日本語複合名詞のアクセント句の合成
○青柳詠美，小島正樹（東京薬科大）
で発表いたします。

===========================
東京薬科大学　生命科学研究科　生物情報科学研究室
青柳　詠美
s168002@icloud.com
utaharunomar17@gmail.com
==========================