import requests

url = "https://api.api-ninjas.com/v1/animals?name=cheetah"
xApiKey = 'IoHiDsq59vVzdV0benC0Az6w6CPmlqxZ3db1xpnI'

response = requests.get(url, headers={'X-Api-Key': xApiKey})
print(response.json())