import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np
import plotly.express as px
cluster = MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["electronic_appliances"]
c=db["confirmed_ticket"]
n = c.find()
#l=[n[i] for i in range(n.count())]
n = [i['date'] for i in list(n)]
print(n)
df=pd.DataFrame(n)
print(df)
#st.title("Products graph")
#n_count = {'Air Conditioner': n.count('Air Conditioner'), 'Mobile': n.count('Mobile'), 'Heater': n.count('Heater')}
#fig = px.pie(df,values=list(n_count.values()), names=list(n_count.keys()), title='sale')
#st.plotly_chart(fig)

st.title("Products date graph")
n_count={'date':n.count('06/01/2021')}
fig = px.pie(df,values=list(n_count.values()), names=list(n_count.keys()), title='sale')
st.plotly_chart(fig)
        

