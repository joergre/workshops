#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess
import sys, traceback
import crypt
print("Kopiere: .my.cnf kann das Passwort und Benutzername von MySQL-Nutzern hinterlegt werden. Achtung: Sicherheitsrisiko!")
cp my.cnf ~/.my.cnf 
# Update Upgrade
print("Update und Upgrade des Betriebssystems")
cmd1 = os.system("apt-get update -qq && sudo apt-get upgrade -y -qq")
print(" Passwort und Benutzer für mysql festlegen: fbs/bs")
cmd1 = os.system("debconf-set-selections <<< 'mysql-server mysql-server/root_password password fbs'")
cmd1 = os.system("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password fbs'")
print(" Datenbank installieren")
cmd1 = os.system("apt -y install mysql") 
print(" Datenban vmail anlegen.")
cmd1 = os.system("mysql -u root -pfbs -e 'create database vmail;'")
print("Benutzer vmail anlegen.")
cmd1 = os.system("mysql -u root -pfbs -e 'GRANT ALL ON vmail.* TO 'vmail'@'localhost' IDENTIFIED BY 'fbs';'")
print("Tabellen anlegen")
cmd1 = os.system("mysql 'vmail' < 'mysql')
