import collections
import streamlit as st
import pymongo,ssl,random,re,smtplib
from pymongo import MongoClient
gen1=0
client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db=client["electronic_appliances"]
col=db["user_details"]
otpcollection = db['otp']
st.title("Forgot_password")
def verification(to):
    global gen1
    otpcollection.remove()
    fromaddr = 'abirami.prodapt@gmail.com'
    gen1=str(random.randint(1000,9999))
    otpcollection.insert_one({'otp': gen1})
    msg = 'Your 4 digit otp is '+str(gen1)
    username = 'abirami.prodapt@gmail.com'  
    password = 'Abirami103$'
    server = smtplib.SMTP('smtp.gmail.com',587)  
    server.starttls()
    server.login(username, password)  
    server.sendmail(fromaddr,to, msg)  
with st.form(key='my_form'):
    email=st.text_input("Email address")
    c=st.form_submit_button("Generate otp")
if c:   
    verification(email)
with st.form(key='myform'):
    otp=st.text_input("OTP")

    st.info("Please check your email & enter the 4 digit pin")
    p1=st.text_input("Create password")
    p2=st.text_input("Confirm password")
    submit=st.form_submit_button("submit")
firstotp = list(otpcollection.find({}))
firstotp = firstotp[0]['otp']
if(otp!=firstotp) and (submit):
    st.warning("Incorrect OTP")
elif(p1!=p2) and (submit):
    st.warning("Password doesn't match!")
elif (submit):
    st.success("Password changed!")
    a=col.find({'email':email})
    a=list(a)
    pw=p2
    col.update_one({'email':email},{'$set':{'password':pw}})

