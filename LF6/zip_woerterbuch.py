import zipfile
import sys
from threading import Thread
zFile = zipfile.ZipFile("evil.zip")

def entpackeDatei(zFile, passwort):
    try:
        zFile.extractall(pwd=passwort)
        print("[+]"+passwort+"\n")
    except:
        print("[]"+passwort+"\n")
        pass

def main():
    passFile = open('German.dic')
    for line in passFile:
        passwort = line.rstrip()
        t =Thread(target= entpackeDatei, args =(zFile, passwort))
        t.start()

main()