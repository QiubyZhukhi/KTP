#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print ("""
Basic for Modul Androidhelper py2.7 Func 
phoneDialNumber
Coded: QiubyZhukhi
""")
from sl4a import Android as droid
import os
import errno

path = "/storage/sdcard1/###/"

def folder(p):
    try:
        os.makedirs(path)
    except IOError and OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    return p

def sms():
    while True:
        droid.vibrate()
        nik = input("NIK: ")
        kk = input("KK: ")
        format1 = "*444*%s*%s#" % (nik,kk) #Untuk format Call
        droid.phoneCallNumber(format1)
        print (format1)
        droid.setClipboard(kk)
        print("Nomor KK otomtis di Copy")
        with open(file+"NIK2.txt","a+") as f:
            f.write(format1+"\n")
        ask = input("Continue? please Enter: ")
        if ask == "":
            os.system("clear")
            continue
        else:
            break        
    print ("SELESAI")
if __name__ == "__main__":
    droid = droid()
    file = folder(path)
    sms()