import requests

response = requests.get("https://dog.ceo/api/breeds/list/all")
print(response)