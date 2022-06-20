import requests
 

url = 'https://192.168.40.251/glpi'

r = requests.get(url,verify=False)
print(r.headers.get('server'))