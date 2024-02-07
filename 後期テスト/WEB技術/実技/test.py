import streamlit as st
from  PIL import Image
import os
import time
code = """
サフランで風味付けしたスペインの米料理。
米と具（魚介・鶏肉など）をオリーブ油で炒(いた)め、スープで炊き上げる。
パエリアの起源は、スペインに稲作をもたらしたアラブ人に由来する。
紀元9世紀以後、アル＝アンダルスのムスリムの間で作られてきた。
ピラフと同様にその歴史は古い。
"""
st.title('今日の料理')
st.header('パエリア')
image = Image.open(f'{os.path.dirname(__file__)}/ダウンロード.jpg')
st.image(image,width=200)
st.write(code)
number = st.text_input('注文数')
submit_btn = st.button('注文') 
cancel_btn = st.button('戻る')
if submit_btn:
    st.write(f'パエリア{number}個、注文されました')
    text = st.text('調理中...')
    time.sleep(5)
    text = st.text('料理が完成しました!!')
elif cancel_btn:
    st.write('キャンセルされました')