import streamlit as st #Este 'as st que usamos é para abreviar o nome do pacote e não precisa escreve-lo por extenso sempre.
import pandas as pd
from datetime import datetime, date
import datetime
import json

st.set_page_config(page_title="Cadastro de Veículos", page_icon="🚗")

# Nome do arquivo JSON
ARQUIVO_DADOS = 'carro.json'

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
        return{}
    
def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_veiculos(placa, marca, modelo, ano_de_fabricacao, ano_modelo, cor,tipo_veiculo, combustivel, date_cadastro):
    return{
        "Placa": placa,
                    "Marca": marca,
                    "Modelo": modelo,
                    "Ano Fabricação": ano_de_fabricacao,
                    "Ano Modelo": ano_modelo,
                    "Cor": cor,
                    "Tipo": tipo_veiculo,
                    "Combustível": combustivel,
                    "Data Cadastro": date_cadastro
    }

# Função para validar placa (formato brasileiro Mercosul ou antigo)
def validar_placa(placa):
    if len(placa) != 7:
        return False
    # Formato Mercosul (ABC1D23) ou antigo (ABC1234)
    return (placa[:3].isalpha() and placa[3].isdigit() and 
            placa[4].isalpha() and placa[5:].isdigit()) or \
           (placa[:3].isalpha() and placa[3:].isdigit())


def cadastrar_veiculos():
    # Configuração da página
    

    st.title('Seja bem vindo') # st. write substitui o print que usamos inicialmente.

    st.write('Hello World! I am back!')

    # Título
    st.title("🚗 Cadastro de Veículos")

    data_minima = datetime.date(1900, 1, 1)
    data_maxima = datetime.date(2100, 12, 31)

    nome = st.text_input('Qual o seu Nome?')
    cpf = st.text_input('Qual o seu CPF?')
    rg = st.text_input('Qual o seu RG?')
    idade = st.number_input('Idade?', step=1, value=0, format='%d')
    DtNasc = st.date_input('Nasc?',format='DD/MM/YYYY',min_value=data_minima, max_value=data_maxima)

    st.write(f'olá {nome} de {idade} anos!')

    st.write('Fale um pouco sobre o seu veiculo')
    bio = st.text_area('')


    # Formulário de cadastro
    with st.form("form_veiculo"):
        col1, col2 = st.columns(2)
        
        with col1:
            placa = st.text_input("Placa (ex: ABC1D23):", max_chars=7, key='user_input', on_change=to.upper).upper()
            marca = st.text_input("Marca (ex: Volkswagen):")
            modelo = st.text_input("Modelo (ex: Gol):")
            ano_fabricacao = st.number_input("Ano de Fabricação:", min_value=1900, max_value=2120)


        with col2:
            ano_modelo = st.number_input("Ano do Modelo:", min_value=1900, max_value=2120)
            cor = st.selectbox("Cor:", ["Branco", "Preto", "Prata", "Vermelho", "Azul", "Outro"])
            tipo_veiculo = st.selectbox("Tipo:", ["Carro", "Moto", "Caminhão", "SUV", "Van"])
            combustivel = st.selectbox("Combustível:", ["Gasolina", "Álcool", "Diesel", "Flex", "Elétrico", "Híbrido"])

        # Validação e submissão
        submitted = st.form_submit_button("Cadastrar Veículo")
        if submitted:
            if not all([placa, marca, modelo]):
                st.error("Preencha os campos obrigatórios (Placa, Marca, Modelo)!")
            elif not validar_placa(placa):
                st.error("Placa inválida! Use o formato ABC1D23 ou ABC1234.")
            else:
                # Criar DataFrame (ou salvar em banco de dados)
                novo_veiculo = pd.DataFrame([{
                    "Placa": placa,
                    "Marca": marca,
                    "Modelo": modelo,
                    "Ano Fabricação": ano_fabricacao,
                    "Ano Modelo": ano_modelo,
                    "Cor": cor,
                    "Tipo": tipo_veiculo,
                    "Combustível": combustivel,
                    "Data Cadastro": "2025"
                }])

                # Salvar em CSV (para exemplo)
                try:
                    with open("veiculos.csv", "a") as f:
                        novo_veiculo.to_csv(f, header=f.tell()==0, index=False, sep=";")
                    st.success("Veículo cadastrado com sucesso!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Erro ao salvar: {e}")

        # Mostrar dados cadastrados (opcional)
        if st.checkbox("Visualizar veículos cadastrados"):
            try:
                veiculos_df = pd.read_csv("veiculos.csv", sep=";")
                st.dataframe(veiculos_df)
            except FileNotFoundError:
                st.warning("Nenhum veículo cadastrado ainda.")

def listar_veiculos():
    pass

def editar_veiculos():
    pass

def excluir_veiculos():
    pass

# menu lateral
st.sidebar.title('Menu')
opcao = st.sidebar.radio('Selecione uma opção:', ('Cadastrar Veiculos', 'Listar Veiculos', 'Editar Veiculos', 'Excluir Veiculos'))

#Navegação entre páginas
if opcao == 'Cadastrar Veiculos':
    cadastrar_veiculos()
elif opcao == 'Listar Veiculos':
    listar_veiculos()
elif opcao == 'Editar Veiculos':
    editar_veiculos()
elif opcao == 'Excluir Veiculos':
    excluir_veiculos()

# Rodapé
st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Artur')
st.sidebar.markdown(f'Total de veiculos:')

