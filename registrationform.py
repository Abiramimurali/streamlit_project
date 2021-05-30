
import streamlit as st,random
import pymongo,ssl
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db=client["electronic_appliances"]
col=db["sign_up"]

id=random.randint(1,100)

st.title("Sign Up")

with st.form(key='my_form'):
    name,last=st.beta_columns(2)
    name=name.text_input(" Frist Name")
    last=last.text_input(" last Name")
    email,otp=st.beta_columns([3,1])
    email=email.text_input("Mail Address")
    pw1,pw2=st.beta_columns(2)
    pw1=pw1.text_input("Create your password",type="password")
    pw2=pw2.text_input("Confirm your password",type="password")
    if(pw1!=pw2):
        st.warning("Password doesn't match!")
    ph,add=st.beta_columns([1,3])
    ph=ph.text_input("Phone number")
    add=add.text_input("location")
    c=st.checkbox("I Agree")
    
    submit_button = st.form_submit_button(label='Submit')
   

print(name,last,email,otp,pw1,pw2,ph,add)
print(submit_button)
if(submit_button):
    if(c==False):
        st.error("Please check aggree box")

if((submit_button and c) and (pw1==pw2)):
    st.success("Successfully Signedup! \nyou should verify your email address from home page -> by clicking emailverification ")
    p={"_id":id}
    p['name']=name+" "+last
    p['email']=email
    p['password']=pw2
    p['ph_no']=ph
    p['address']=add
    col.insert_one(p)


