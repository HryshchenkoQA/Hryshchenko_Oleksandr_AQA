from requests import get
url = 'https://reqres.in'
headers = {
    "ContentType": "application/json"
}
responsee = get(url + "api/users?page=2", headers=headers)
print(responsee.json())
