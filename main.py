import streamlit as st
import pandas as pd

st.title('掲示板アプリ')

messages = pd.DataFrame({'ユーザー': ['ユーザーA', 'ユーザーB'], 'メッセージ': ['こんにちは！', 'Streamlit楽しいですね！']})

st.table(messages)

new_message = st.text_input('新しいメッセージを入力してください')
submit_button = st.button('送信')

if submit_button:
    messages = messages.append({'ユーザー': '新規投稿', 'メッセージ': new_message}, ignore_index=True)
    st.table(messages)
