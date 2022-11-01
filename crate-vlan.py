import json
import routeros_api


url = '10.10.10.1'
username='admin'
password='admin'
port = 8728 # MIKORTIK API PORT


conn = routeros_api.RouterOsApiPool(host=url, username=username, password=password, port=port, plaintext_login=True) 
api = routeros_api.connect
api = conn.get_api()

#create new vlan
get_vlan = api.get_resource('interface/vlan/')
get_vlan.add(name='office', comment='staff only', vlan_id='20', interface='ether1')

#Get vlan info
show_vlan = get_vlan.get()
print(json.dumps(show_vlan, indent=3))

conn.disconnect()