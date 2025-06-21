import requests
url = "https://projects-fox-x-get-jwt.vercel.app/get?uid=&password="
get = requests.get(url).json()
data = get["token"]
print(data)