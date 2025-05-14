import streamlit as st #Este 'as st que usamos é para abreviar o nome do pacote e não precisa escreve-lo por extenso sempre.
import pandas as pd
from datetime import datetime, date
import datetime
import json

st.set_page_config(page_title="Portal do entregador", page_icon="🚗")

# Nome do arquivo JSON
ARQUIVO_DADOS = 'entregador.json'

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
        return{}
    
def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_veiculos():
    return

# Função para validar placa (formato brasileiro Mercosul ou antigo)
def validar_placa():
        return


def cadastrar_veiculos():
    # Configuração da página
    

    st.title('Seja bem vindo') # st. write substitui o print que usamos inicialmente.

    st.write('Hello World! I am back!')

    # Título
    st.title("🚗 Portal do entregador")

def listar_veiculos():
    pass

def editar_veiculos():
    pass

def excluir_veiculos():
    pass

# menu lateral
st.sidebar.title('Menu')
opcao = st.sidebar.radio('Selecione uma opção:', ('Arrumar Celular e Acessórios', 'Arrumar Rodas', 'Borracheiro', 'Costureira', 'Guicho', 'Lojas'))

#Navegação entre páginas
if opcao == 'Arrumar Celular e Acessórios':
    cadastrar_veiculos()
elif opcao == 'Arrumar Rodas':
    listar_veiculos()
elif opcao == 'Borracheiro':
    editar_veiculos()
elif opcao == 'Costureira':
    excluir_veiculos()
elif opcao == 'Guicho':
    excluir_veiculos()
elif opcao == 'Lojas':
    excluir_veiculos()

# Rodapé
st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Artur')
#st.sidebar.markdown(f'Total de veiculos:')

