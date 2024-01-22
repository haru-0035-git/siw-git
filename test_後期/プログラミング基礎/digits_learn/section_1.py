from sklearn.datasets import load_digits 
digits = load_digits()  
#データの出力
print(digits.data) 
print(digits.data.shape) 
print(digits.target) 
print(digits.target_names)