import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
cluster = MongoClient("mongodb+srv://shalini:Shalu18#@cluster0.pfjfc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["demo"]
c=db["store details"]

st.title("Admin Page")
st.header("Add Products")

with st.form(key="my_form"):
    number,name,price,stock= st.beta_columns(4)

    p_id=number.text_input("Enter Product id")
    p_name=name.text_input("Enter Product name")
    p_cost=price.text_input("Enter Price")
    p_stock=stock.text_input("Enter Stock details")
    
    discription=st.text_input("Enter description")
    brand,bl=st.beta_columns(2)
    brand=brand.text_input("Enter Brand")

    ch,ch1,bl,sub = st.beta_columns(4)
    Add=ch.checkbox("I Agree")
    submit=sub.form_submit_button("Add")
print(p_id,p_name,p_cost,p_stock,discription,brand,Add,submit)

if (p_stock and Add!=True):
    st.error("Check Add Box")
if(submit and Add==True):
    
    post={}
    post["p_id"]=p_id
    post["p_name"]=p_name
    post["p_cost"]=p_cost
    post["p_stock"]=p_stock
    post["discription"]=discription
    post["brand"]=brand
    post["ratings"]={}
    post["reviews"]={}
    c.insert_one(post)
    st.success("Products Successfully Added")


st.header("Products Display")
n = c.find()
l=[]
for i in range(n.count()):
    d=n[i]
    l.append(d)
df=pd.DataFrame(l)
st.dataframe(df.head(10))
    
     

st.header("Delete Products")
with st.form(key="second_form"):
    number,name = st.beta_columns(2)
    p_id=number.text_input("Enter Product id you want to delete")
    p_name=name.text_input("Enter Product name you want to delete")

    ch,bl,sub = st.beta_columns(3)
    Delete=ch.checkbox("I Agree")
    submit=sub.form_submit_button("Delete")
print(p_id,p_name,Delete,submit)

if (p_name and Delete!=True):
    st.error("Check delete Box")
if(submit and Delete==True):
    st.success("Products Successfully Deleted")
post={}
post["p_id"]=p_id
post["p_name"]=p_name
c.delete_one({"p_id":p_id})

st.header("Modify Products")
with st.form(key="Third_form"):
    number,price,stock = st.beta_columns(3)
    p_id=number.text_input("Enter Product id")
    p_cost=price.text_input("Enter Product price")
    p_stock=stock.text_input("Enter Stock details")

    ch,bl,sub = st.beta_columns(3)
    Modify=ch.checkbox("I Agree")
    submit=sub.form_submit_button("Update")
print(p_id,p_cost,p_stock,Modify,submit)

if (p_stock and Modify!=True):
    st.error("Check modify Box")
if(submit and Modify==True):
    st.success("Products Successfully Modified")

post={}
post["p_id"]=p_id
post["p_cost"]=p_cost
post["p_stock"]=p_stock
c.update_one({'p_id':p_id},{'$set':{'p_cost':p_cost,'p_stock':p_stock}})

    
