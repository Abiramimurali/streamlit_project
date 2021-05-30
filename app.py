import streamlit as st
import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster["electronic_appliances"]

def main():
    """APPLIANCE STORE"""
    st.title("APPLIANCE STORE")

    menu = ["Home","Login","SignUp","user_data","EmailRegistration","Order_Product","product_cancellation","admin","about_us "]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        
    elif choice== "SignUp":
        st.subheader("Registration page")
        
    elif choice=="EmailRegistration":
        st.subheader("Email")
        
    elif choice== "Login":
        st.subheader("login")

    
    elif choice== "Order_product":
        st.subheader("Order product")
        
    elif choice=="product_cancellation":
        st.subheader("Product_cancellation")
        
    elif choice=="admin":
        st.subheader("admin view")
        
    elif choice=="about us":
        st.subheader("about us")
            
            
main()
