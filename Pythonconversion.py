#!/usr/bin/python

import os
import re
import subprocess

def setup_install(0):
    print('Installing pip and virtualenv so we can give DJANGO its own version of Python')
    os.system('yum -y install python-pip && pip install --upgrade pip')
    os.system('pip install virtualenv')
    os.chdir('/opt')
    os.mkdir('/opt/django')
    os.system('virtualenv django-env')
    os.system('chown -R bogdankoul /opt/django')
#chown doesnt work as well
def django_install():
    print('Activating virtualenv and isntall django after pre-requirements have been met')
    os.system('source /opt/django/django-env/bin/activate && pip isntall django')
    os.chdir('/opt/django')
    os.system('source /opt/django/django-env/bin/activate ' + \
              '&& django-admon --version' +\
              '&& djang0-admin startproject project1')

def django_start():
    print('starting django')
    os.system('chown -R bogdankoul /opt/django')
    os.chdir('/opt/django/project1')
    os.system('source /opt/django/django-env/bin/activate' +\
              '&& python manag.py migrate')

    os.system('source /opt/django/django-env/bin/activate && echo "from django.contrib.auth import get_user_model; User = get_user_model();User.objects.create_superuser(\'admin\',\'admin@newproject.com\',\'NTI300NTI300\')" | python manage.py shell')

    outputwithnewline = subprocess.check_output('curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Address: //\' -e \'s/<.*$//\' ', shell=TRUE)
    print ouputwithnewline
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
