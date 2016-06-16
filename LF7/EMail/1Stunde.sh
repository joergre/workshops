#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess
import sys, traceback
import crypt
# .my.cnf kann das Passwort und Benutzername von MySQL-Nutzern hinterlegt werden. Achtung: Sicherheitsrisiko!
cp my.cnf ~/.my.cnf 
# Update Upgrade
cmd1 = os.system("apt-get update > vb.log && sudo apt-get upgrade -y >> vb.log")
# Passwort und Benutzer für mysql festlegen:
cmd1 = os.system("debconf-set-selections <<< 'mysql-server mysql-server/root_password password fbs'")
cmd1 = os.system("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password fbs'")
# Datenbank installieren
cmd1 = os.system("apt -y install mysql") 
# Datenban vmail anlegen
cmd1 = os.system("mysql -u root -pfbs -e 'create database vmail;'")
# benutzer vmail anlegen
cmd1 = os.system("mysql -u root -pfbs -e 'GRANT ALL ON vmail.* TO 'vmail'@'localhost' IDENTIFIED BY 'fbs';'")
# Tabellen anlegen
cmd1 = os.system("mysql 'vmail' < 'mysql')
