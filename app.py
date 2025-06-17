import streamlit as st
import pandas as pd
import numpy as np

st.title('Deepnoteで動くStreamlitアプリ')
st.write('これはDeepnote上で実行されています！')

# ユーザー入力
user_name = st.text_input('あなたの名前を入力してください:', 'ゲスト')
st.write(f'こんにちは、{user_name}さん！')

# スライダー
num_points = st.slider('表示する点の数を選択してください:', 10, 100, 50)

# ランダムデータの生成と表示
chart_data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=['a', 'b']
)
st.subheader('ランダムデータ')
st.line_chart(chart_data)

# ボタン
if st.button('メッセージを表示'):
    st.success('ボタンがクリックされました！')

st.markdown("""
---
Created with Streamlit on Deepnote
""")
