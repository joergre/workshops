cp my.cnf ~/.my.cnf 
apt update && apt -y upgrade
# Passwort und Benutzer für mysql festlegen:
debconf-set-selections <<< 'mysql-server mysql-server/root_password password fbs'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password fbs'
apt -y install mysql 
mysql -u root -pfbs -e "create database vmail;"
mysql -u root -pfbs -e "GRANT ALL ON vmail.* TO 'vmail'@'localhost' IDENTIFIED BY 'fbs';"
mysql "vmail" < "mysql"
