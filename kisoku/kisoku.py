# -*- coding: utf-8 -*-
#OPEN J TALKで言われているアクセントの結合法則を元論文から再現
#【注意】実際のOPENJTALKはアクセント核の推定にCRFを用いているため、
#実際のOPENJTALKと推定結果は一致しない。

#アクセント結合方法
"""
OPEN_J_TALK (njd_set_accent_phrase_rule_utf_8.h)より
/*
  Rule 01 デフォルトはくっつける
  Rule 02 「名詞」の連続はくっつける
  Rule 03 「形容詞」の後に「名詞」がきたら別のアクセント句に
  Rule 04 「名詞,形容動詞語幹」の後に「名詞」がきたら別のアクセント句に
  Rule 05 「動詞」の後に「形容詞」or「名詞」がきたら別のアクセント句に
  Rule 06 「副詞」，「接続詞」，「連体詞」は単独のアクセント句に
  Rule 07 「名詞,副詞可能」（すべて，など）は単独のアクセント句に
  Rule 08 「助詞」or「助動詞」（付属語）は前にくっつける-
  Rule 09 「助詞」or「助動詞」（付属語）の後の「助詞」，「助動詞」以外（自立語）は別のアクセント句に
  Rule 10 「*,接尾」の後の「名詞」は別のアクセント句に
  Rule 11 「形容詞,非自立」は「動詞,連用*」or「形容詞,連用*」or「助詞,接続助詞,て」or
          「助詞,接続助詞,で」に接続する場合に前にくっつける
  Rule 12 「動詞,非自立」は「動詞,連用*」or「名詞,サ変接続」に接続する場合に前にくっつける
  Rule 13 「名詞」の後に「動詞」or「形容詞」or「名詞,形容動詞語幹」がきたら別のアクセント句に
  Rule 14 「記号」は単独のアクセント句に <-これはCSJ上は「記号」の後は別のアクセント句に
  Rule 15 「接頭詞」は単独のアクセント句に
  Rule 16 「*,*,*,姓」の後の「名詞」は別のアクセント句に
  Rule 17 「名詞」の後の「*,*,*,名」は別のアクセント句に
  Rule 18 「*,接尾」は前にくっつける
*/
各用語とunidicとの対応================
品詞:pos1
非自立:pos2
語幹:pos3
活用形:cForm
姓名:lType
記号:goshu
て:orthBase
くっつける->0
別のアクセント句->1,~
単独アクセント句->1,1
"""
#アクセント結合する部分====================================
def Gi(pos1a,pos1b,pos2a,pos2b,pos3a,pos3b,orthBaseb,\
       cFormb,goshua,goshub,lTypea,lTypeb):
    #01
    kugiri = 0
    
    #02
    if pos1a == "名詞" and pos1b == "名詞":
        kugiri = 0

    #03    
    if pos1a == "形容詞" and pos1b == "名詞":
        kugiri = 1

    #04
    if pos1a == "名詞" and pos3a in ["形状詞可能","サ変形状詞可能"] \
       and pos1b == "名詞":
        kugiri = 1

    #05
    if pos1a == "動詞" and pos1b == "形容詞" \
       or pos1a == "動詞" and pos1b == "名詞":
        kugiri = 1

    #06-1    
    if pos1b == "副詞" or pos1b == "接続詞" or pos1b == "連体詞":
        kugiri=1
    #06-2
    if pos1a == "副詞" or pos1a == "接続詞" or pos1a == "連体詞":
        kugiri=1

    #07-1    
    if pos1b == "名詞" and pos3b == "副詞可能":
        kugiri = 1
    #07-2
    if pos1a == "名詞" and pos3a == "副詞可能":
        kugiri = 1

    #08    
    if pos1b == "助詞" or pos1b == "助動詞":
        kugiri = 0

    #09    
    if pos1a == "助詞" and pos1b not in ["助詞","助動詞"] \
       or pos1a == "助動詞" and pos1b not in ["助詞","助動詞"]:
        kugiri = 1

    #10    
    if pos1a == "接尾辞" and pos1b == "名詞":
        kugiri = 1

    #11
    if "形容詞非自立可能動詞連用" in pos1a + pos2a + pos1b + cFormb \
       or "形容詞非自立可能形容詞連用" in pos1a + pos2a + pos1b + cFormb \
       or "形容詞非自立可能助詞接続助詞て" in pos1a + pos2a + pos1b + pos2b + orthBaseb \
       or "形容詞非自立可能助詞接続助詞で" in pos1a + pos2a + pos1b + pos2b + orthBaseb:
        kugiri = 0

    #12    
    if "動詞非自立可能動詞連用" in pos1a + pos2a + pos1b + cFormb \
        or "動詞非自立可能名詞サ変可能" in pos1a + pos2a + pos1b + pos3b \
        or "動詞非自立可能名詞サ変形状詞可能" in pos1a + pos2a + pos1b + pos3b:
        kugiri = 0

    #13
    if pos1a + pos1b == "名詞動詞" \
       or pos1a + pos1b == "名詞形容詞" \
       or pos1a + pos1b + pos3b in ["名詞名詞形状詞可能","名詞名詞サ変形状詞可能"]:
        kugiri = 1

    #14-1
    #if goshub == "記号":
    #    kugiri = 1
    #14-2
    if goshua == "記号":
        kugiri = 1

    #15-1
    if pos1b == "接頭辞":
        kugiri = 1
    #15-2
    if pos1a == "接頭辞":
        kugiri = 1

    #16
    if lTypea == "姓" and pos1b == "名詞":
        kugiri = 1

    #17
    if pos1a == "名詞" and lTypeb == "名":
        kugiri = 1

    #18
    if pos1a == "接尾辞":
        kugiri = 0

    return kugiri

if __name__ == "__main__":
    main()

