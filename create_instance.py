#!/usr/bin/python
#Google cloud assignment

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
import pprint
import json

credentials = GoogleCredentials.get_application_default()
compute = discovery.build('compute','v1', credentials=credentials)

project = 'rising-rune-254201'
zone = 'us-central1-a'
name = 'django-final'

def list_instances(compute,project,zone):
  result = compute.instances().list(project=project,zone=zone).execute()
  return result['items']
  
def create_instance(compute,project,zone,name):
 startup_script = open('startup-script.sh','r').read()
 image_response = compute.images().getFromFamily(
   project = 'centos-cloud', family = 'centos-7').execute()
 
 source_disk_image = image_response['selfLink']
 machine_type = "zones/%s/machineTypes/f1-micro" % zone
 #next up
 config = {
  'name' : name,
  'machineType' : machine_type,
  
  'disks': [
    {
      'boot': True,
      'autoDelete': True,
      'initializeParams': {
        'sourceImage': source_disk_image, # Specify the boot disk and image 
      }
    }
  ],
  

  'networkInterfaces': [{
    'network': 'global/networks/default',
    'accessConfigs': [   # Specify a network interface with NAT adapter
      {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
    ]
  }],
  
  # Allow the instance to access cloud storage and logging.
  'serviceAccounts': [{
    'email': 'default',
    'scopes': [
      'https://www.googleapis.com/auth/devstorage.read_write',
      'https://www.googleapis.com/auth/logging.write'
    ]
  }],
  
  # Enablle http/https for select instances
  "labels": {
    "http-server": "",
    "https-server": ""
  },
  
  "tags": {
    "items": [
      "http-server",
      "https-server"
    ]
  },
  
  
  'metadata': {
    'items': [{# Metadata is being read from instances
      
      'key': 'startup-script',
      'value': startup_script
    }] # Startup script is auto execute by this instance and automated
  }
 }
 
 return compute.instances().insert(
  project=project,
  zone=zone
  body=config).execute()

newinstance = create_instance(compute,project,zone,name)
instances = list_instances(compute,project,zone)

pprint.pprint(newinstance)
pprint.pprint(instances)
