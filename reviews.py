import streamlit as st
from pymongo import MongoClient, collection
cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['electronic_appliances']
collection = db['product_details']
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

    
    
    

        
    