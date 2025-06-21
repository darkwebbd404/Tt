import requests
url = "https://projects-fox-x-get-jwt.vercel.app/get?3805642913=&password=BB43313F3419F8961BABF036994BD8DE638E20AE9FEB59348318B93056725DF8"
get = requests.get(url).json()
data = get["token"]
print(data)
