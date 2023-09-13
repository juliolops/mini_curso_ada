import streamlit as st
import pandas as pd


st.title("EXEMPLO STREAMLIT:")


df = pd.DataFrame({"A":[10,20,10,20,30,40,50,10,20],
                   "B":[11,25,15,25,32,41,13,16,22],
                   "C":[12,22,11,25,32,11,15,11,22],})



st.header("DATAFRAME PLOT:")
st.table(df)


options_reasons = st.selectbox(
    'COLUNAS DATAFRAME',
     list(df.columns))


st.header("MÉTRICAS GERAIS:")

col1, col2, col3  = st.columns(3)

col1.metric("Média",f'{round(df[options_reasons].mean(),2)}' )
col2.metric("Soma", f'{round(df[options_reasons].sum(),2)}')
col3.metric("Máximo", f'{round(df[options_reasons].max(),2)}')



col4, col5, col6  = st.columns(3)

col4.metric("Mínimo",f'{round(df[options_reasons].min(),2)}')
col5.metric("Mediana", f'{round(df[options_reasons].median(),2)}')
col6.metric("Desvio Padrão",f'{round(df[options_reasons].std(),2)}')
