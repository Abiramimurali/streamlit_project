import smtplib
import streamlit as st
import pymongo
from PIL import Image
from pymongo import MongoClient
import pandas as pd
from datetime import date
import streamlit.components.v1 as stc
from random import randint
import random
import smtplib
import ssl
import numpy as np
import plotly.express as px


cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


HTML_BANNER = """
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
    <div style="background-color:#00BFFF;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center; font-family:'Bebas Neue'">Electronic Store </h1>
    </div>
    """

RESULT_TEMP = """
<div style="width:90%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 60px;
box-shadow:0 0 15px 5px #ccc; background-color: #FFFF00;
  border-left: 5px solid #6c6c6c;">
<h4>{}</h4>
<p style="color:blue;"><span style="color:black;">🔨brand::</span>{}</p>
<p style="color:blue;"><span style="color:black;">😃ratings::</span>{}</p>
<p style="color:blue;"><span style="color:black;">💲Price:</span>{}</p>
<p style="color:blue;"><span style="color:black;">🧑‍👀 Views:</span>{}</p>

</div>
"""


details_TEMP="""

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Details
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            {}
          </div>
        </div>
      </div>
   </div>

"""



def main():
   
    menu = ["SignUp","Login",'Home', "user_data","Email Verification","Search","Order_Product","payment_page","product_cancellation","Product_Review",'Profile', "admin", "Sales_display", "about_us"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        stc.html(HTML_BANNER)
        st.header('Welcome to Electronic Store')
        cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = cluster['electronic_appliances']
        collection = db['product_details']
        try:
            email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
            products = list(collection.find({}))
            c_user = db['user_details']
            user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
        except:
            pass
        if random.randint(0, 1):
            products = [i['p_name'] for i in products]
            random_product = products[random.randint(0, len(products)-1)]
            st.markdown("""
            <html>
                <link href="https://fonts.googleapis.com/css?family=Be+Vietnam|Josefin+Sans:700&display=swap" rel="stylesheet">
                <style>
                    .container
                    {
                        position: absolute;
                        height: 500px;
                        width: 300px;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, 10%);
                        font-size: 20px;
                        text-align: center;
                        font-family: 'Be Vietnam';
                        clip-path: circle(18% at 50% 50%);
                        background: linear-gradient(-45deg, #C9BFFF, #F4E9FF);
                        transition: .5s ease-in-out;
                        border-radius: 8px;
                    }
                    .first
                    {
                        position: absolute;
                        height: 500px;
                        width: 300px;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        line-height: 250px;
                        background: rgb(255, 44, 44);
                        clip-path: circle(0% at 50% 50%);
                        transition: .5s ease-in-out;
                    }
                    .second
                    {
                        position: absolute;
                        height: 500px;
                        width: 300px;
                        top: 50%;
                        left: 50%;
                        font-size: 30px;
                        font-family: 'Nunito', 'Courier New', Courier, monospace;
                        transform: translate(-50%, -50%);
                        line-height: 500px;
                        background: rgb(156, 156, 255);
                        clip-path: circle(15% at 50% 50%);
                        transition: .5s ease-in-out;
                    }
                    .container:hover .first
                    {
                        clip-path: circle(0%);
                    }
                    .container:hover .second
                    {
                        clip-path: circle(0%);
                    }
                    .container:hover
                    {
                        clip-path: circle(100%);
                        background: linear-gradient(-45deg, #00C5D4, #15FFBA);
                    }
                    .icon
                    {
                        position: absolute;
                        top: 25%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        height: 20%;
                    }
                    .winmsg
                    {
                        position: absolute;
                        top: 80%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 20px;
                    }
                </style>
                <div class = 'container'>
                    <svg class='icon' id="_x33_0" enable-background="new 0 0 64 64" height="512" viewBox="0 0 64 64" width="512" xmlns="http://www.w3.org/2000/svg"><g><g><path d="m32 51.71-6 4.29 2.37-6.88z" fill="#ff826e"/><path d="m49.81 38.99-14.18 10.13-1.44-4.2-1.56-4.53-.63-1.84 1.4-4.08c.91.94 2.19 1.53 3.6 1.53 2.76 0 5-2.24 5-5 0-.35-.04-.69-.1-1.01 1.77 1.59 3.76 2.92 5.93 3.94-.52.54-.83 1.27-.83 2.07 0 1.59 1.24 2.9 2.81 2.99zm-6.81 3.01c0-1.66-1.34-3-3-3s-3 1.34-3 3 1.34 3 3 3 3-1.34 3-3z" fill="#ff826e"/><path d="m35.63 49.12 2.37 6.88-6-4.29-3.63-2.59-1.59-1.14c5.39-.24 7.41-3.06 7.41-3.06z" fill="#fcd770"/><path d="m32 38.55.63 1.84c-1 .96-4.22 3.35-11.46 3.59l-5.6-4c10.38-.34 14.46-3.96 15.27-4.8z" fill="#fcd770"/><path d="m15.94 27.65c.15-.12.3-.23.45-.34 2.92-2.1 6.49-3.31 10.26-3.31h.35l-.93 1.4c-3.27 4.9-8.2 8.45-13.88 10l-2.19.6c.69-2.06 1.73-3.92 3.06-5.54.84-1.05 1.81-1.99 2.88-2.81z" fill="#fcd770"/><path d="m32.63 40.39 1.56 4.53s-2.02 2.82-7.41 3.06l-5.61-4c7.24-.24 10.46-2.63 11.46-3.59z" fill="#5cd6b3"/><path d="m27 24 3.84 11.18c-.81.84-4.89 4.46-15.27 4.8l-5.57-3.98 2.19-.6c5.68-1.55 10.61-5.1 13.88-10z" fill="#5cd6b3"/><circle cx="60" cy="27" fill="#ff826e" r="2"/><circle cx="60" cy="60" fill="#ff826e" r="2"/><circle cx="56" cy="4" fill="#ff826e" r="2"/><path d="m54 36-4.19 2.99c-1.57-.09-2.81-1.4-2.81-2.99 0-.8.31-1.53.83-2.07 1.27.6 2.6 1.09 3.98 1.47z" fill="#fcd770"/><path d="m54 36-2.19-.6c-1.38-.38-2.71-.87-3.98-1.47-2.17-1.02-4.16-2.35-5.93-3.94-1.5-1.35-2.84-2.89-3.97-4.59l-.93-1.4h.35c3.77 0 7.34 1.21 10.26 3.31 2.92 2.11 5.19 5.11 6.39 8.69z" fill="#ff826e"/><circle cx="47" cy="15" fill="#ff826e" r="2"/><circle cx="45" cy="51" fill="#ff826e" r="2"/><circle cx="40" cy="42" fill="#fcd770" r="3"/><path d="m41.9 29.99c.06.32.1.66.1 1.01 0 2.76-2.24 5-5 5-1.41 0-2.69-.59-3.6-1.53l3.6-10.47.93 1.4c1.13 1.7 2.47 3.24 3.97 4.59z" fill="#fcd770"/><g fill="#ff826e"><circle cx="34" cy="6" r="2"/><circle cx="25" cy="16" r="2"/><circle cx="21" cy="60" r="2"/><circle cx="8" cy="19" r="2"/></g></g><g><path d="m36.823 49.498 18.36-13.114-.233-.701c-2.53-7.586-9.602-12.683-17.599-12.683h-1.065l-4.286 12.469-4.286-12.469h-1.065c-3.764 0-7.316 1.141-10.293 3.127-.214-.616-.356-1.323-.356-2.127 0-1.817.982-3.158 2.022-4.579.973-1.328 1.978-2.702 1.978-4.421h-2c0 1.065-.738 2.073-1.592 3.24-1.129 1.542-2.408 3.289-2.408 5.76 0 1.313.287 2.43.692 3.362-.664.56-1.284 1.172-1.866 1.823-2.355-1.179-4.692-1.185-6.826-1.185-.567 0-1.095-.039-1.569-.116-.816-.132-1.431-.879-1.431-1.738 0-.472.184-.917.518-1.25l1.189-1.189-1.414-1.414-1.189 1.189c-.712.712-1.104 1.658-1.104 2.664 0 1.859 1.309 3.42 3.111 3.712.579.095 1.215.142 1.889.142 1.903 0 3.737.005 5.545.792-1.048 1.473-1.9 3.11-2.493 4.891l-.233.701 18.36 13.114-3.139 9.132 7.96-5.687 7.961 5.687zm3.177-5.498c-1.103 0-2-.897-2-2s.897-2 2-2 2 .897 2 2-.897 2-2 2zm8-8c0-.293.07-.574.19-.834 1.09.47 2.205.887 3.362 1.203l.154.042-2.149 1.535c-.894-.204-1.557-1.002-1.557-1.946zm4.327-1.493-.25-.068c-5.358-1.461-10.009-4.785-13.143-9.363 5.828.555 10.914 4.148 13.393 9.431zm-11.327-3.507c0 2.206-1.794 4-4 4-.898 0-1.737-.305-2.433-.844l2.728-7.937c1.062 1.549 2.291 2.955 3.648 4.218.026.186.057.373.057.563zm-7.111 5.126c.928.566 1.993.874 3.111.874 2.938 0 5.384-2.123 5.897-4.915 1.101.835 2.27 1.574 3.495 2.221-.247.527-.392 1.098-.392 1.694 0 1.344.674 2.54 1.706 3.267l-3.714 2.653c-.044-2.168-1.814-3.92-3.992-3.92-2.206 0-4 1.794-4 4 0 1.725 1.103 3.184 2.636 3.745l-2.492 1.78-3.087-8.979zm-7.184-9.907 2.979 8.667c-1.333 1.133-5.305 3.733-13.823 4.073l-3.567-2.548.154-.042c5.811-1.585 10.856-5.189 14.257-10.15zm3.668 10.669 1.094 3.183c-1.211.936-4.195 2.642-9.997 2.893l-3.05-2.179c6.491-.632 10.151-2.562 11.953-3.897zm1.773 5.159.908 2.643c-.684.664-2.503 2.032-5.992 2.269l-3.069-2.192c4.129-.503 6.693-1.731 8.153-2.72zm-17.853-9.34 1.414-1.414c-.387-.387-.775-.724-1.164-1.025.374-.401.769-.779 1.179-1.139.827 1.09 1.654 1.658 1.723 1.704l1.109-1.664c-.013-.008-.633-.433-1.259-1.27 2.271-1.556 4.931-2.551 7.769-2.822-3.134 4.577-7.785 7.902-13.143 9.363l-.25.068c.45-.959.993-1.855 1.603-2.694.341.258.68.554 1.019.893zm13.668 20.663.914-2.659 1.404 1.003zm1.456-4.73c2.032-.451 3.44-1.247 4.333-1.929l2.289 6.659z"/><path d="m22 16c0 1.654 1.346 3 3 3s3-1.346 3-3-1.346-3-3-3-3 1.346-3 3zm4 0c0 .551-.449 1-1 1s-1-.449-1-1 .449-1 1-1 1 .449 1 1z"/><path d="m34 9c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3 1.346 3 3 3zm0-4c.551 0 1 .449 1 1s-.449 1-1 1-1-.449-1-1 .449-1 1-1z"/><path d="m50 15c0-1.654-1.346-3-3-3s-3 1.346-3 3 1.346 3 3 3 3-1.346 3-3zm-3 1c-.551 0-1-.449-1-1s.449-1 1-1 1 .449 1 1-.449 1-1 1z"/><path d="m60 24c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.551 0-1-.449-1-1s.449-1 1-1 1 .449 1 1-.449 1-1 1z"/><path d="m56 7c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3 1.346 3 3 3zm0-4c.551 0 1 .449 1 1s-.449 1-1 1-1-.449-1-1 .449-1 1-1z"/><path d="m5 19c0 1.654 1.346 3 3 3s3-1.346 3-3-1.346-3-3-3-3 1.346-3 3zm4 0c0 .551-.449 1-1 1s-1-.449-1-1 .449-1 1-1 1 .449 1 1z"/><path d="m5.353 11.942c.609 1.218 1.716 2.106 3.038 2.437l6.367 1.592.485-1.94-6.367-1.592c-.754-.188-1.386-.696-1.734-1.391-.093-.186-.142-.393-.142-.601 0-.512.284-.971.742-1.2.323-.162.685-.247 1.047-.247h3.598l-.955-2.867c-.181-.542-.048-1.137.376-1.584.333-.349.8-.549 1.32-.549.94 0 1.822.364 2.483 1.026 1.541 1.54 2.389 3.588 2.389 5.766v2.208h2v-2.208c0-2.712-1.056-5.262-2.974-7.18-1.039-1.04-2.423-1.612-3.937-1.612-1.026 0-2.021.427-2.76 1.204-.905.951-1.209 2.316-.794 3.562l.078.234h-.824c-.671 0-1.343.159-1.941.458-1.14.57-1.848 1.715-1.848 2.989 0 .516.122 1.033.353 1.495z"/><path d="m27.093 4.444c-.224.177-.805.42-1.17.573-1.234.515-2.923 1.221-2.923 2.983 0 3.888 7.181 4 8 4v-2c-2.092 0-6-.586-6-2 0-.43.939-.823 1.694-1.138.975-.407 1.983-.829 2.329-1.757.125-.339.206-.883-.128-1.552-1.215-2.43-5.957-2.553-6.895-2.553v2c1.727.002 4.48.442 5.093 1.444z"/><path d="m29.791 22.022.419 1.956c.195-.042 4.79-1.065 4.79-4.407 0-2.62-2.392-3.571-4-3.571v2c.205 0 2 .044 2 1.571 0 1.702-3.179 2.445-3.209 2.451z"/><path d="m37 12.424c0 1.769.687 3.463 1.934 4.77 1.332 1.396 2.066 2.747 2.066 3.806h2c0-1.621-.881-3.366-2.619-5.188-.891-.932-1.381-2.136-1.381-3.388v-.181c0-1.179.459-2.288 1.293-3.122 1.446-1.446 3.968-1.446 5.414 0l.586.586 1.414-1.414-.586-.586c-1.1-1.101-2.564-1.707-4.121-1.707s-3.021.606-4.121 1.707c-1.212 1.211-1.879 2.822-1.879 4.536z"/><path d="m47.168 23.445 1.663 1.112c.017-.025 1.754-2.557 4.169-2.557h2.171c2.091 0 4.057-.814 5.536-2.293l.093-.093c1.419-1.418 2.2-3.305 2.2-5.312 0-1.05-.308-2.067-.891-2.941-.985-1.478-2.635-2.361-4.412-2.361-1.362 0-2.642.53-3.604 1.493l-.8.8 1.414 1.414.8-.8c.585-.585 1.363-.907 2.19-.907 1.107 0 2.134.55 2.748 1.471.363.544.555 1.178.555 1.832 0 1.472-.573 2.856-1.614 3.897l-.093.093c-1.101 1.101-2.564 1.707-4.122 1.707h-2.171c-3.495 0-5.738 3.305-5.832 3.445z"/><path d="m6.542 50.727c-.888-.43-2.542-1.228-2.542-1.727 0-1.025 2.196-1.816 3.198-2.02l-.394-1.96c-.492.098-4.804 1.045-4.804 3.98 0 1.754 1.951 2.696 3.672 3.527.69.333 2.082 1.005 2.3 1.4-.356.47-1.872 1.442-3.402 2.169l.858 1.807c3.034-1.44 4.572-2.754 4.572-3.903 0-1.604-1.758-2.453-3.458-3.273z"/><path d="m51.196 50.02-.394 1.961c1.002.203 3.198.994 3.198 2.019 0 .499-1.654 1.297-2.542 1.727-1.7.82-3.458 1.669-3.458 3.273 0 1.149 1.538 2.463 4.571 3.903l.858-1.807c-1.501-.713-3.043-1.702-3.401-2.169.221-.396 1.61-1.067 2.3-1.4 1.721-.831 3.672-1.773 3.672-3.527 0-2.935-4.312-3.882-4.804-3.98z"/><path d="m14.316 50.051c-.758-.252-2.169-.723-2.316-1.051 0-.78 1.918-1.695 3.244-2.03l-.486-1.94c-.795.199-4.758 1.324-4.758 3.97 0 1.721 1.957 2.373 3.684 2.949.683.228 1.895.631 2.237.949-.127.131-.312.3-.46.436-.83.761-2.084 1.91-2.008 3.476.053 1.069.69 2.047 1.948 2.99l1.2-1.6c-.51-.383-1.124-.952-1.15-1.489-.031-.627.774-1.364 1.361-1.903.637-.584 1.188-1.089 1.188-1.808 0-1.721-1.957-2.373-3.684-2.949z"/><path d="m21 57c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.551 0-1-.449-1-1s.449-1 1-1 1 .449 1 1-.449 1-1 1z"/><path d="m45 48c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.551 0-1-.449-1-1s.449-1 1-1 1 .449 1 1-.449 1-1 1z"/><path d="m60 57c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.551 0-1-.449-1-1s.449-1 1-1 1 .449 1 1-.449 1-1 1z"/><path d="m28 59h2v2h-2z"/><path d="m20 49h2v2h-2z"/><path d="m10 59h2v2h-2z"/><path d="m58 47h2v2h-2z"/><path d="m42 57h2v2h-2z"/><path d="m49 3h2v2h-2z"/><path d="m20 20h2v2h-2z"/><path d="m32 12h2v2h-2z"/><path d="m4 4h2v2h-2z"/><path d="m56 15h2v2h-2z"/></g></g></svg>
                    <p class='winmsg'>Congratulations!! You've won a 40% offer on the following product</p>
                    <div class = 'first'>
                    </div>
                    <div class = 'second'>
                        hover
                    </div>
                </div>
            </html>
            """, True)
            st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');
            temp=[]
            post={"name":"Ramu"}
            st.subheader("Order product")
            img3=Image.open("Mobile.jpg")
            img2=Image.open("Air Conditioner.jpg")
            img1=Image.open("Heater.jpeg")
            resizedImages=[]
            for image in [img1,img2,img3]:
                img = image
                resizedImg = img.resize((500, 500), Image.ANTIALIAS)
                resizedImages.append(resizedImg)
            resizedImages = {products[i]:resizedImages[i] for i in range(3)}
            with st.form(key='my_form'):
                col1, x,col2,y,col3 = st.beta_columns(5)
                col2.header(random_product)
                original = resizedImages[random_product]
                col2.image(original, use_column_width=True)
                level = st.slider("Select the level", 1, 10)
                post['product'] = random_product
                post["quantity"]=level
                submit = st.form_submit_button('Submit')
            if(submit):
                temp.append(post)
                collection = db['buffer']
                collection.insert_one(post)
                st.success("Added to cart -> Proceed with payment")
        else:
            st.markdown("""
            <html>
                <link href="https://fonts.googleapis.com/css?family=Be+Vietnam|Josefin+Sans:700&display=swap" rel="stylesheet">
                <style>
                    .container
                    {
                        position: absolute;
                        height: 500px;
                        width: 300px;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, 10%);
                        font-size: 20px;
                        text-align: center;
                        font-family: 'Be Vietnam';
                        clip-path: circle(18% at 50% 50%);
                        background: linear-gradient(-45deg, #C9BFFF, #F4E9FF);
                        transition: .5s ease-in-out;
                        border-radius: 8px;
                    }
                    .first
                    {
                        position: absolute;
                        height: 500px;
                        width: 300px;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        line-height: 250px;
                        background: rgb(255, 44, 44);
                        clip-path: circle(0% at 50% 50%);
                        transition: .5s ease-in-out;
                    }
                    .second
                    {
                        position: absolute;
                        height: 500px;
                        width: 300px;
                        top: 50%;
                        left: 50%;
                        font-size: 30px;
                        font-family: 'Nunito', 'Courier New', Courier, monospace;
                        transform: translate(-50%, -50%);
                        line-height: 500px;
                        background: rgb(156, 156, 255);
                        clip-path: circle(15% at 50% 50%);
                        transition: .5s ease-in-out;
                    }
                    .icon
                    {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        height: 35%;
                        clip-path: circle(0% at 50% 50%);
                        transition: .5s ease-in-out;
                    }
                    .container:hover .first
                    {
                        clip-path: circle(0%);
                    }
                    .container:hover .second
                    {
                        clip-path: circle(0%);
                    }
                    .container:hover .icon
                    {
                        clip-path: circle(100%);
                    }
                    .container:hover
                    {
                        clip-path: circle(100%);
                        background: linear-gradient(-45deg, #00C5D4, #15FFBA);
                    }
                    .winmsg
                    {
                        position: absolute;
                        top: 80%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 20px;
                    }
                </style>
                <div class = 'container'>
                    <svg class = 'icon' height="512" viewBox="0 0 64 64" width="512" xmlns="http://www.w3.org/2000/svg"><g id="flat"><path d="m61 19c0-3.866-3.134-8-7-8a6.917 6.917 0 0 0 -6 3 15.99 15.99 0 0 0 -16-3 15.99 15.99 0 0 0 -16 3 6.917 6.917 0 0 0 -6-3c-3.866 0-7 4.134-7 8a7.282 7.282 0 0 0 6 7c-4.326 9.352-3.021 13.979 2 19 6 6 19 8 21 9 2-1 15-3 21-9 5.021-5.021 6.326-9.648 2-19a7.282 7.282 0 0 0 6-7z" fill="#d3843d"/><path d="m14.253 16.686a3.992 3.992 0 1 0 -3.58 6.281c1.073-1.93 2.467-4.407 3.58-6.281z" fill="#66342e"/><path d="m49.747 16.686a3.992 3.992 0 1 1 3.58 6.281c-1.073-1.93-2.467-4.407-3.58-6.281z" fill="#66342e"/><path d="m43 39c0 6.627-6 10-11 10s-11-3.373-11-10 6-14 11-14 11 7.373 11 14z" fill="#f9bb4b"/><path d="m23 26a2 2 0 1 1 2-2 2 2 0 0 1 -2 2z" fill="#301a12"/><path d="m41 26a2 2 0 1 1 2-2 2 2 0 0 1 -2 2z" fill="#301a12"/><path d="m37 33c0 1.657-2.239 2-5 2s-5-.343-5-2 2.239-4 5-4 5 2.343 5 4z" fill="#66342e"/><path d="m21 30a2 2 0 0 1 -4 0c0-1.105 4-3 4-3z" fill="#f4f4e6"/><path d="m43 30a2 2 0 0 0 4 0c0-1.105-4-3-4-3z" fill="#f4f4e6"/><path d="m31.927 43.376-1.856-.747a5.4 5.4 0 0 1 3.281-3.042c1.615-.424 3.388.124 5.273 1.632l-1.25 1.562c-1.358-1.088-2.533-1.514-3.5-1.263a3.4 3.4 0 0 0 -1.948 1.858z" fill="#143441"/><g fill="#66342e"><path d="m19.316 22.948-.632-1.9a27.591 27.591 0 0 0 5.761-2.884l1.11 1.664a29.007 29.007 0 0 1 -6.239 3.12z"/><path d="m44.684 22.948a29.007 29.007 0 0 1 -6.239-3.116l1.11-1.664a27.591 27.591 0 0 0 5.761 2.884z"/></g></g></svg>
                    <p class='winmsg'>No offers! Better luck next time</p>
                    <div class = 'first'>
                    </div>
                    <div class = 'second'>
                        hover
                    </div>
                </div>
            </html>
            """, True)
                
        
    elif choice== "SignUp":
        stc.html(HTML_BANNER)
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
            p={}
            p['name']=name+" "+last
            p['email']=email
            p['password']=pw2
            p['ph_no']=ph
            p['address']=add
            col.insert_one(p)

    elif choice=="Email Verification": 
        stc.html(HTML_BANNER)
        gen1=0
        client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
        db=client["electronic_appliances"]
        c1=db["user_details"]
        c2=db['sign_up']
        otp1=db['email_ver_otp']
        st.title("email_verification")

        def verification(to):
            db['email_ver_otp'].remove()
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
            print('came')
            verification(email)
        with st.form(key='my-form'):
            st.info("Please check your email & enter the 4 digit pin")
            otp=st.text_input("OTP")
            submit_button = st.form_submit_button(label='Submit')
        try:
            f = list(otp1.find())
            print(list(f))
            f = f[0]['otp']
        except:
            pass

        print(otp,f)

        if(otp==f) and (submit_button) :
            a1=otp1.find_one()
            a1=a1['email']
            print(a1, 'this is a1')
            a2=c2.find_one({'email':a1})
            if(a2==None):
                st.error("Please give registered email address")
            c1.insert_one(a2)
            c2.delete_one({'email':a1})
            st.success("Email verified!")
        elif(submit_button) and (otp!=f):
            st.error("Incorrect otp!")
        
        
    elif choice== "Login":
        stc.html(HTML_BANNER)
        client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
        db=client["electronic_appliances"]
        email_ver_otp = db['email_ver_otp'].remove()
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
                x = {}
                x['email']=email
                db['email_ver_otp'].insert_one(x)
                st.success("successfully logged in")
        elif(submit)and (a!=None):
            st.error("Invalid email address! Please sign up")

        if(c):
                st.info("You can change the password by clicking -> Home choose -> Forgot password")

    elif choice == 'Profile':
        client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
        db=client["electronic_appliances"]
        col=db["user_details"]
        c_user = db['user_details']
        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']

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

        """%user, unsafe_allow_html=True)

        n=col.find({'email':email_ver_otp})
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
    
    elif choice == 'user_data':
        stc.html(HTML_BANNER)
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

    
    elif choice== "Order_Product":
        stc.html(HTML_BANNER)
        temp=[]
        cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db=cluster["electronic_appliances"]
        c=db["buffer"]
        c_user = db['user_details']
        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
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

        confirmed_ticket=db["confirmed_ticket"]
        coll_prod_details=db["product_details"]
        pro_d=coll_prod_details.find()

        price=[i["price"] for i in pro_d]

        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        c_user = db['user_details']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
        post={"name":user}
        st.subheader("Order product")
        img1=Image.open("Ac.jpg")


        img2=Image.open("phone4.jpg")

        img3=Image.open("heater.jpeg")

        resizedImages=[]

        for image in [img1,img2,img3]:
            img = image
            resizedImg = img.resize((500, 500), Image.ANTIALIAS)
            resizedImages.append(resizedImg)



        with st.form(key='my_form'):



            col1, x,col2,y,col3 = st.beta_columns(5)

            original = resizedImages[0]
            col1.header("Air Conditioner")
            col1.image(original, use_column_width=True)

            original = resizedImages[1]

            col2.header("IPHONE")
            col2.image(original, use_column_width=True)

            original = resizedImages[2]
            col3.header("Electric Heater")
            col3.image(original, use_column_width=True)

            choice = st.selectbox("Choose One: ",
                     ['Air Conditioner', 'Mobile', 'Heater'])

            if choice:
                
                level = st.slider("Select the level", 1, 10)
                post["product"]=choice
                post["quantity"]=level
            
            submit = st.form_submit_button('Add to cart')

            if(submit):
                temp.append(post)
                c.insert_one(post)
                print(temp)
                st.success("Added to cart -> Proceed with payment")


    elif choice=="payment_page":
        cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db=cluster["electronic_appliances"]
        c=db["buffer"]
        c_user = db['user_details']
        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
        

        confirmed_ticket=db["confirmed_ticket"]
        coll_prod_details=db["product_details"]
        pro_d=coll_prod_details.find()

        price=[i["price"] for i in pro_d]

        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        c_user = db['user_details']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
        post={"name":user}

        stc.html(HTML_BANNER)
        st.header("payment page")
        cart=c.find()
        #cart gives u a cursor object
        l=[]
        for i in range(cart.count()):
            d=cart[i]
            if(d["product"]=="Air Conditioner"):
                p=int(price[1])*d["quantity"]
                brand="Hitachi"
            elif(d["product"]=="Mobile"):
                p=int(price[2])*d["quantity"]
                brand="iPhone"
            else:
                p=int(price[1])*d["quantity"]
                brand="Bajaj"
            day=date.today().strftime("%m/%d/%Y")
            md={"name":d["name"],"product":d["product"],"quantity":d["quantity"],"brand":brand,"price":p,"date":day}
            print(md)
            l.append(md)
            
        print(l)
        ld= pd.DataFrame(l)
        print(ld)
            
        print(l)   
        #print(df)
        st.dataframe(ld.head(10))

        tp=sum(ld["price"])
        #print(sum(tp))

        st.info("The total price of your cart  is %d"%(tp))

        check=st.button("Confirm payment")

        if check:
            for i in l:
                confirmed_ticket.insert_one(i)
            c.remove({})
            st.success("Done with payment")
                
            
        
    elif choice=="Search":
        stc.html(HTML_BANNER)
        client = pymongo.MongoClient("mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
        db=client["electronic_appliances"]
        c_user = db['user_details']
        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
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
        choice = st.selectbox("Choose Category: ",
                     ['Air Conditioner', 'Mobile', 'Heater'])

        if(choice=='Air Conditioner'):
            st.image("AC1.jpg")
    
            rt=RESULT_TEMP.format("Air Conditioner","Hitachi","5","20000","200")
            stc.html(details_TEMP.format(rt),height=350)

            st.image("AC.jpg")
    
            rt=RESULT_TEMP.format("Air Conditioner","SONY","5","20000","200")
            stc.html(details_TEMP.format(rt),height=350)
    

        if(choice=='Mobile'):
            st.image("iphone1.jpg")
            #stc.html(RESULT_TEMP.format("Iphone","Apple","5","200000","200"),height=350)
            rt=RESULT_TEMP.format("Iphone","Apple","5","200000","200")
            stc.html(details_TEMP.format(rt),height=350)

            

            st.image("phone4.jpg")
            #stc.html(RESULT_TEMP.format("Iphone","Apple","5","200000","200"),height=350)
            rt=RESULT_TEMP.format("Iphone","Apple","5","200000","200")
            stc.html(details_TEMP.format(rt),height=350)
    
    

        if(choice=='Heater'):
            st.image("heater1.jpeg")
            rt=RESULT_TEMP.format("Heater","Bajaj","5","450","200")
            stc.html(details_TEMP.format(rt),height=350)

            st.image("heater.jpeg")
            rt=RESULT_TEMP.format("Heater","Bajaj","5","450","200")
            stc.html(details_TEMP.format(rt),height=350)
            
    
                        
    elif choice=="product_cancellation":
        stc.html(HTML_BANNER)
        sender_email = 'abirami.prodapt@gmail.com'
        password = 'Abirami103$'
        cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = cluster['electronic_appliances']
        collection = db['confirmed_ticket']
        c_user = db['user_details']
        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
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
            with st.form(key='my_form1'):
                for i in range(len(products)):
                    check_products[i] = st.checkbox(label=products[i])
                submit_button1 = st.form_submit_button(label='Submit')
            if submit_button1:
                if [False]*len(products) == check_products:
                    st.warning('Select a Product to cancel!')
                else:
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
                            
                   
    elif choice=="admin":
        stc.html(HTML_BANNER)
        cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = cluster["electronic_appliances"]
        c=db["product_details"]

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
            post["price"]=p_cost
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
        c.update_one({'p_id':p_id},{'$set':{'price':p_cost,'p_stock':p_stock}})

    elif choice =='Sales_display':
        stc.html(HTML_BANNER)
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
        
        
    elif choice=="about_us":
        stc.html(HTML_BANNER)
        st.title("About Us")

        st.header("Our Mission")
        '''
        Welcome to our website!
        Our Mission is to create best Electronic Appliances Web application
        which will make people's online shopping more easy and user friendly.

        '''
        st.header("Meet Our Team")
        '''
        Our team Sibi,Mothish,Abirami,Shalini We four created this Web app.'''
        st.header("Tools we used")
        '''
        -->Language:Python


        -->Frontend:Streamlit


        -->Database:MongoDB
        '''
        st.header("Contact Us")
        '''
        Send your queries

        Gmail:Eappstore@gmail.com

        Call:600993-39409
        '''


    elif choice =='Product_Review':
        stc.html(HTML_BANNER)
        cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = cluster['electronic_appliances']
        collection = db['product_details']
        c_user = db['user_details']
        email_ver_otp = list(db['email_ver_otp'].find())[0]['email']
        user = list(c_user.find({'email' : email_ver_otp}))[0]['name']
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
        comments = {i['p_name'] : i['reviews'] for i in list(collection.find({}))}
        head_html = """<head>
            <link href="https://fonts.googleapis.com/css?family=Be+Vietnam|Josefin+Sans:700&display=swap" rel="stylesheet">
            <style>
                .product-container
                {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    height: 80px;
                    width: 300px;
                    transform: translate(-100%, -50%);
                    background: rgb(255,33,33);
                    background: linear-gradient(90deg, rgba(255,33,33,1) 0%, rgba(255,175,0,1) 100%);
                    border-radius: 0px 40px 0px 40px;
                    font-family: 'Josefin Sans';
                    color: white
                }
                .product-text-container
                {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                }
                .review-container
                {
                    position: absolute;
                    height: 150px;
                    width: 600px;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgb(218,255,250);
                    background: linear-gradient(90deg, rgba(218,255,250,1) 0%, rgba(187,255,255,0.8942927512801996) 100%);
                    border-radius: 40px 0px 40px 0px;
                }
                .review-text-container
                {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-family: Be Vietnam;
                    font-style: italic;
                    color: #4a4a4a;
                }
            </style>"""
        body_html1 = """<body>
                <div class='product-container'>
                    <div class='product-text-container'>
                        %s
                    </div>
                </div>
                """
        body_html2 = """<body>
                <div class='review-container'>
                    <div class='review-text-container'>"%s" ~ %s</div>
                </div>
            </body>"""
        st.title('Product Reviews')
        st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('')
        for i in comments:
            st.markdown('<html>' + head_html + body_html1%(i) + '</html>', True)
            for j in comments[i]:
                st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('')
                st.markdown('<html>' + head_html + body_html2%(comments[i][j], j) + '</html>', True)
                st.text('');st.text('')
            st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('');st.text('')
        st.header('Add a comment')
        with st.form(key='my_form'):
            choice = st.selectbox("Choose One: ",['Air Conditioner', 'Mobile', 'Heater'])
            username = st.text_input(label='Enter the username')
            comment = st.text_input(label='Enter the review')
            submit = st.form_submit_button('Submit')
        if submit:
            old_comments = comments[choice]
            old_comments[username] = comment
            collection.update_one({'p_name': choice}, {'$set': {'reviews': old_comments}})
            st.success('Review added!')

    
    
    

        
    
                

       

         
main()
