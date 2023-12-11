import requests 
res = requests.get('https://gihyo.jp/book') 
print(res.status_code)
