
#!/bin/bash

yum -y install python-pip
pip install virtualenv
pip install --upgrade pip 
mkdir ~/newproject   
cd ~/newproject   
virtualenv 3 newenv   
source newenv/bin/activate   
pip install django  
django-admin --version   
django-admin 3 startproject newproject  
cd newproject/
python manage.py migrate
python manage.py createsuperuser	
newproject/setting.py	
python manage.py runserver 0.0.0.0:8000   
