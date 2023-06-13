import math
import streamlit as st
import pandas as pd
import sqlite3

# データベース接続
conn = sqlite3.connect('messages.db')
c = conn.cursor()

# テーブル作成（存在しない場合）
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)''')

st.text("ヤッハロー")
#         ↑ガハマすこ

# 投稿データを保持するリスト
posts = []

# 投稿の作成
def create_post(title, content):
    posts.append({"title": title, "content": content})

# 投稿の表示
def show_posts():
    for post in posts:
        st.write(f"**{post['title']}**")
        st.write(post['content'])
        st.write('---')

# 掲示板アプリのタイトル
st.title("舞チャン")

# 新しい投稿の作成
st.header("新しい投稿を作成")
title = st.text_input("スレタイトル")
content = st.text_area("内容")
if st.button("作成！"):
    create_post(title, content)
    st.success("作成完了！")
 
    message:
        # メッセージをデータベースに保存
    c.execute("INSERT INTO messages (content) VALUES (?)", (message,))
    conn.commit()
        st.success('メッセージが保存されました。')

# データベースから全てのメッセージを取得
c.execute("SELECT * FROM messages")
all_messages = c.fetchall()

# メッセージの表示
st.subheader('保存されたメッセージ')
for row in all_messages:
    st.write(row[1])

# データベース接続をクローズ
conn.close()
このコードでは、messages.dbという名前のSQLiteデータベースファイルを作成し、messagesというテーブルを作成してメッセージを保存します。Streamlitアプリケーション内で、入力フォームからメッセージを入力し、「送信」ボタンを押すことで、メッセージがデータベースに保存されます。また、保存されたメッセージはアプリケーション上で表示されます。








# 投稿一覧の表示
st.header("スレタイトル一覧")
if len(posts) == 0:
    st.info("まだ投稿はありません")
else:
    show_posts()