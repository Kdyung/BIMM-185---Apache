README
Development Notes:
Directory: /var/www
 cd /var/www/
  
 check disk space df -h

#access the webserver installed
http://localhost/

#access the scripts written
vi hello.php
http://localhost/hello.py

#php to executable
python hello.py 
chmod a+x hello.php 

/etc/init.d/apache2 restart

vi /etc/apache2/sites-enabled/000-default 
vi /var/log/apache2/error.log 



This folder is the /www/ folder of Apache2 systems on a Linux platform. This contains the programs implemented with Apache2, PHP5 and MySQL.


Installation(from Onelaboratory):

>sudo apt-get install apache2
​>sudo apt-get install mysql-server
​>sudo apt-get install php5 libapache2-mod-php5
>sudo /etc/init.d/apache2 restart

After installation, you will need to configure your networking. I recommend a combination of "NAT" and "Host-only" as the networking interface. NAT will be used by the VM to connect to the internet, while Host-Only will allow you to connect to your VM (SSH-ing into it and testing your web services). By default, NAT is already configured on the Adapter 1 interface.

To add the Host-Only adapter, here are instructions:

Windows: http://askubuntu.com/questions/293816/in-virtualbox-how-do-i-set-up-host-only-virtual-machines-that-can-access-the-in
Mac: https://forums.virtualbox.org/viewtopic.php?f=8&t=34396

Once you have your network setup, you should be able to SSH into your VM by using either putty in windows or command line terminal on Mac.

>ssh username@192.168.XX.XXX

The IP address should be whatever you set it in your /etc/network/interfaces file of the Ubuntu install.

Configure Your WebServer for Scripting

To execute python or perl scripts on your webserver, you will need to do some configuration. First, you will need to enable the cgi module in Apache2:

>sudo a2enmod cgi

Then edit the file /etc/apache2/sites-enabled/000-default (may also be just "default") and add the following under the line "DocumentRoot /var/www/html". Some versions may only contain "/var/www" so remove "html" from the path.

       <Directory />
                Options FollowSymLinks
                AllowOverride None
       </Directory>
       <Directory /var/www/html>
                Options Indexes FollowSymLinks MultiViews ExecCGI
​                DirectoryIndex index.cgi index.php index.html
                AllowOverride All
                Order allow,deny
                allow from all
        </Directory>

Restart your web server: >sudo /etc/init.d/apache2 restart
After that, you should be able to run python or perl scripts anywhere inside /var/www/html/
Make sure to make your scripts executable: chmod a+x myscript.py
