import streamlit as st

import pandas as pd
import numpy as np

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.title ('Panel de Covid-19 ')

st.markdown ('El panel visualizará la situación de Covid-19 en el mundo')

st.markdown ('La enfermedad por coronavirus (COVID-19) es una enfermedad infecciosa causada por un coronavirus recién descubierto. La mayoría de las personas infectadas con el virus COVID-19 experimentarán una enfermedad respiratoria leve a moderada y se recuperarán sin requerir un tratamiento especial. \nEsta aplicación le brinda el análisis de impacto en tiempo real de los casos confirmados, fallecidos, activos y recuperados de COVID-19')

st.sidebar.title ('Selector de visualización')

st.sidebar.markdown ('Seleccione los gráficos que desea visualizar')



DATA_URL=('covid_19_india.csv')
@st.cache(persist=True)

def load_data():
    data=pd.read_csv(DATA_URL)
    return data

df=load_data()


st.sidebar.checkbox("Análisis por País ", True, key=1)
# select = st.sidebar.selectbox('Selecciona el País',df['State/UnionTerritory'].unique())

select = st.sidebar.selectbox('Selecciona el País',df['State/UnionTerritory'])

#get the state selected in the selectbox
state_data = df[df['State/UnionTerritory'] == select]
select_status = st.sidebar.radio("Estado del paciente", ('Confirmed',
'Cured', 'Deaths'))


def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Estatus':['Confirmed', 'Cured', 'Deaths'],
    'Numero de casos':(dataset.iloc[0]['Confirmed'],
    dataset.iloc[0]['Cured'], 
    dataset.iloc[0]['Deaths'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("Analisis por estado", True, key=2):
    st.markdown("## **Analisis por estado**")
    st.markdown("### Casos confirmados, muertos y curados  %s en" % (select))
    if not st.checkbox('Mostrar gráfica', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='Estatus',
        y='Numero de casos',
        labels={'Numero de casos':'Numero de casos en %s' % (select)},
        color="Estatus")
        st.plotly_chart(state_total_graph)


def get_table():
    datatable = df[['State/UnionTerritory', 'Confirmed', 'Cured', 'Deaths']]
    #datatable = datatable[datatable['State/UnionTerritory'] != 'State Unassigned']
    return datatable

datatable = get_table()
st.markdown("### Covid-19 cases in India")
st.markdown("The following table gives you a real-time analysis of the confirmed, active, recovered and deceased cases of Covid-19 pertaining to each state in India.")
#st.dataframe(datatable) # will display the dataframe
st.table(datatable)# will display the table

