import streamlit as st
import pymongo
from PIL import Image
from pymongo import MongoClient
import pandas as pd
from datetime import date
import streamlit.components.v1 as stc


cluster = MongoClient('mongodb+srv://abirami:mmakk2000@cluster0.8rqgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster["electronic_appliances"]
c=db["buffer"]
confirmed_ticket=db["confirmed_ticket"]
coll_prod_details=db["product_details"]
pro_d=coll_prod_details.find()

price=[i["price"] for i in pro_d]


HTML_BANNER = """
    <div style="background-color:#00BFFF;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Electronic Store </h1>
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
    """APPLIANCE STORE"""
    st.title("APPLIANCE STORE")
   
    menu = ["Home","Signup","Login","user_data","EmailRegistration","Search","Order_Product","payment_page","product_cancellation","admin","about_us "]
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
                global flag
                flag=1
                st.success("Added to cart -> Proceed with payment")


    elif choice=="payment_page":
        st.header("payment page")
        st.header(price)
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
        choice = st.selectbox("Choose Category: ",
                     ['Air Conditioner', 'Mobile', 'Heater'])

        if(choice=='Air Conditioner'):
            st.image("AC1.jpg")
    #stc.html(RESULT_TEMP.format("Air Conditioner","Sony","5","20000","200"),height=350)
            rt=RESULT_TEMP.format("Air Conditioner","Sony","5","20000","200")
            stc.html(details_TEMP.format(rt),height=350)
    

        if(choice=='Mobile'):
            st.image("iphone1.jpg")
    #stc.html(RESULT_TEMP.format("Iphone","Apple","5","200000","200"),height=350)
            rt=RESULT_TEMP.format("Iphone","Apple","5","200000","200")
            stc.html(details_TEMP.format(rt),height=350)


    
    

        if(choice=='Heater'):
            st.image("heater1.jpeg")
            stc.html(RESULT_TEMP.format("Heater","Bajaj","5","450","200"),height=350)
            
    
                        
    elif choice=="product_cancellation":
        st.subheader("Product_cancellation")
        
    elif choice=="admin":
        st.subheader("admin view")
        
    elif choice=="about us":
        st.subheader("about us")

       

print()    
flag=0           
main()
