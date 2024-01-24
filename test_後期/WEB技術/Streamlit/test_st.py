import streamlit as st
from  PIL import Image
import os
code = """
import streamlit as st 
st.title('ABC')
"""
st.code(code,language='python') 
image = Image.open(f'{os.path.dirname(__file__)}/digi.jpeg')
st.image(image,width=200)

video_file = open(f'{os.path.dirname(__file__)}/aaa.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)

name = st.text_input('名前')
print(name)
# submit_btn = st.button('送信') 
# cancel_btn = st.button('キャンセル') 
# print(f'submit_btn: {submit_btn}') 
# print(f'cancel_btn: {cancel_btn}')
# submit_btn = st.button('送信')
# cancel_btn = st.button('キャンセル')
# if submit_btn:
#         st.text(f'こんにちは！{name}さん！') 

with st.form(key='profile_form'):
    #textbox
    name = st.text_input('名前')
    address = st.text_input('住所')
    print(name)
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'こんにちは！{name}さん！郵送先は{address}ですね')

with st.form(key='profile_form_2'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    # セレクトボックス
    age_category = st.selectbox('年齢層', ('子供', '大人'))
    hobby = st.multiselect('趣味', ('スポーツ','読書','映画'))
    # 送信ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'こんにちは！{name}さん！郵送先は{address}ですね。') 
        st.text(f'年齢層: {age_category}') 
        st.text(f'趣味：{",".join(hobby)}')
    if cancel_btn:     
        st.text('キャンセルされました。')