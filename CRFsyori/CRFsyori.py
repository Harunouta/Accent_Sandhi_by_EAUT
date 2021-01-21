# -*- coding: utf-8 -*-
#CRFで予測したアクセント句の強調可能性()
import subprocess

"""
1.CRF予測を格納する
"""
#CRF予測を格納する==============================================
def CRFbox(SUW,pho):
    
    #test data maker
    with open ("CRFsyori/test.txt","w",encoding = "UTF-8")as f:
        for n in range(len(SUW)):
            if pho[n] == "":#読みなし回避
                p = "*"
            else:
                p = pho[n]
            f.write(SUW[n]+"\t"+p+"\n")
        f.write("EOS\tEOS\n")
    #run by CRF
    subprocess.run("crf_test -m CRFsyori/model_file CRFsyori/test.txt > CRFsyori/result.txt",shell = True)
    #read results
    with open ("CRFsyori/result.txt","r",encoding = "UTF-8")as f:
        lines = f.readlines()
        box = []
        for n in range(len(lines)):
            lines[n] = lines[n].split()
            if lines[n][0] == "EOS":
                break
            box.append(lines[n][2])
    return box



#test
#print(CRFbox(["三","回"],["サン","カイ"]))

if __name__ == "__main__":
    main()

