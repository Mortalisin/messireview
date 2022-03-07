import requests
URL='https://api.rainforestapi.com/request?api_key=52A7DC0D4AB1402B9A1AE358433137AE&type=product&amazon_domain=amazon.com&asin=B073JYC4XM'
r=requests.get(url=URL)
data=r.json()
print(data)