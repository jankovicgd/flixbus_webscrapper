import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')

print(r)

json = r.json()

for element in json:
    print(element['email'])
