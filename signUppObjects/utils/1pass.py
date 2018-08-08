import requests

url = 'http://127.0.0.1:8000/login/'
d = {'username': 'xxd', 'password': 'xxd12345'}
headers = {'Authorization':'9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'}
r = requests.post(url,data=d)
print(r.text)