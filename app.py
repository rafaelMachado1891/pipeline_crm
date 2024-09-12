import streamlit as st
from datetime import datetime, time

def main ():
    
    st.title('Sistema de CRM e Vendas')
    email = st.text_input('Campo de texto para inserção do email do vendedor')
    data = st.date_input('Campo para inserção da data da venda', datetime.now())
    hora = st.time_input('Campo para inserção da hora da venda', value=time(9,0))
    valor = st.number_input('Campo para inserção do valor do produto', min_value=0.0, format='%.2f')
    quantidade = st.number_input('Campo para inserção da quantidade vendida', min_value=1, step= 1)
    produto = st.selectbox('Campo de seleção para escolher o produto vendido',['Zapflow com gemini', 'Zapflow com Chatgpt', 'ZapFlow com Liama'])

    if st.button('salvar'):
        data_hora = datetime.combine(data, hora)
        st.write('**dados da venda**')
        st.write(f'email do vendedor {email}')
        st.write(f'data da venda {data}')
        st.write(f'hora da venda {hora}')
        st.write(f'valor do produto {valor}')
        st.write(f'quantidade da venda {quantidade}')
        st.write(f'produto {produto}')

if __name__=="__main__":
    main()
    