
import streamlit as st
import pymongo,ssl


client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db=client["electronic_appliances"]
col=db["user_details"]


st.title("Profile")


st.markdown("""
<html>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Acme&display=swap" rel="stylesheet">
    <style>
        .user
        {
            background: #DEFFFD;
            background: -webkit-linear-gradient(right, #DEFFFD, #D6DFFF);
            background: -moz-linear-gradient(right, #DEFFFD, #D6DFFF);
            background: linear-gradient(to left, #DEFFFD, #D6DFFF);
			position: absolute;
			top: -30px;
			right: 0px;
            height: 40px;
            padding-left: 7px;
            padding-right: 7px;
            border-radius: 8px;
            border: 0.25px solid;
		}
        .username
        {
            font-family: 'Acme', sans-serif;
            font-size: 20px;
            line-height: 40px;
        }
    </style>
    <div class = 'user'>
        <p class = 'username'>Logged in as %s</p>
    </div>
</html>

"""%'user', unsafe_allow_html=True)

n=col.find({'email':'abiramimurali103@gmail.com'})
n=list(n)
print(n)
name1=n[0]['name']
pw1=n[0]['password']
ph1=n[0]['ph_no']
loc1=n[0]['address']
name=st.write("NAME : "+name1.upper())
pw=st.write("PASSWORD : "+pw1)
ph=st.write("PHONE NUMBER : "+ph1)
loc=st.write("ADDRESS : "+loc1.upper())
p={}

st.markdown("""<html>
    <style>
    .order-cancel
    {
        background: #DEFFFD;
        background: -webkit-linear-gradient(right, #DEFFFD, #D6DFFF);
        background: -moz-linear-gradient(right, #DEFFFD, #D6DFFF);
        background: linear-gradient(to left, #DEFFFD, #D6DFFF);
        font-family: 'Acme', sans-serif;
        font-size: 19px;
        line-height: 40px;
        border: 1px solid #515a5e;
        border-radius: 7px;
        text-align: center;
    }
    </style>
    <p class = 'order-cancel'>Here you can change your profile details </p>
    </html>
    """, True)
with st.form(key='my_form'):
    name=st.text_input("Name")
    st.write("Email address")
    st.info(n[0]['email'])
    pw=st.text_input("Password",type='password')
    ph=st.text_input("phone number")
    add=st.text_input("Address")
    ch=st.form_submit_button("change profile")

if(ch):
    st.success("Profile details changed successfully!")
    p['name']=name1 if (name==None) or (name=='') else name
    p['password']=pw1 if(pw==None) or (pw=='') else pw
    p['ph_no']=ph1 if(ph==None) or (ph=='') else ph
    p['address']=loc1 if(add==None) or (add=='') else add
    print(p)
    col.update({'email':'abiramimurali103@gmail.com'},{'$set':p})
    