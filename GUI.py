# -*- coding: utf-8 -*-
import acmakeGiopenjtalk #数詞あり規則読みunidic
import acmakesurunidic
import acmakephounidic

from Mecabespresso import Mecabespresso

import tkinter as tk

root = tk.Tk()
root.title("do-GUI")
root.geometry()
c=0

#Frame
Frame1=tk.Frame(root)
Frame2=tk.Frame(root)
Frame2a=tk.Frame(root)
Frame3=tk.Frame(root)
Frame4=tk.Frame(root)
Frame5=tk.Frame(root)
Frame6=tk.Frame(root)
Frame7=tk.Frame(root)
Frame8=tk.Frame(root)
Frame9=tk.Frame(root)
Frame10=tk.Frame(root)

#doing
def bunkatsu():
    global word
    word = lab2.get()
    Mecabespresso.sentence(word)
    with open ("Mecabespresso/split.txt","r",encoding="UTF-8") as f:
        line=f.readlines()

    #SUW
    global SUW,strong ,c,chk,chk_bln
    SUW=[]
    strong=[]
    for n in range(len(line)):
        if line[n]!="EOS\n":
            SUW.append(Mecabespresso.surface(line[n]))
        strong.append(0)

    #推定方法選べるように
    lab5.configure(state='active')
    lab6.configure(state='active')
    lab7.configure(state='active')
    
    #もともとあったものをどう破壊するか
    if c!=0:
        for n in range(len(chk)):
            chk[n].destroy()
    chk=[]
    chk_bln = {}#チェックボックスにチェックが入っているかどうかを
    
    for i in range(len(SUW)):
        chk_bln[i] = tk.BooleanVar()
        chk.append(tk.Checkbutton(Frame6,variable=chk_bln[i],text=str(SUW[i]))) 
        chk[i].pack(side ="left")
    c=1

def touch():
    for n in range(len(chk)):
        chk[n].configure(state='active')
def untouch():
    for n in range(len(chk)):
        chk[n].configure(state='disabled')
def do():
    def st():
        global strong,chk_bln
        for m in range(len(chk_bln)):
            if chk_bln[m].get()==1:
                strong[m]="1"
            else:
                strong[m]="0"
    global ans
    ans=""
    if var.get()==1:
        #print(acmakeGiopenjtalk.acmake(word))
        lab12.configure(state='active')
        ans=str(acmakeGiopenjtalk.acmake(word))
        lab12["text"] = ans
    elif var.get()==2:
        st()
        lab12.configure(state='active')
        ans=str(acmakephounidic.acmake(word,strong))
        lab12["text"] = ans 
    elif var.get()==3:
        st()
        lab12.configure(state='active')
        ans=str(acmakesurunidic.acmake(word,strong))
        lab12["text"] = ans
    else:
        pass
    
def clear():
    if c!=0:
        for n in range(len(chk)):
            chk[n].destroy()
    lab5.configure(state='disabled')
    lab6.configure(state='disabled')
    lab7.configure(state='disabled')
    lab12["text"] = ""
    lab2.delete(0, tk.END) 

def copy():
    lab14.clipboard_clear()
    lab14.clipboard_append(ans)
    pass

#widget
lab1 = tk.Label(Frame1, text="複合名詞(コピペなら確実)")

lab2 = tk.Entry(Frame2)
lab2.insert(tk.END,"複合名詞")

lab3 = tk.Button(Frame2a, text="分割",command=bunkatsu)

lab4 = tk.Label(Frame3, text="アクセント句推定方法")

var = tk.IntVar()
var.set(0)
lab5=tk.Radiobutton(Frame4,variable=var,value=1,text="規則",command=untouch)
lab5.configure(state='disabled')
lab6=tk.Radiobutton(Frame4,variable=var,value=2,text="読みありCRF",command=touch)
lab6.configure(state='disabled')
lab7=tk.Radiobutton(Frame4,variable=var,value=3,text="読みなしCRF",command=touch)
lab7.configure(state='disabled')

lab8=tk.Label(Frame5,text="強調")
lab10=tk.Button(Frame7,text="実行",command=do)

lab11=tk.Label(Frame8,text="結果")

lab12=tk.Label(Frame9,text="[出力結果]")
lab12.configure(state='disabled')

lab13=tk.Button(Frame10,text="クリア",command=clear)#入力と強調ラベルを削除
lab14=tk.Button(Frame10,text="コピー",command=copy)

"""
 0 1 2 3 4
0
1
2
3
4
...
"""
#位置
Frame1.grid(row=0, column=1)
Frame2.grid(row=1, column=1)
Frame2a.grid(row=2, column=3)
Frame3.grid(row=3, column=0)

Frame4.grid(row=4, column=1)

Frame5.grid(row=5, column=0) 
 
Frame6.grid(row=6, column=1)

Frame7.grid(row=7, column=3)

Frame8.grid(row=8, column=0)

Frame9.grid(row=9, column=1)

Frame10.grid(row=10, column=4)

#決定
lab1.pack(anchor="c")
lab2.pack()
lab3.pack()
lab4.pack()
lab5.pack(side="left")
lab6.pack(side="left")
lab7.pack(side="left")
lab8.pack()
#lab9.pack()
lab10.pack()
lab11.pack()
lab12.pack()
lab13.pack(side="right")
lab14.pack(side="right")


root.mainloop()
