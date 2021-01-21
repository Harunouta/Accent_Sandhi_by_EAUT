# -*- coding: utf-8 -*-
#CRFで予測したアクセント句の強調可能性()
#表層形のみを入力にしたもの(テンプレートはaの方、モデルは10/21に作成)
import subprocess

"""
1.CRF予測を格納する
"""
#CRF予測を格納する==============================================
def CRFbox(SUW):
    
    #test data maker
    with open ("CRFsyori2/test.txt","w",encoding="UTF-8")as f:
        for n in range(len(SUW)):
            f.write(SUW[n]+"\n")
        f.write("EOS\n")
    #run by CRF
    subprocess.run("crf_test -m CRFsyori2/model_file CRFsyori2/test.txt > CRFsyori2/result.txt",shell = True)
    #read results
    with open ("CRFsyori2/result.txt","r",encoding = "UTF-8")as f:
        lines = f.readlines()
        box = []
        for n in range(len(lines)):
            lines[n] = lines[n].split()
            if lines[n][0] == "EOS":
                break
            box.append(lines[n][1])
    return box



#test
#print(CRFbox(["三","回"]))

if __name__ == "__main__":
    main()


