
from neutronclient.v2_0 import client as neutronclient
import keystoneclient.v2_0.client as ksclient
from novaclient.client import Client
from cinderclient import client as cinderclient
import os
import logging
import sys
logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

def get_nova_credentials_v2(region='Slo'):
  d = {}
  d['version'] = '2'
  d['username'] = os.environ['OS_USERNAME']
  d['api_key'] = os.environ['OS_PASSWORD']
  d['auth_url'] = os.environ['OS_AUTH_URL']
  d['project_id'] = os.environ['OS_TENANT_NAME']
  d['region_name'] = region
  return d

def get_glance_credentials_v1(region='Slo'):
  d = {}
  d['version'] = '2'
  d['username'] = os.environ['OS_USERNAME']
  d['api_key'] = os.environ['OS_PASSWORD']
  d['auth_url'] = os.environ['OS_AUTH_URL']
  d['project_id'] = os.environ['OS_TENANT_NAME']
  d['endpoint'] = os.environ['OS_IMAGE_ENDPOINT']
  d['token'] = os.environ['OS_AUTH_TOKEN']
  d['region_name'] = region
  return d

def get_keystone_credentials_v1(region='Slo'):
  d = {}
  d['auth_url'] = os.environ['OS_AUTH_URL']
  d['username'] = os.environ['OS_USERNAME']
  d['password'] = os.environ['OS_PASSWORD']
  d['tenant_name'] = os.environ['OS_TENANT_NAME']
  d['region_name'] = region
  return d

def get_cinder_credentials_v1(region='Slo'):
  d = {}
  d['version'] = '1'
  d['username'] = os.environ['OS_USERNAME']
  d['api_key'] = os.environ['OS_PASSWORD']
  d['auth_url'] = os.environ['OS_AUTH_URL']
  d['project_id'] = os.environ['OS_TENANT_NAME']
  d['region_name'] = region
  return d

def initialise_keystone():
  credentials = get_keystone_credentials_v1()
  keystone = ksclient.Client(**credentials)
  return keystone

def initialise_neutron(region=os.environ.get('OS_REGION_NAME')):
  credentials = get_keystone_credentials_v1(region=region)
  neutron = neutronclient.Client(**credentials)
  return neutron

def initialise_cinder(region=os.environ.get('OS_REGION_NAME')):
  credentials = get_cinder_credentials_v1(region)
  cinder = cinderclient.Client(**credentials)
  return cinder

def initialise_nova(region=os.environ.get('OS_REGION_NAME')):
  credentials = get_nova_credentials_v2(region)
  nova_client = Client(**credentials)
  return nova_client

try:
  NOVA_CLIENT = initialise_nova()
  CINDER = initialise_cinder()
  NEUTRON = initialise_neutron()
  KEYSTONE = initialise_keystone()
except KeyError, error:
  LOG.error("Please source your openstack credentials")
  sys.exit(99)
