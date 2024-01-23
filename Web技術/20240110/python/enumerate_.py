# iterable = ['a', 'b', 'c']  
# for index, value in enumerate(iterable):     
#     print(index, value) 

# iterable = ['a', 'b', 'c'] 
# for index, value in enumerate(iterable, start=1):
#     print(index, value)

def find_person(people,target):
    found = False
    for i,person in enumerate(people):
        if person ==  target:
            print(f'{target}が i=={i}で見つかりました')
            found = True
            continue
        if not found:
            print(f"{target} はここでは見つかりませんでした。")  
find_person(['Wilma', 'Woof', 'Wally'], 'Wally') 
find_person(['Wenda', 'Odlaw', 'WatcherA', 'WatcherB'], 'Whitebeard') 