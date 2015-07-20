__author__ = 'mca18'

from .credentials import get_nova_credentials_v2, get_keystone_credentials_v1, get_cinder_credentials_v1, NOVA_CLIENT, CINDER, NEUTRON
from .credentials import initialise_nova, initialise_cinder, initialise_neutron, initialise_keystone
from .namespaces import get_namespaces, RegionError
