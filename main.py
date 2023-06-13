import math
import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('messages.db')
c = conn.cursor()

# ↑データベース接続

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
        # メッセージをデータベースに保存
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


# 投稿一覧の表示
st.header("スレタイトル一覧")
if len(posts) == 0:
    st.info("まだ投稿はありません")
else:
    show_posts()

    import streamlit as st
import pandas as pd

# メッセージを保存するデータフレーム
messages_df = pd.DataFrame(columns=['User', 'Message'])

def main():
    st.title("掲示板アプリ")

    # 新しいメッセージの入力
    user = st.text_input("ユーザー名")
    message = st.text_area("メッセージ")

    # 送信ボタンがクリックされた場合
    if st.button("送信"):
        if user and message:
            add_message(user, message)
            st.success("メッセージが追加されました！")

    # 保存されたメッセージの表示
    if not messages_df.empty:
        st.subheader("保存されたメッセージ")
        st.dataframe(messages_df)

def add_message(user, message):
    # メッセージをデータフレームに追加
    messages_df.loc[len(messages_df)] = [user, message]

if __name__ == '__main__':
    main()
