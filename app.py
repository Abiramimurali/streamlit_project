import streamlit as st
import pymongo
from PIL import Image
from pymongo import MongoClient
import pandas as pd

cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster["electronic_appliances"]
c=db["buffer"]



def main():
    """APPLIANCE STORE"""
    st.title("APPLIANCE STORE")
   
    menu = ["Home","Signup","Login","user_data","EmailRegistration","Order_Product","payment_page","product_cancellation","admin","about_us "]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        
    elif choice== "SignUp":
        st.subheader("Registration page")
        
    elif choice=="EmailRegistration":
        st.subheader("Email")
        
    elif choice== "Login":
        st.subheader("login")

    
    elif choice== "Order_Product":
        temp=[]
        post={"name":"Ramu"}
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
            col1.header("AC")
            col1.image(original, use_column_width=True)

            original = resizedImages[1]

            col2.header("IPHONE")
            col2.image(original, use_column_width=True)

            original = resizedImages[2]
            col3.header("Electric Heater")
            col3.image(original, use_column_width=True)

            choice = st.selectbox("Choose One: ",
                     ['AC', 'IPHONE', 'HEATER'])

            if choice:
                level = st.slider("Select the level", 1, 10)
                post["product"]=choice
                post["quantity"]=level
            submit = st.form_submit_button('Submit')

            if(submit):
                temp.append(post)
                c.insert_one(post)
                print(temp)
                global flag
                flag=1
                st.success("Added to cart -> Proceed with payment")


    elif choice=="payment_page":
        st.header("payment page")
        cart=c.find()
        #cart gives u a cursor object
        l=[]
        for i in range(cart.count()):
            d=cart[i]
            md={"name":d["name"],"product":d["product"],"quantity":d["quantity"]}
            print(md)
            l.append(md)
            
            
        print(l)
        ld= pd.DataFrame(l)
        print(ld)
            
        print(l)   
        #print(df)
        st.dataframe(ld.head(10))

        st.info("The total price of your cart ")
            
        
        
            
    
                        
    elif choice=="product_cancellation":
        st.subheader("Product_cancellation")
        
    elif choice=="admin":
        st.subheader("admin view")
        
    elif choice=="about us":
        st.subheader("about us")

       

print()    
flag=0           
main()
