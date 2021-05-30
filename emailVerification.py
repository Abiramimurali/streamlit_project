import streamlit as st,random,smtplib
import pymongo,ssl
from pymongo import MongoClient
gen1=0
client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db=client["electronic_appliances"]
c1=db["user_details"]
c2=db['sign_up']
otp1=db['email_ver_otp']
st.title("email_verification")

def verification(to):
   
    global gen1
    otp1.remove()
    fromaddr = 'abirami.prodapt@gmail.com'
    gen1=str(random.randint(1000,9999))
    x={}
    x['email']=to
    x['otp']=gen1
    otp1.insert_one(x)
    msg = 'Your 4 digit otp is '+str(gen1)
    username = 'abirami.prodapt@gmail.com'  
    password = 'Abirami103$'
    server = smtplib.SMTP('smtp.gmail.com',587)  
    server.starttls()
    server.login(username, password)  
    server.sendmail(fromaddr,to, msg)  
 

with st.form(key='email_verification'):
    email=st.text_input("Email Address")
    check=st.form_submit_button("generate otp for verify your email address")
if (check):
    verification(email)
with st.form(key='my-form'):
    st.info("Please check your email & enter the 4 digit pin")
    otp=st.text_input("OTP")
    st.text(gen1)
    submit_button = st.form_submit_button(label='Submit')

    f = otp1.find({})
    f = f[0]['otp']

print(otp,submit_button)

if(otp==f) and (submit_button) :


   
    copy=otp1.find_one()
    print("copy",copy)
    for i in copy:
        a1=i['email']
    print("a1",a1)
    a2=c2.find_one({'email':a1})
    print("a2",a2)
    c1.insert_one(a2)
    c2.delete_one({'email':a1})
    st.success("Email verified!")
elif(submit_button) and (otp!=f):
    st.error("Incorrect otp!")