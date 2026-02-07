import streamlit as st

# ---Titulo
st.title("Elementos Interativos de layout")

# ---Barra/menu Lateral
st.sidebar.header("Menu Lateral")

# ---Adcionar uma caixa de texto ao menu
nome = st.sidebar.text_input(label="Digite o seu nome")

if nome: #--- Adicionei uma condição para que o texto abaixo só apareça quando a string for preechida :)
    #---Em Python, se uma variável de texto estiver vazia, ela é considerada "falsa". Se tiver qualquer letra, é "verdadeira". Por isso, você pode escrever apenas assim:

    # ---Fazer um print usando a variavel nome
    st.sidebar.write(f"Olá {nome}")


# ---Coluna para organizar o conteudo principal
col1 = st.columns(
    2
)  # --- criei uma variavel e usei o comando st.columns, com valor de 2 colunas. As colunas sempre começacam no 0, da esquerda para direita.

with col1[0]:  # ---Primeira coluna
    st.header("Coluna 1")  # --- Titulo
    if st.button("Clique aqui"):  # ---Botão para clicar
        st.success("Você clicou no botão da coluna 1")  # --- Mensagem de retorno

    # ---Barra slider para escolher um valor
    valor_slider = st.slider(
        label="Escolha um valor", min_value=0, max_value=100, value=0
    )
    if valor_slider > 0:
        st.write(f"Valor selecionado: {valor_slider}")# --- print para exibir mensagem do valor selecionado.

with col1[1]:  # ---Segunda coluna
    st.header("Coluna 2")  # --- Titulo
    st.info("Esta é uma mensagem informativa")  # --- caixa fixa de mensagem informativa

    st.warning(
        "Esta é uma mensagem de atenção"
    )  # --- caixa fixa de mensagem de atenção

    # --- Você pode usar uma URL de imagem ou um caminho de um arquivo local.
    st.image(
        image=r"C:\Users\leona\Documents\GitHub\mundopython-streamlit\aula-02\key_300dp_CCDAF5_FILL0_wght400_GRAD0_opsz48.png",  # --- o 'r' inserido faz com o python considere exatamente o que esta escrito.
        caption="apenas um simbolo qualquer",  # --- um titulo/comentario sobre a imagem.
        use_container_width=True,  # --- faz com que a imagem aproveite todo o espaço da coluna que esta está.
    )

#--- Entrada de numero e exibição (barra)
num1 = st.number_input(
    label='Digite um numero',
    min_value=0,
    max_value=100
)
if num1 > 0:
    st.write(f'Valor digitado {num1}')