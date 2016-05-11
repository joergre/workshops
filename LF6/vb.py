:#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess
import sys, traceback
import crypt
print("UPDATE")

try:
	cmd1 = os.system("apt-get update > vb.log && sudo apt-get upgrade -y >> vb.log")
except:
	print("Update fehlgeschlagen!")

try:
        print("Installation von einigen Basisprogrammen")
	cmd1 = os.system("apt -y install screen emacs wget python-software-properties >> vb.log")
except:
	print("Installation fehlgeschlagen")

try:
        print("Repository hinzufügen")
        output = subprocess.check_output("lsb_release -sc", shell = True)
        lsb = output
        
        cmd1 = os.system("add-apt-repository 'deb http://download.virtualbox.org/virtualbox/debian "+lsb+" contrib'")
        cmd1 = os.system("add-apt-repository --remove 'deb-src http://download.virtualbox.org/virtualbox/debian "+lsb+" contrib'")
        # Änderung des Schlüssel für das Repository ab Ubuntu 16.04 (xenial)
        if lsb == "xenial":
                cmd1 = os.system("wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
        else:
                cmd1 = os.system("wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -")    
        cmd1 = os.system("apt-get update >> vb.log")
except:
        print("Repository hinzufügen fehlgeschlagen")
try:
        print("Instalation VirtualBox")
        output = subprocess.check_output("uname -r", shell = True)
        Kernel = output
        cmd1 = os.system("apt-get install -y linux-headers-"+Kernel)
        cmd1 = os.system("apt-get install -y build-essential virtualbox-5.0 dkms >> vb.log")
        cmd1 = os.system ("wget http://download.virtualbox.org/virtualbox/5.0.16/Oracle_VM_VirtualBox_Extension_Pack-5.0.16.vbox-extpack")
        cmd1 = os.system("VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-5.0.16.vbox-extpack")
        password ="fbs"
        encPass = crypt.crypt(password,"22")
        os.system("useradd -p "+encPass+" vbox -G vboxusers")
except:
        print("Installation von VirtualBox fehlgeschlagen")
