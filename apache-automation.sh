yum -y install httpd mod_ssl
systemctl start httpd
sed -i 's/^/#/g' /etc/httpd/conf.d/welcome.conf
echo "<html><body><h1>Hi there NTI 300</h1></body?></html>" > /var/www/html/index.html
systemctl restart httpd
