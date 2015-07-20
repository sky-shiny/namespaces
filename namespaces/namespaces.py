from . import NEUTRON


class RegionError(Exception):
    """Wrong region error."""
    def __init__(self, message):
        Exception.__init__(self, message)

def get_namespaces(quantum_gateway):
    '''
    Get a list of namespaces for a given quantum gateway
    :return: list of namespaces
    '''
    agents = NEUTRON.list_agents()
    try:
        qgateways_dhcp_agent = [agent['id'] for agent in agents['agents'] if
                                'neutron-dhcp-agent' in agent['binary'] and quantum_gateway in agent['host']]
        dhcp_networks = NEUTRON.list_networks_on_dhcp_agent(qgateways_dhcp_agent[0])
        dhcp_namespaces = ['qdhcp-' + net['id'] for net in dhcp_networks['networks']]

        qgateways_l3_agent = [agent['id'] for agent in agents['agents'] if
                              'neutron-l3-agent' in agent['binary'] and quantum_gateway in agent['host']]
        l3_routers = NEUTRON.list_routers_on_l3_agent(qgateways_l3_agent[0])
        router_namespaces = ['qrouter-' + router['id'] for router in l3_routers['routers']]

        qgateways_lb_agent = [agent['id'] for agent in agents['agents'] if
                              'neutron-lbaas-agent' in agent['binary'] and quantum_gateway in agent['host']]
        lb_pools = NEUTRON.list_pools_on_lbaas_agent(qgateways_lb_agent[0])
        lb_namespaces = ['qlbaas-' + lb['id'] for lb in lb_pools['pools']]

        namespaces = dhcp_namespaces + lb_namespaces + router_namespaces

        return namespaces
    except IndexError:
        raise RegionError("Agent does not exist in this region please update your environment.")
