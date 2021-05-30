import streamlit as st
import pymongo,ssl



client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db=client["electronic_appliances"]
col=db["user_details"]
st.title("Login")

email=st.text_input("Email address")
pw=st.text_input("Password")
submit=st.button("login")
c=st.button("Forgot password")
a=col.find({'email':email})
a=list(a)
if a:
    if(submit) and (a[0]['password']!=pw):
        st.error("Invalid password")
    elif(submit) and (a[0]['password']==pw):
        st.success("successfully logged in")
elif(submit)and (a!=None):
    st.error("Invalid email address! Please sign up")

if(c):
        st.info("You can change the password by clicking -> Home choose -> Forgot password")


