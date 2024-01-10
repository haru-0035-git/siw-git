import matplotlib.pyplot as plt  
import json,japanize_matplotlib 
import os
# values = [60, 30,10] 
# labels = ['A', 'B', 'C'] 
# plt.pie(values, labels=labels) 
# plt.show() 

data = json.load(open(f'{os.path.dirname(os.path.abspath(__file__))}/pop.json',encoding='utf-8'))
# 複数の線グラフを描画するようにデータを分割  
x, totals, man, woman = [],[],[],[] 
for row in data:     
    x.append(row['year']) 
    # 西暦年     
    totals.append(row['total']) 
    # 男女合計     
    man.append(row['man']) 
    # 男性     
    woman.append(row['woman']) 
    # 女性  
# グラフを描画 
p_total = plt.plot(x, totals, label='合計(千人)') 
p_man = plt.plot(x, man, marker='x', label='男') 
p_woman = plt.plot(x, woman, marker='.', label='女') 
plt.legend() # 凡例を表示  
plt.show() 