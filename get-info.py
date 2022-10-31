import json
import routeros_api


url = '10.10.10.1'
username='admin'
password='admin'
port = 8728 # MIKORTIK API PORT


# response = requests.post(url,data=json.dumps(payload), headers=myheaders, auth=(username,password,port)).json()
conn = routeros_api.RouterOsApiPool(host=url, username=username, password=password, port=port, plaintext_login=True) 
api = routeros_api.connect
api = conn.get_api()

#GET IP ADDRESS
get_ip = api.get_resource('ip/address/')
show_ip = get_ip.get()

#GET Interfaces
get_int = api.get_resource('interface/')
show_int = get_int.get()

print(json.dumps(show_ip, indent=3))
print(json.dumps(show_int, indent=3))

conn.disconnect()