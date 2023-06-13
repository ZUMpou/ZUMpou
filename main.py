import math
import streamlit as st
import pandas as pd
import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect('data.db')
c = conn.cursor()

# テーブルの作成（初回のみ実行）
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)''')
conn.commit()

# データベースからメッセージを取得して表示
c.execute("SELECT * FROM messages")
result = c.fetchall()
for row in result:
    st.write(row[1])

# データベースの接続をクローズ
conn.close()


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

# 投稿一覧の表示
st.header("スレタイトル一覧")
if len(posts) == 0:
    st.info("まだ投稿はありません")
else:
    show_posts()

if st.button("保存"):
    c.execute("INSERT INTO messages (message) VALUES (?)", (message,))
    conn.commit()
    st.success("メッセージが保存されました")

# データベースからメッセージを取得して表示
c.execute("SELECT * FROM messages")
result = c.fetchall()
for row in result:
    st.write(row[1])

# データベースの接続をクローズ
conn.close()

# メッセージをデータベースに保存
if st.button("保存"):
    c.execute("INSERT INTO messages (message) VALUES (?)", (message,))
    conn.commit()
    st.success("メッセージが保存されました")