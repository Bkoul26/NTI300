#!/usr/bin/python 
#edited 11/6/2019 / troubleshooting issues on line 9 & line 47
import os
import re
import subprocess

def setup_install():
        print('isntalling pip and virtualenv so we can give django its own version of python')
        os.system('yum -y install python-pip && pip install --upgrade pip')
        os.system ('pip install virtualenv')
        os.chdir('/opt')
        os.mkdir('/opt/django')
        os.chdir('/opt/django')
        os.system('virtualenv django-env')
        os.system('chown -R bogdankoul /opt/django')
def django_install():
        print('Activating virtualenv and install django after pre-requirements have been met')
        os.system('source /opt/django/django-env/bin/activate && pip isntall django')
        os.chdir('/opt/django') 
        os.system('source /opt/django/django-env/bin/activate ' + \
              '&& django-admin --version' +\
              '&& django-admin startproject project1'+\
              '&& chown -R django /opt/django')

def django_start():
        print('starting django')
        os.system('chown -R bogdankoul /opt/django')
        os.chdir('/opt/django/project1')#cd's in the script
        os.system('source /opt/django/django-env/bin/activate' +\
              '&& python manage.py migrate')

        os.system('source /opt/django/django-env/bin/activate && echo "from django.contrib.auth import get_user_model; User = get_user_model();User.objects.create_superuser(\'admin\',\'admin@newproject.com\',\'NTI300NTI300\')" | python manage.py shell')

        outputwithnewline = subprocess.check_output('curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Address: //\' -e \'s/<.*$//\' ', shell=TRUE)
        print ('ouputwithnewline')
        output = outputwithnewline.replace("\n", "")
        old_string = "ALLOWED_HOSTS = []"
        new_string = 'ALLOWED_HOSTS = [\'{}\']'.format(output)
        print (new_string)
        print (old_string)

        with open('project1/settings.py') as f:
         newText=f.read().replace(old_string, new_string)
        with open('project1/settings.py', "w") as f:
         f.write(newText)
        
        os.system('sudo -u bogdankoul sh -c "source /opt/django/django-env/bin/activate && python manage.py runserver 0.0.0.0:8000&"')

setup_install()
django_install()
django_start()
