# -*- coding: utf-8 -*-
import acmakekisoku #数詞あり規則読みunidic
import acmakesurunidic
import acmakephounidic

from Mecabespresso import Mecabespresso


#強調手入力
def instrong(word):
    Mecabespresso.sentence(word)
    with open ("Mecabespresso/split.txt","r",encoding="UTF-8") as f:
        line=f.readlines()
        
    #強調ラベル
    SUW=[]
    for n in range(len(line)):
        if line[n]!="EOS\n":
            SUW.append(Mecabespresso.surface(line[n]))
    strong=[]
    while len(strong)!=len(SUW):
        print(SUW)
        print("input 0(non_strong) or 1(strong) example:0,1,1\n")
        st=input()
        st=st.replace(" ","")
        strong=st.split(",")
    return strong

#実験データ読み込み
print("複合名詞を入力してください。")
word=input()
print("条件を選んでください。kisoku,sur,pho")
condition=input()

#条件選択#出力
if condition=="kisoku":
    print(acmakekisoku.acmake(word))

elif condition=="sur":
    strong=instrong(word)
    print(acmakesurunidic.acmake(word,strong))
    
elif condition=="pho":
    strong=instrong(word)
    print(acmakephounidic.acmake(word,strong))
else:
    print("none")
    
