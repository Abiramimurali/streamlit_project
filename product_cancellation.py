import streamlit as st
from pymongo import MongoClient, collection
import smtplib
from random import randint
sender_email = 'abirami.prodapt@gmail.com'
password = 'Abirami103$'
cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['electronic_appliances']
collection = db['confirmed_ticket']
c_user = db['user_details']
user = 'Ramu'
rec_email = list(c_user.find({'name': user}))[0]['email']
n = collection.find({'name': user})
n = list(n)

products = list(set([i['product'] for i in n]))
check_products = products[::]

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
            top: 0px;
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
"""%user, unsafe_allow_html=True)
st.title('Product Cancellation')
if len(products) == 0:
        st.warning('Your order list is empty!')
else:
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
    <p class = 'order-cancel'>Select the items to be cancelled</p>
    </html>
    """, True)
    flag = 0
    with st.form(key='my_form1'):
        for i in range(len(products)):
            check_products[i] = st.checkbox(label=products[i])
        submit_button1 = st.form_submit_button(label='Submit')
    if submit_button1:
        if [False]*len(products) == check_products:
            st.warning('Select a Product to cancel!')
        else:
            flag = 1
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            otp = str(randint(1000, 9999))
            otptable = db['otp']
            otptable.remove({})
            otptable.insert_one({'otp': otp})
            message = 'Your OTP is %s'%(otp)
            server.login(sender_email, password)
            server.sendmail(sender_email, rec_email, message)
            st.success('An OTP has been sent to your email!')
        
    with st.form(key='my_form2'):
        otp = st.text_input(label='Enter the OTP')
        submit_button2 = st.form_submit_button(label='Submit OTP')

    if submit_button2:
        otptable = db['otp']
        if otp == list(otptable.find({}))[0]['otp']:
            st.title('Products cancelled')
            for i in range(len(products)):
                if check_products[i]:
                    collection.remove({'name':user, 'product': products[i]})
                    st.success(products[i])
        else:
            st.error('Invalid OTP')
                    
    



