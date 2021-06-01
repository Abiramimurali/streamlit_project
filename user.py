import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
cluster = MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["electronic_appliances"]
c=db["user_details"]

st.header("Users")
n = c.find()
l=[]
for i in range(n.count()):
    d=n[i]
    l.append(d)
df=pd.DataFrame(l)
st.dataframe(df.head(10))
