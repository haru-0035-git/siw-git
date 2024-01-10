import json
import os
items = [
    {'name':'Aoki','age':30},
    {'name':'Isida','age':32},
    {'name':'Tori','age':29}
]

with open(f'{os.path.dirname(os.path.abspath(__file__))}/test.json','w',encoding='utf-8') as fp:
    json.dump(items,fp,indent=4)
with open(f'{os.path.dirname(os.path.abspath(__file__))}/test.json','r',encoding='utf-8') as fp:
    data = json.load(fp)
print(data[0]['name'], data[0]['age']) 
print(data[1]['name'], data[1]['age']) 


