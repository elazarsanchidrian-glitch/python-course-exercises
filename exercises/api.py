import requests

response = requests.get("https://dog.ceo/api/breeds/about/list/all")
print(response)
print(response.json())
print(response.status_code)