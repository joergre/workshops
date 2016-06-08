import zipfile
zFile = zipfile.ZipFile("evil.zip")
zFile.extractall(pwd="ASCII")