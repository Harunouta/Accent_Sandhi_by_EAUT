# -*- coding: utf-8 -*-

#『日本語文音声変換のための数詞読み規則』(宮崎.1984)
#『条件付確率場に基づく日本語アクセント型予測モデルの改良と日本語教育システムへの応用』(小林.2012)より

#参考:TASET(rule.py mkdata_accent.py)

def MIYAZAKI(n1,n2,orth,orth2,sushi):
    josushi = ""
    if orth == "個" or orth == "位" or orth == "時" or orth == "分" \
       or orth == "時間" or orth == "歳" or orth == "羽" or orth == "通り" \
       or orth == "斤" or orth == "層" or orth == "アール" or orth == "センチ" \
       or orth == "キロ" or orth == "ドル" or orth == "度" or orth == "階" \
       or orth == "球" or orth == "巡" or orth == "乗" or orth == "週" \
       or orth == "人前" or orth == "敗" or orth == "着" or orth == "度目" \
       or orth == "代目" or orth == "貫目" or orth == "日目" or orth == "球目" \
       or orth == "丁目" or orth == "畳" or orth == "ヶ月":
        josushi = "a"
        
    elif orth == "問" or orth == "台" or orth=="軒" or orth=="件" or orth=="票" \
         or orth=="町" or orth=="艘" or orth=="代" or orth=="枚" or orth=="名" \
         or orth=="面" or orth=="本" or orth=="杯" or orth=="丁":
        josushi = "b"
        
    elif orth == "升":
        josushi = "c"
        
    elif orth == "年" or orth == "段" or orth == "番":
        josushi = "d"
        
    elif orth == "貫" or orth == "版" or orth == "銭" or orth == "回" \
         or orth == "点" or orth == "巻":
        josushi = "e"
        
    elif orth == "尺" or orth == "着" or orth == "角":
        josushi = "f"
        
    elif orth == "円":
        josushi = "g"
        
    elif orth == "曲" or orth == "石" or orth == "匹" or orth == "冊" \
         or orth == "足" or orth == "拍" or orth == "脚" or orth == "局" \
         or orth == "発" or orth == "室" or orth == "節":
        josushiType = "h"
        
    elif orth == "合":
        josushi = "i"

    elif orth == "人":
        josushi = "j"

    elif orth == "月" or orth == "日":
        josushi= "k"

    elif orth == "寸":
        josushi = "l"

    else:
        josushi = "m"
    

#バグ対策
    if len(orth2) < 1:
        orth2 = "-" + orth2
        
# 0型となる規則
    if sushi == "N1"and josushi == "g" \
       or sushi == "N2" and josushi == "g" or orth2[-1] in ["二","2","２"] and josushi == "g" \
       or sushi == "N3" and josushi == "g" or orth2[-1] in ["三","3","３"] and josushi == "g" \
       or sushi == "N6" and josushi == "g" or orth2[-1] in ["六","6","６"] and josushi == "g" \
       or sushi == "N8" and josushi == "g" or orth2[-1] in ["八","8","８"] and josushi == "g" \
       or sushi == "N3" and josushi == "d" or orth2[-1] in ["三","3","３"] and josushi == "d" \
       or sushi == "N4" and josushi == "d" or orth2[-1] in ["四","4","４"] and josushi == "d" \
       or sushi == "N5" and josushi == "d" or orth2[-1] in ["五","5","５"] and josushi == "d" \
       or sushi == "N3" and josushi == "c" or orth2[-1] in ["三","3","３"] and josushi == "c" \
       or sushi == "N5" and josushi == "c" or orth2[-1] in ["五","5","５"] and josushi == "c" \
       or sushi == "N5" and josushi == "b" or orth2[-1] in ["五","5","５"] and josushi == "b" \
       or orth2[-1] == "千" \
       or orth2[-1] == "億" \
       or orth2[-1] == "万" \
       or orth2[-1] == "兆" \
       or sushi == "Ns" \
       or sushi == "Nm":
        target = 0

#助数詞の第一音節
    elif sushi == "N0" and josushi == "e" \
         or sushi == "N1" and josushi == "e" or orth2[-1] in ["一","1","１"] and josushi == "e" \
         or sushi == "N2" and josushi == "e" or orth2[-1] in ["二","2","２"] and josushi == "e" \
         or sushi == "N3" and josushi == "e" or orth2[-1] in ["三","3","３"] and josushi == "e" \
         or sushi == "N5" and josushi == "e" or orth2[-1] in ["五","5","５"] and josushi == "e" \
         or sushi == "N6" and josushi == "e" or orth2[-1] in ["六","6","６"] and josushi == "e" \
         or sushi == "N8" and josushi == "e" or orth2[-1] in ["八","8","８"] and josushi == "e" \
         or sushi == "N1" and josushi == "i" or orth2[-1] in ["一","1","１"] and josushi == "i" \
         or sushi == "N2" and josushi == "i" or orth2[-1] in ["二","2","２"] and josushi == "i" \
         or sushi ==" N5" and josushi == "i" or orth2[-1] in ["五","5","５"] and josushi == "i" \
         or sushi == "N6" and josushi == "i" or orth2[-1] in ["六","6","６"] and josushi == "i" \
         or sushi == "N3" and josushi == "j" or orth2[-1] in ["三","3","３"] and josushi == "j" \
         or sushi == "N4" and josushi == "j" or orth2[-1] in ["四","4","４"] and josushi == "j" \
         or sushi == "N5" and josushi == "j" or orth2[-1] in ["五","5","５"] and josushi == "j" \
         or sushi == "N9" and josushi == "j" or orth2[-1] in ["九","9","９"] and josushi == "j" \
         or sushi == "N1" and josushi == "l" or orth2[-1] in ["一","1","１"] and josushi == "l" \
         or sushi == "N2" and josushi == "l" or orth2[-1] in ["二","2","２"] and josushi == "l" \
         or sushi == "N5" and josushi == "l" or orth2[-1] in ["五","5","５"] and josushi == "l" \
         or sushi == "N6" and josushi == "l" or orth2[-1] in ["六","6","６"] and josushi == "l" \
         or sushi == "N8" and josushi == "l" or orth2[-1] in ["八","8","８"] and josushi == "l" \
         or sushi == "Nj" and josushi == "l" or orth2[-1] == "十" and josushi == "l" \
         or sushi == "Nh" and josushi == "l" or orth2[-1] == "百" and josushi == "l":
        target = n1 + 1

#助数詞の最終音節
    elif sushi == "N0" and josushi == "f" \
         or sushi == "N1" and josushi == "f" or orth2[-1] in ["一","1","１"] and josushi == "f" \
         or sushi == "N2" and josushi == "f" or orth2[-1] in ["二","2","２"] and josushi == "f" \
         or sushi == "N5" and josushi == "f" or orth2[-1] in ["五","5","５"] and josushi == "f" \
         or sushi == "N6" and josushi == "f" or orth2[-1] in ["六","6","６"] and josushi == "f" \
         or sushi == "N8" and josushi == "f" or orth2[-1] in ["八","8","８"] and josushi == "f" \
         or sushi == "Nj" and josushi == "f" or orth2[-1] == "十" and josushi == "f" \
         or sushi == "N1" and josushi == "h" or orth2[-1] in ["一","1","１"] and josushi == "h" \
         or sushi == "N6" and josushi == "h" or orth2[-1] in ["六","6","６"] and josushi == "h" \
         or sushi == "N8" and josushi == "h" or orth2[-1] in ["八","8","８"] and josushi == "h" \
         or sushi == "N1" and josushi == "k" or orth2[-1] in ["一","1","１"] and josushi == "k" \
         or sushi == "N2" and josushi == "k" or orth2[-1] in ["二","2","２"] and josushi == "k" \
         or sushi == "N4" and josushi == "k" or orth2[-1] in ["四","4","４"] and josushi == "k" \
         or sushi == "N6" and josushi == "k" or orth2[-1] in ["六","6","６"] and josushi == "k" \
         or sushi == "N7" and josushi == "k" or orth2[-1] in ["七","7","７"] and josushi == "k" \
         or sushi == "N8" and josushi == "k" or orth2[-1] in ["八","8","８"] and josushi == "k" \
         or sushi == "Nj" and josushi == "k" or orth2[-1] == "十" and josushi == "k" \
         or sushi == "Nh" and josushi == "k" or orth2[-1] == "百" and josushi == "k":
        target = n1 + n2
    else:
        target = ""
        
    return target

           
if __name__ == "__main__":
    main()
