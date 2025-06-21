import requests
url = "https://jwt-ei3z.onrender.com/api/oauth_guest?uid=3987815200&passwordB17E6BB8C9046D75DE76146FD7730470BB94AE42EA37D40D5C22313689E874F6"
get = requests.get(url).json()
data = get["token"]
print(data)
