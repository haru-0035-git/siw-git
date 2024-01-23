"""
文法： str.replace(old, new[, count])
・str :  置き換えを行う文字列。 
・old :  置き換える対象の部分文字列 
・new : old  を置き換える新しい文字列 
・count :  置き換えを行う回数（省略可）。指定しない場合は、すべての  old  が置き換えらる 
元の文字列は変更されない(非破壊)
"""
st = 'Hello world'
replaced_text = st.replace('world','Python')
print(replaced_text)