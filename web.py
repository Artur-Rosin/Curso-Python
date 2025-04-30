import streamlit as st

st.title('Hello World') # st. write substitui o print que usamos inicialmente.

st. write('Hello World! I am back!')

nome = st.text_input('Qual o seu Nome?')
idade = st.number_input('Idade?', step=1, value=0, format='%d')
Dtnasc = st.date_input('Nasc?')
st.write(f'olá {nome} de {idade} anos!')

st.write('Fale um pouco sobre você')
bio = st.text_area('')
