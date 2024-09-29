import streamlit as st
from datetime import datetime,time
from contrato import Vendas, ProdutoEnum
from pydantic import ValidationError


def main ():
    
    st.title('Sistema de CRM e Vendas')
    email = st.text_input('Campo de texto para inserção do email do vendedor')
    data = st.date_input('Campo para inserção da data da venda', datetime.now())
    hora = st.time_input('Campo para inserção da hora da venda', value=time(9,0))
    valor = st.number_input('Campo para inserção do valor do produto', min_value=0.0, format='%.2f')
    quantidade = st.number_input('Campo para inserção da quantidade vendida', min_value=1, step= 1)
    produto = st.selectbox("Produto", options=[e.value for e in ProdutoEnum])

    if st.button('salvar'):
        try: 
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor, 
                quantidade = quantidade, 
                produto = produto
            )

            st.write(venda)
        except ValidationError as e:
            st.error(f'Erro {e}')

if __name__=="__main__":
    main()
    