# -*- coding: utf-8 -*-
##########
###Mecabesplesso.py
###作成者：青柳詠美
###作成：2021/1月
###version 0.1
##作成環境：MacOS 10.14.6, Python:3.6.8
###動作環境：MacOS 10.14.6,Python:3.5
############

#単語からMecab-unidicを作成(2021/1/22現在最新のunidicを想定)
import subprocess

"""
mecab -Overbose sentence.txt -o split.txt
"""

def sentence(word):
    with open("Mecabespresso/sentence.txt","w",encoding = "UTF-8") as f:
        f.write(word)
        f.write("\n")
    #print(word)
    subprocess.run("mecab -d unidic-cwj-2.3-2.0/ -Overbose Mecabespresso/sentence.txt -o Mecabespresso/split.txt",shell=True)
    

#sentence("鍵盤楽器")

#unidicからアクセントに関わる情報を抽出する
"""
魚
surface:魚	pos1:名詞	pos2:普通名詞	pos3:一般	pos4:	cType:	cForm:	lForm:サカナ	lemma:魚	orth:魚	pron:サカナ	orthBase:魚	pronBase:サカナ	goshu:和	iType:サ濁	iForm:基本形	fType:	fForm:	iConType:	fConType:	lType:体	kana:サカナ	kanaBase:サカナform:サカナ	formBase:サカナ	aType:0	aConType:C2	aModType:	lid:3824110132142592	lemma_id:13912
EOS
"""

"""
Macabでの使用例
mecab -Overbose sentence.txt -o test9.txt
"""
def nonum():
    return 0
def nowantword():
    t = ""
    return t
def noword():
    t = "*"
    return t
#抽出する部分=================================
def surface(target):
    if len(target.split("\t")) < 1:
        target = noword()
    else:
        target = target.split("\t")[0][8:]
    return target
def pos1(target):
    if len(target.split("\t")) < 2:
        target = nowantword()
    else:
        target = target.split("\t")[1][5:]
    return target
def pos2(target):
    if len(target.split("\t")) < 3:
        target = nowantword()
    else:
        target = target.split("\t")[2][5:]
    return target
def pos3(target):
    if len(target.split("\t")) < 4:
        target = noawantword()
    else:
        target = target.split("\t")[3][5:]
    return target
def pos4(target):
    if len(target.split("\t")) < 5:
        target = noword()
    else:
        target = target.split("\t")[4][5:]
    return target
def cType(target):
    if len(target.split("\t")) < 6:
        target = noword()
    else:
        target = target.split("\t")[5][6:]
    return target
def cForm(target):
    if len(target.split("\t")) < 7:
        target = nowantword()
    else:
        target = target.split("\t")[6][6:]
    return target
def lForm(target):
    if len(target.split("\t")) < 8:
        target = nowantword()
    else:
        target = target.split("\t")[7][6:]
    return target
def lemma(target):
    if len(target.split("\t")) < 9:
        target = noword()
    else:
        target = target.split("\t")[8][6:]
    return target
def orth(target):
    if len(target.split("\t")) < 10:
        target = noword()
    else:
        target = target.split("\t")[9][5:]
    return target
def pron(target):
    if len(target.split("\t")) < 11:
        target = noword()
    else:
        target = target.split("\t")[10][5:]
    return target
def orthBase(target):
    if len(target.split("\t")) < 12:
        target = noword()
    else:
        target = target.split("\t")[11][9:]
    return target
def pronBase(target):
    if len(target.split("\t")) < 13:
        target = noword()
    else:
        target = target.split("\t")[12][9:]
    return target
def goshu(target):
    if len(target.split("\t")) < 14:
        target = noword()
    else:
        target = target.split("\t")[13][6:]
    return target
def iType(target):
    if len(target.split("\t")) < 15:
        target = nowantword()
    else:
        target = target.split("\t")[14][6:]
    return target
def iForm(target):
    if len(target.split("\t")) < 16:
        target = nowantword()
    else:
        target = target.split("\t")[15][6:]
    return target
def fType(target):
    if len(target.split("\t")) < 17:
        target = nowantword()
    else:
        target = target.split("\t")[16][6:]
    return target
def fForm(target):
    if len(target.split("\t")) < 18:
        target = nowantword()
    else:
        target = target.split("\t")[17][6:]
    return target
def iConType(target):
    if len(target.split("\t")) < 19:
        target = nowantword()
    else:
        target = target.split("\t")[18][9:]
    return target
def fConType(target):
    if len(target.split("\t")) < 20:
        target = nowantword()
    else:
        target = target.split("\t")[19][9:]
    return target
def lType(target):
    if len(target.split("\t")) < 21:
        target = nowantword()
    else:
        target = target.split("\t")[20][6:]
    return target
def kana(target):
    if len(target.split("\t")) < 22:
        target = noword()
    else:
        target = target.split("\t")[21][5:]
    return target
def kanaBase(target):
    if len(target.split("\t")) < 23:
        target = noword()
    else:
        target = target.split("\t")[22][9:]
    return target
def form(target):
    if len(target.split("\t")) < 24:
        target = noword()
    else:
        target = target.split("\t")[23][5:]
    return target
def formBase(target):
    if len(target.split("\t")) < 25:
        target = noword()
    else:
        target = target.split("\t")[24][9:]
    return target
def aType(target):
    if len(target.split("\t")) < 26:
        target = nonum()
    else:
        target = target.split("\t")[25][6:]
    return target
def aConType(target):
    if len(target.split("\t")) < 27:
        target = nowantword()
    else:
        target = target.split("\t")[26][9:]
    return target
def aModType(target):
    if len(target.split("\t")) < 28:
        target = nowantword()
    else:
        target = target.split("\t")[27][9:]
    return target
def lid(target):
    if len(target.split("\t")) < 29:
        target = noword()
    else:
        target = target.split("\t")[28][4:]
    return target
def lemma_id(target):
    if len(target.split("\t")) < 30:
        target = noword()
    else:
        target = target.split("\t")[29][9:]
    return target

#複数出てきたときの対処法など=====================================
#アクセント核やaConTypeなどに
def acseiri(acnum):
    if acnum == "":
        acnum = 0
    elif acnum == 0:
        pass
    elif len(acnum.split(",")) != 1:
        acnum = acnum.split(",")[0]
    return acnum

#モーラ数を数える==============================================
def mora(pho):
    mora = 0
    for n in range(len(pho)):
        if pho[n] not in ["ァ","ィ","ゥ","ェ","ォ","ャ","ュ","ョ"]:
            mora = mora+1
    return mora

if __name__ == "__main__":
    main()

