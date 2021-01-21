# -*- coding: utf-8 -*-

from Mecabespresso import Mecabespresso
from SAGISAKA import SAGISAKA
from MIYAZAKI import MIYAZAKI
from YURAGI import YURAGI
from CRFsyori import CRFsyori


def acmake(word,strong):
    #mecabの結果から実際に抽出する
    with open ("Mecabespresso/split.txt","r",encoding = "UTF-8") as f:
        line = f.readlines()

    SUW = []
    pho = []
    
    for n in range(len(line)):
        if line[n] != "EOS\n":
            SUW.append(Mecabespresso.surface(line[n]))
            pho.append(Mecabespresso.pron(line[n]))

    #CRFの結果を取ってくる
    CRFS = CRFsyori.CRFbox(SUW,pho)
        
    #print("strongs:"+str(strong))
    #print("CRF:"+str(CRFS))

    #アクセント句の推定
    ku = []
    for n in range(len(CRFS)):
        if CRFS[n] == "1" and strong[n] == "1":
            ku.append(1)
        else:
            ku.append(0)
    #print("accent:"+str(ku))


    #アクセント合成==================================
    zenbu = int(Mecabespresso.acseiri(Mecabespresso.aType(line[0])))
    propho = Mecabespresso.pron(line[0])
    suw = Mecabespresso.surface(line[0])

    #M優先
    acbox = []
    readbox = []
    suwbox = []
    if Mecabespresso.aModType(line[0]) != "":
        zenbu = SAGISAKA.M(Mecabespresso.mora(propho),zenbu,Mecabespresso.aModType(line[0]))
    for n in range(len(line)-1):#bi-gram
        if "EOS" in line[n+1]:#終了
            #print(Mecabespresso.surface(line[n]))
            #print(Mecabespresso.surface(line[n+1]))
            #print(zenbu)
            #print("===================================")
            #print(SUW)
            #print(pho)
            acbox.append(zenbu)
            #print(acbox)
            readbox.append(propho)
            #print(readbox)
            suwbox.append(suw)
            #print(suwbox)

            return [acbox,readbox,suwbox]

        #先頭アクセントが独立のとき
        elif n == 0 and ku[n] == 1:
            zenbu = int(Mecabespresso.acseiri(Mecabespresso.aType(line[n])))
            if len(YURAGI.morabox(propho)) > 1 and zenbu == 0:
                zenbu = len(YURAGI.morabox(propho))

            #独立句のアクセント核が0のとき 
            if len(YURAGI.morabox(propho)) > 1:
                zenbu = YURAGI.wave(YURAGI.morabox(propho),zenbu)

            #独立アクセント句を書き出す    
            acbox.append(zenbu)
            zenbu = int(Mecabespresso.acseiri(Mecabespresso.aType(line[n+1])))
            propho = Mecabespresso.pron(line[n+1])
            suw = Mecabespresso.surface(line[n+1])
            readbox.append(Mecabespresso.pron(line[n]))
            suwbox.append(Mecabespresso.surface(line[n]))
            
        #独立後のアクセント   
        elif ku[n] == 1:
            acbox.append(zenbu)
            readbox.append(propho)
            suwbox.append(suw)
            zenbu = int(Mecabespresso.acseiri(Mecabespresso.aType(line[n+1])))
            propho = Mecabespresso.pron(line[n+1])
            suw = Mecabespresso.surface(line[n+1])

        else:
            #アクセント句の抽出
            m1 = zenbu
            m2 = Mecabespresso.acseiri(Mecabespresso.aType(line[n+1]))

            #M優先
            if Mecabespresso.aModType(line[n+1]) != "":
                m2 = SAGISAKA.M(Mecabespresso.mora(Mecabespresso.pron(line[n+1])),int(Mecabespresso.acseiri(Mecabespresso.aType(line[n+1]))),Mecabespresso.aModType(line[n+1]))

            #数詞結合法則
            suu = ""
            suu = MIYAZAKI.MIYAZAKI(Mecabespresso.mora(propho),Mecabespresso.mora(Mecabespresso.pron(line[n+1])),Mecabespresso.orth(line[n+1]),Mecabespresso.orth(line[n]),Mecabespresso.iConType(line[n]))

            #アクセント結合(数詞結合法則で載っていなかったら)
            #MIYAZAKI.pyに該当部分がなかったらSAGISAKA.py
            if suu == "":
                #接頭辞
                if "P" in Mecabespresso.aConType(line[n]):
                    zenbu = SAGISAKA.P(Mecabespresso.mora(propho),Mecabespresso.mora(Mecabespresso.pron(line[n+1])),zenbu,int(Mecabespresso.acseiri(Mecabespresso.aType(line[n+1]))),Mecabespresso.aConType(line[n]))

                elif "C" in Mecabespresso.aConType(line[n+1]):
                    zenbu = SAGISAKA.C(Mecabespresso.mora(propho),zenbu,int(Mecabespresso.acseiri(Mecabespresso.aType(line[n+1]))),Mecabespresso.aConType(line[n+1]))
 
                elif Mecabespresso.pos1(line[n+1]) in Mecabespresso.aConType(line[n+1]):#該当品詞が無かったらN
                    zenbu = SAGISAKA.F(Mecabespresso.mora(propho),zenbu,Mecabespresso.aConType(line[n+1]),Mecabespresso.pos1(line[n+1]))
                else:
                    zenbu = SAGISAKA.N(Mecabespresso.mora(propho),Mecabespresso.mora(Mecabespresso.pron(line[n+1])),zenbu,int(Mecabespresso.acseiri(Mecabespresso.aType(line[n+1]))))
            else:
                zenbu = suu
            #print(suu)
            #print(propho)
                
            propho = propho + Mecabespresso.pron(line[n+1])
            suw = suw + Mecabespresso.surface(line[n+1])
            zenbu = YURAGI.wave(YURAGI.morabox(propho),zenbu)

            #print(Mecabespeesso.surface(line[n+1]))
            #print(zenbu)
            
if __name__ == "__main__":
    main()
