import zipfile
import sys
zFile = zipfile.ZipFile("evil.zip")

def entpackeDatei(zFile, passwort):
    try:
        zFile.extractall(pwd=passwort)
#        print("[-]"+passwort)
        return passwort
    except:
#        print(passwort+"\n")
        return

def main():
    passFile = open('German.dic')
    for line in passFile:
        passwort = line.rstrip()
#        print("Passwort: "+passwort)
        versuch = entpackeDatei(zFile, passwort)
        if versuch:
            print("[+] Passwort = "+passwort+"\n")
            exit(0)

main()