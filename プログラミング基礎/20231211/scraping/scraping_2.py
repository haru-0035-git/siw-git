import requests 
res = requests.get('https://gihyo.jp/book') 
print(res.status_code)

html_doc = res.text
print(html_doc[:300])