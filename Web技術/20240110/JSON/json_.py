# import json
# import os
# items = [
#     {'name':'Aoki','age':30},
#     {'name':'Isida','age':32},
#     {'name':'Tori','age':29}
# ]

# with open(f'{os.path.dirname(os.path.abspath(__file__))}/test.json','w',encoding='utf-8') as fp:
#     json.dump(items,fp,indent=4)
# with open(f'{os.path.dirname(os.path.abspath(__file__))}/test.json','r',encoding='utf-8') as fp:
#     data = json.load(fp)
# print(data[0]['name'], data[0]['age']) 
# print(data[1]['name'], data[1]['age']) 


# import json, japanize_matplotlib 
# import matplotlib.pyplot as plt   
# # 人口推移のJSON ファイルを読む  
# data = json.load(open(f'{os.path.dirname(os.path.abspath(__file__))}/pop.json', encoding='utf-8'))  
# # 複数の線グラフを描画するようにデータを分割  
# x, totals, man, woman = [],[],[],[] 
# for row in data:     
#     x.append(row['year']) # 西暦年     
#     totals.append(row['total']) # 男女合計     
#     man.append(row['man']) # 男性     
#     woman.append(row['woman']) # 女性  
#     # グラフを描画 
# p_total = plt.plot(x, totals, label='合計(千人)')
# p_man = plt.plot(x, man, marker='x', label='男') 
# p_woman = plt.plot(x, woman, marker='.', label='女')
# plt.legend() # 凡例を表示 
# plt.show()


# import matplotlib.pyplot as plt 
# import json  
# # JSON データ。円グラフのための値とラベルを含む 
# data_json = '{"values": [60, 30, 10], "labels": ["A", "B", "C"]}'  
# # JSON データを解析する 
# data = json.loads(data_json)  
# # JSON データから取得した値とラベルを使用して円グラフを描画 
# plt.pie(data["values"], labels=data["labels"]) 
# plt.show()


# import json, requests, japanize_matplotlib 
# import matplotlib.pyplot as plt  
# # Web API から好きなOS に関するJSON データを取得 
# url = 'https://api.aoikujira.com/like/api.php?m=get&item_id=8' 
# r = requests.get(url)  
# # 取得したJSON をPython で扱えるように変換 
# data = json.loads(r.text)  
# # グラフ描画のためにデータを分ける 
# labels, values = [], [] 
# for it in data['answers']:     
#     labels.append(it['label'])     
#     values.append(it['point'])  
# #    グラフを描画 
# plt.barh(labels, values) 
# plt.title('好きなOS は?')  
# plt.show()