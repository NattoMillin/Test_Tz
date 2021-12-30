import streamlit as st
from time import sleep

st.title('Streamlit New')
st.write('Interractive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右にカラムを表示')

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f'Uteratuin {i + 1}')
    bar.progress(i + 1)
    sleep(0.01)

if button:
    right_column.write('ここに表示')

expamder1 = st.expander('問い合わせ1')
expamder1.write('問い合わせ内容')