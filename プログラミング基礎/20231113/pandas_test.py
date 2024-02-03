import pandas as pd
import os
score = pd.read_csv(f'{os.path.dirname(__file__)}\data.csv',encoding='utf-8')
print(score)