import streamlit as st #Este 'as st que usamos é para abreviar o nome do pacote e não precisa escreve-lo por extenso sempre.
import pandas
import datetime

# Configuração da página
st.set_page_config(page_title="Cadastro de Veículos", page_icon="🚗")

st.title('Seja bem vindo') # st. write substitui o print que usamos inicialmente.

st. write('Hello World! I am back!')

# Título
st.title("🚗 Cadastro de Veículos")

data_minima = datetime.date(1900, 1, 1)
data_maxima = datetime.date(2100, 12, 31)

nome = st.text_input('Qual o seu Nome?')
idade = st.number_input('Idade?', step=1, value=0, format='%d')
DtNasc = st.date_input('Nasc?',format='DD/MM/YYYY',min_value=data_minima, max_value=data_maxima)

st.write(f'olá {nome} de {idade} anos!')

st.write('Fale um pouco sobre você')
bio = st.text_area('')

# Função para validar placa (formato brasileiro Mercosul ou antigo)
def validar_placa(placa):
    if len(placa) != 7:
        return False
    # Formato Mercosul (ABC1D23) ou antigo (ABC1234)
    return (placa[:3].isalpha() and placa[3].isdigit() and 
            placa[4].isalpha() and placa[5:].isdigit()) or \
           (placa[:3].isalpha() and placa[3:].isdigit())

# Formulário de cadastro
with st.form("form_veiculo"):
    col1, col2 = st.columns(2)
    
    with col1:
        placa = st.text_input("Placa (ex: ABC1D23):", max_chars=7).upper()
        marca = st.text_input("Marca (ex: Volkswagen):")
        modelo = st.text_input("Modelo (ex: Gol):")
        ano_fabricacao = st.number_input("Ano de Fabricação:", min_value=1900, max_value=datetime.now().year)
    
    with col2:
        ano_modelo = st.number_input("Ano do Modelo:", min_value=1900, max_value=datetime.now().year + 1)
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
                "Data Cadastro": datetime.now().strftime("%d/%m/%Y %H:%M")
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