Namespaces
==========


Takes the name of a neutron agent and returns a list of namespaces that should exist on that agent.


Installation
------------


```
pip install git+https://github.com/sky-shiny/namespaces.git
```

Usage
-----

Source your openstack credentials.

```
ns --help
usage: ns [-h] host

positional arguments:
  host        Which host should we look up the namespace for

optional arguments:
  -h, --help  show this help message and exit
```

Example
-------

```
neutron agent-list | grep quantum | head -1 | awk '{print $8}'
#quantum-gateway-RegionOne1234
ns quantum-gateway-RegionOne1234
#qdhcp-04435a04-6fff-4212-aa68-9c3006edeca1
#qdhcp-17624bd6-5949-41b5-9286-b2f466d3f9c1
#qdhcp-3215a2e8-2143-42f8-8293-67833e54d401
#qdhcp-3356f7d5-e8d7-4d67-954d-9a1f9faf48b1
#qdhcp-3f8d6142-3d30-4230-8fdb-1b5a42e5d1f1
#qdhcp-ba1ac7a4-c7d5-4794-9f2b-cba959c64b11
#qdhcp-efa9e122-782d-4d0a-8b77-6f18c3620921
#qdhcp-f09c765d-d94a-4724-8295-dcf921f27771
#qdhcp-fb5f2348-94c8-4a14-86de-00a36a8eb811
#qlbaas-3b7a19b3-2a08-40bb-81bc-b76fc20108a1
#qlbaas-975da6ec-754d-4c4b-82ea-47d601ded841
#qrouter-1d26e028-f2ea-4d36-a6b8-f8f860322291
#qrouter-3c1798cc-41c4-47a0-89c4-33699988d3b1
#qrouter-3fd50377-95da-4a01-a0c5-3d613c7adb21
#qrouter-717cf868-f978-4b86-bfba-89fb1187d201
#qrouter-9afdb5a2-2bff-4083-8969-e324f081e4c1
#qrouter-a653047b-1963-44d6-9a52-ddad00e68101
```

Once you have your list log onto the agent in question and check the list against the results of the following.

```
ssh quantum-gateway-RegionOne1234 "ip netns list | sort" > /tmp/onhost
ns quantum-gateway-RegionOne1234 | sort > /tmp/required
opendiff /tmp/onhost /tmp/required
```
