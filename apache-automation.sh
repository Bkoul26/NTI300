#!/bin/bash
if [ -e/etc/httpd ]; then  
 exit 0                    
 fi                             
yum -y install httpd mod_ssl                                                                       # install apache and ssl
systemctl start httpd                                                                              # start apach
sed -i 's/^/#/g' /etc/httpd/conf.d/welcome.conf                                                    # WELCOME PAGE 
echo "<html><body><h1>Hi there NTI 300</h1></body?></html>" > /var/www/html/index.html             # CUSTOM WELCOME PAGE CREATED 
systemctl restart httpd                                                                            # restart apache forr changes to take effect
