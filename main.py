import requests
 

url = 'https://0.0.0.0/glpi'

r = requests.get(url,verify=False)
print(r.headers.get('server'))