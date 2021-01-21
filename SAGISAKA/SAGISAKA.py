# -*- coding: utf-8 -*-
#unidicやOPEN J TALKで言われているアクセントの結合法則を元論文から再現
#『日本語単語連鎖のアクセント規則』(匂坂.et.al.1983)



#アクセント結合する部分====================================
def C(n1,m1,m2,Cnum):
    ku = "0"
    if Cnum == "C1":
        ku = n1 + m2
    if Cnum == "C2":
        ku = n1 + 1
    if Cnum == "C3":
        ku = n1
    if Cnum == "C4":
        ku = 0
    if Cnum == "C5":
        ku = m1
    return ku


def N(n1,n2,m1,m2):
    ku = "0"
    if m1 == 0:
        if m2 == 0:
            ku = 0
        else:
            ku = n1 + m2
    else:
        if m2 == 0:
            ku = m1
        else:
            ku = m1
    return ku


def P(n1,n2,m1,m2,Pnum):
    ku = "0"
    if Pnum == "P1":
        if m2 == 0 or m2 == n2:
            ku = 0
        else:
            ku = n1 + m2
    if Pnum == "P2":
        if m2 == 0 or m2 == n2:
            ku = n1 + 1
        else:
            ku = n1 + m2
    if Pnum == "P4":
        if m2 == 0 or m2 == n2:
            ku = n1 + 1
        else:
            ku = m1
    if Pnum ==" P6":
        ku = 0
    if Pnum == "P13":
        ku = m1
    if Pnum == "P14":
        if m2 == 0 or m2 == n2:
            ku = m1
        else:
            ku = n1 + m2
    return ku

def F(n1,m1,Fnum,pos):
    #m=@以降の数字,l=カンマ以降の数字
    ku = "0"
    Fnum = Fnum.split(",")
    fnum = ""
    for n in range(len(Fnum)):
        if pos in Fnum[n]:#前句の品詞にあったものを選択、なかったらN
            fnum = Fnum[n]
    if fnum == "":
        fnum = Fnum[0]
        
    if "%" in fnum:
        fnum = fnum.split("%")[1]
    if "F1" in fnum:
        ku = m1
    if "F2" in fnum:
        m = int(fnum.split("@")[1])
        if m1 == 0:
            ku = n1 + m
        else:
            ku = m1
    if "F3" in fnum:
        m = int(fnum.split("@")[1])
        if m1 == 0:
            ku = m1
        else:
            li = n1 + m
    if "F4" in fnum:
        m = int(fnum.split("@")[1])
        ku = n1 + m
    if "F5" in fnum:
        ku = 0
    if "F6" in fnum:
        m = int(Fnum.split("@")[1].split(",")[0])
        l = int(Fnum.split("@")[1].split(",")[1])
        if n1 == 0:
            ku = n1 + m
        else:
            ku = n1 + l
    return ku

def M(n0,m0,Mnum):
    ku = "0"
    m = int(Mnum.split("@")[1])
    Mnum = Mnum.split("@")[0]
    if Mnum == "M1":
        ku = n0 - m
    if Mnum == "M2":
        if m0 == 0:
            ku = n0 - m
        else:
            ku = m0
    if Mnum == "M4":
        if m0 == 0 or m0 == 1:
            ku = m0
        else:
            ku = m0 - m

    return ku

if __name__ == "__main__":
    main()

