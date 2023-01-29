import streamlit as st
from datetime import datetime
import uuid
from uuid import uuid1
import pandas as pd
import time
from deta import Deta


style = """ 

#mainmenu{
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer{
    visibility: hidden;
}


.header-item{
    background-color: rgb(255, 75, 75);
    border-radius: 200px;
    padding: 30px;
    color: white;
    font-size: 65px;
}

.subheader-item{
    background-color: rgb(255, 75, 75);
    padding: 7px;
    color: white;
    font-size: 20px;
}
a{
    text-decoration: none;
    color:white;
}
.btn{
    color: white;
    background-color: rgb(255, 75, 75); 
    border: 1px solid rgb(255, 75, 75);;
    border-radius: 6px;    
    padding: 5px 20px;      
    text-align: center;      
    display: inline-block;      
    font-size: 16px;      
    margin: 4px 2px;       
}
"""


st.set_page_config("Quick Meal","🍲",'centered')

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

payment_link= "https://paystack.com/pay/n3dypl0pnm"

def gen_id():
    unique_code = str(uuid1())
    global order_id
    order_id = unique_code[0:8]


date_time = datetime.now().strftime('%Y-%m-%d')

deta = Deta("a0j7y42b_xgRLgV4rX4Kd8AcjGHLakQayy1tQXWGJ")
order_history = deta.Base('Customer_Information')
order_summary = []
order_list = []
cost = []

#st.image('logo.png',width=700)
st.markdown("<h1 class='header-item' style='text-align: center'> Quick Meal <h1>", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.header("Order a meal of your choice👇🏽")


with st.form("user_data",True):
    col1,col2 = st.columns(2)
    customer = col1.text_input("Your Name")
    room_number = col2.text_input("Room Number")
    mail = st.text_input("Email Address")
    st_state = st.form_submit_button("Submit")

    if st_state:
        if customer == "" and room_number == "":
            st.warning("Please fill the above fields")
        else:
            st.success("Submitted Sucessfully ")


gen_id()


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.markdown(" <h1 style='text-align: center'> MENU📋 <h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown(" <h4 class='subheader-item' style='text-align: center'> Beans Section🍛 <h4>", unsafe_allow_html=True)
beans_section = st.multiselect("Pick an option(s)",('Beans','Fried yam','Akara'))

if beans_section: 
    for food in beans_section:
        amount = st.number_input(food,step=100,min_value=100)
        cost.append(amount)
        order_summary.append('Customer Name:{}'.format(customer))
        order_summary.append('Order ID:{}'.format(order_id))
        order_summary.append('Room Number:{}'.format(room_number))
        orders = st.code('{} - ₦{}'.format(food,amount),'text')
        order_summary.append('{} - ₦{}'.format(food,amount))
        order_list.append('{} - ₦{}'.format(food,amount))
        order_summary.append('Date/Time:{}'.format(date_time))
        
        
st.markdown("---")        
        

st.markdown(" <h4 class='subheader-item' style='text-align: center'> Solid Section🍮 <h4>", unsafe_allow_html=True)
solid_section = st.multiselect("Pick an option(s)",('Semo','Eba'))

if solid_section: 
    for food in solid_section:
        amount = st.number_input(food,step=100,min_value=100)
        cost.append(amount)
        order_summary.append('Customer Name:{}'.format(customer))
        order_summary.append('Order ID:{}'.format(order_id))
        order_summary.append('Room Number:{}'.format(room_number))
        orders = st.code('{} - ₦{}'.format(food,amount),'text')
        order_summary.append('{} - ₦{}'.format(food,amount))
        order_list.append('{} - ₦{}'.format(food,amount))
        order_summary.append('Date/Time:{}'.format(date_time))
st.markdown("---")


st.markdown(" <h4 class='subheader-item' style='text-align: center'> Main Bar🍟 <h4>", unsafe_allow_html=True)
main_bar = st.multiselect("Pick an option(s)",('Drink','Donut','Sausage','Chelsea Bread','Meatpie'))

if main_bar: 
    for food in main_bar:
        if food == 'Drink':
            amount = st.number_input(food,min_value=200,step=200)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

        if food == 'Donut':
            amount = st.number_input(food,min_value=150,step=150)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

        if food == 'Sausage':
            amount = st.number_input(food,min_value=250,step=250)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

        if food == 'Chelsea Bread':
            amount = st.number_input(food,min_value=100,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

        if food == 'Meatpie':
            amount = st.number_input(food,min_value=150,step=150)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

st.markdown("---")

st.markdown(" <h4 class='subheader-item' style='text-align: center'> Snacks Bar🍇 <h4>", unsafe_allow_html=True)
snacks_bar = st.multiselect("Pick an option(s)",('Bannana','Pineapple','Orange'))

if snacks_bar: 
    for food in snacks_bar:
        amount = st.number_input(food,100,step=100)
        cost.append(amount)
        order_summary.append('Customer Name:{}'.format(customer))
        order_summary.append('Order ID:{}'.format(order_id))
        order_summary.append('Room Number:{}'.format(room_number))
        orders = st.code('{} - ₦{}'.format(food,amount),'text')
        order_summary.append('{} - ₦{}'.format(food,amount))
        order_summary.append('Date/Time:{}'.format(date_time))
        order_list.append('{} - ₦{}'.format(food,amount))

st.markdown("---")

st.markdown(" <h4 class='subheader-item' style='text-align: center'> Rice Section🍚 <h4>", unsafe_allow_html=True)
rice_section = st.multiselect("Pick an option(s)",('Rice','Salad','Moi Moi','Chicken','Fish','Beef','Plantain','Egg'))

if rice_section: 
    for food in rice_section:
         if food == 'Chicken':
            amount = st.number_input(food,min_value=600,step=600)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

         if food == 'Fish':
            amount = st.number_input(food,min_value=300,step=300)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

         if food == 'Beef':
            amount = st.number_input(food,min_value=200,step=200)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

         if food == 'Rice':
            amount = st.number_input(food,min_value=200,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

         if food == 'Salad':
            amount = st.number_input(food,min_value=100,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))
        
         if food == 'Plantain':
            amount = st.number_input(food,min_value=100,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

         if food == 'Egg':
            amount = st.number_input(food,min_value=100,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

         if food == 'Moi Moi':
            amount = st.number_input(food,min_value=100,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))
          
st.markdown("---")

st.markdown(" <h4 class='subheader-item' style='text-align: center'> Basham Section🍛 <h4>", unsafe_allow_html=True)
basham_section = st.multiselect("Pick an option(s)",("spaghetti","vegetable Rice", "white Rice","fish",'chicken'))

if basham_section: 
    for food in basham_section:
        if food == 'fish':
            amount = st.number_input(food,min_value=300,step=300)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

        if food == 'chicken':
            amount = st.number_input(food,min_value=600,step=600)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))
         
        if food == 'rice':
            amount = st.number_input(food,min_value=200,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

        if food == 'vegetable Rice':
            amount = st.number_input(food,min_value=200,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))

        if food == 'spaghetti':
            amount = st.number_input(food,min_value=200,step=100)
            cost.append(amount)
            order_summary.append('Customer Name:{}'.format(customer))
            order_summary.append('Order ID:{}'.format(order_id))
            order_summary.append('Room Number:{}'.format(room_number))
            order_summary.append('Date/Time:{}'.format(date_time))
            orders = st.code('{} - ₦{}'.format(food,amount),'text')
            order_summary.append('{} - ₦{}'.format(food,amount))
            order_list.append('{} - ₦{}'.format(food,amount))
       
st.markdown("---")


submit_order = st.button("Submit Order",'submit')


if submit_order:

    st.success("Order submitted successfully, proceed to payment.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    

    st.subheader("Order Summary")
    order_summary = list(set(order_summary))
    order_list = list(set(order_list))

    global total_cost
    global total_order
    
    total_cost = 50
    total_order = 50

    for price in cost:
        total_cost = total_cost + price
        total_order = total_order + price

    if total_cost < 1000:
        profit = 100
        total_cost = total_cost + profit
        total_order = total_cost - profit

        


    elif total_cost > 1000:
        profit = 200
        total_cost = total_cost + profit
        total_order = total_cost - profit
        


    order_summary.append('Total Order - ₦{}'.format(total_order))
    order_summary.append('Amount to be paid - ₦{}'.format(total_cost))
    order_history.put({'name':customer, 'room':room_number, 'mail':mail, 'date_time':date_time, 'order_list':order_list, 'total_order':total_order,'total_cost':total_cost},order_id, expire_in=168800)


    for item in order_summary:
        display_order = '{}'.format(item)
        st.code(display_order,'text')


    st.markdown("""
        <form>
            <button class='btn'><a href="https://paystack.com/pay/n3dypl0pnm"> Pay<a/></button>
        </form>
    """,unsafe_allow_html=True)

    


 
                     


        

