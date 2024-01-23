# class Person:     
#     def __init__(self, name, age):         
#         self.name = name         
#         self.age = age      
#     def __str__(self):         
#         return f"名前: {self.name}, 年齢: {self.age}"

# person = Person("太郎", 30) 
# print(str(person))  # 名前: 太郎, 年齢: 30 
# print(person)       # 名前: 太郎, 年齢: 30

# def find_person(people, target):     
#     found = False     
#     for i, person in enumerate(people):         
#         if person == target:             
#             print(f"{target}がi == {i}で見つかりました。")             
#             found = True             
#             break       
#     else:             
#         print(f"{target} は見つかりませんでした。")  


# find_person(['Wilma', 'Woof', 'Wally'], 'Wally') 
# find_person(['Wenda', 'Odlaw', 'WatcherA', 'WatcherB'], 'Whitebeard') 

# date_parts = ['2024', '01', '15'] 
# date_string = '/'.join(date_parts) 
# print(date_string)


# def to_binary_str(num):     
#     digit_list = []
#     while num >0:         
#         digit_list.append(str(num%2))        
#         num = int(num / 2)     
#     digit_list.reverse()     
#     return ''.join(digit_list)  
# print(to_binary_str(19))

# def reverse_string(s):     
#     if len(s) <= 1:         
#         return s     
#     else:         
#         return reverse_string(s[1:]) + s[0]
# print(reverse_string('hello')) 
 

# def format_float(number):     
#     if type(number) is not float:         
#         raise TypeError("引数のタイプはfloat ではありません")
#     number = str(number)     
#     integer_part, float_part = number.split(".")     
#     return ",".join([integer_part, float_part[0:3]])  
# print(format_float(3.1415926536)) 
# print(format_float(1.5))
# print(format_float(1))

