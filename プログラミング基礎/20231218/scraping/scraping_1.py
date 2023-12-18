from bs4 import BeautifulSoup
import requests 
res = requests.get('https://book.impress.co.jp/books/1118101169') 
# print(res.status_code)

html_doc = res.text 
# print(html_doc[:700])

soup = BeautifulSoup(html_doc,'html.parser')

div_book_detail = soup.find('div', class_='block-book-detail')
book_title = div_book_detail.find('h2') 
print(book_title.get_text())

book_price = div_book_detail.find('p', class_='module-book-price') 
print(book_price.get_text())

dl_book_data = div_book_detail.find('dl', class_='module-book-data') 
book_data = {} 
for tag in dl_book_data.find_all(['dt', 'dd']):     
    if tag.name == 'dt':         
        key = tag.get_text()     
    if tag.name == 'dd':         
        book_data[key] = tag.get_text().strip()  
print('発売日：', book_data['発売日']) 
print('著者', book_data['著者'])