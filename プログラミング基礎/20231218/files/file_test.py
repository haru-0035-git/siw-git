import sys
sys.dont_write_bytecode = True
import os

with open(f'{os.path.dirname(__file__)}\sample.txt','w') as file:     
    file.write('Hello World!')

with open(f'{os.path.dirname(__file__)}\sample.txt', 'r') as file:     
    data = file.read()
    data = data.replace("Hello", "Hi")  
with open(f'{os.path.dirname(__file__)}\sample.txt', 'w') as file:     
    file.write(data) 





with open(f'{os.path.dirname(__file__)}\sample.txt','r') as file:     
    data = file.read()     
    print(data)