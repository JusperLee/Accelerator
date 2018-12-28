# coding:GBK
import os

def function1(n):
    s = ""

    for i in range(10):
        mystr = os.popen(r".\bing.exe")
        str1 = mystr.read()
        str1=str(str1)
        s_list=str1.split(" ")
        print(s_list)
        if i != 9:
            start = str1.find("Time")
            s = s + s_list[2]+"\n"
        if i == 9:
            start = str1.find("Time")
            s = s + s_list[2]


    ff = open("time"+str(n)+".txt", 'w')
    ff.write(s)
    ff.close()


