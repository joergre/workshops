import zipfile
import sys
zFile = zipfile.ZipFile("evil.zip")
try:
    zFile.extractall(pwd="bloedsinn")
except:
        print(sys.exc_info()[0])