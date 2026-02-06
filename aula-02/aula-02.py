import streamlit as st

#---Titulo
st.title('Elementos Interativos de Layout')

#---Barra/menu Lateral
st.sidebar.header('Menu')

#---Adcionar uma caixa de texto ao menu
nome = st.sidebar.text_input(label='Digite o seu nome')

#---Fazer um print usando a variavel nome
st.sidebar.write(f'Olá {nome}')