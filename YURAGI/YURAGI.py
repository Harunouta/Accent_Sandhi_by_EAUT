# -*- coding: utf-8 -*-
#元文献:NHK日本語発音アクセント新辞典_

#揺らぎとは？議論にするのは下がり目の回避
"""
TASETでは長音[ー]促音[っ]撥音[ン]でアクセント核を-1

NHK新アの規約では以下の通り
A.長音、撥音は原則回避
B.二重母音aiの[イ]が下がり目回避の傾向がある。
C.無声化拍は回避されることもある。
(促音について下がり目の話が出てこない。上がり目の見えづらさは載っているものの)
(旧版も促音は載っていない)
でもどう考えても促音は絶対回避

本スクリプトは上記AとBを採用
"""
#モーラを格納する==============================================
def morabox(pho):
    box = []
    pi = pho[0]
    for n in range(len(pho)-1):
        if pho[n + 1] not in ["ァ","ィ","ゥ","ェ","ォ","ャ","ュ","ョ"]:
            box.append(pi)
            pi = pho[n+1]
        else:
            pi = pi + pho[n+1]
    box.append(pi)
    return box


#揺らぎを実装する===============================================
def wave(mora,target):
    if target != 0:
        #A
        if mora[target-1] in ["ー","ッ","ン"]:
            target = target - 1
        #B
        if len(mora) > 1:
            if mora[target-1] in ["イ"] and mora[target-2][-1] in ["ア","カ","サ","タ","ナ","ハ","マ","ヤ","ラ","ワ","ガ","ザ","ダ","バ","パ","ャ","ァ"]:#B
                target = target-1
    return target


#test
#print(morabox("チョウチョウフジン"))

if __name__ == "__main__":
    main()

