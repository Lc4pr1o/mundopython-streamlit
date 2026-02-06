# --- Importar o Streamlit --- #
import streamlit as st

# --- Título principal da página --- #
st.title('Bem-Vindo!')

# --- Cabeçalho --- #
st.header('Esta é a minha primeira aplicaão com Streamlit')

# --- Subcabeçalho --- #
st.subheader('Vamos explorar essa ferramenta incrível!')

# --- Texto genérico --- #
st.write('Este é um **texto** simples usando o st.write()') # O st.write() tambem aceita comandos em markdown




# --- Texto formatado com Markdown --- #
st.markdown('''
Este é um exemplo de **Markdown** no Streamlit.
Podemos usar **negrito**, *itálico* e até mesmo **listas**:
* Item 1
* Item 2
''')

# --- Texto literal --- #
st.text('Este é um texto puro, sem formatação.')