from datetime import datetime
import streamlit as st
from deta import Deta
import pandas as pd
import time


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
    padding: 27px;
    color: white;
}
"""


st.set_page_config("Quick Meal Admin",'centered')

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='header-item' style='text-align: center'> Search Order ID🔎 <h1>", unsafe_allow_html=True)


deta = Deta("a0j7y42b_xgRLgV4rX4Kd8AcjGHLakQayy1tQXWGJ")
order_history = deta.Base('Customer_Information')
today = datetime.now().strftime('%Y-%m-%d')

def display_orders():
    global num_orders
    global recent_orders
    recent_orders = order_history.fetch({'date_time':today})._items
    num_orders = order_history.fetch({'date_time':today})._count
    st.info('Orders Today - {}'.format(num_orders),icon='🧾')
    result_display = pd.DataFrame(recent_orders,copy=False)
    st.dataframe(result_display) 
    
form = st.form("search")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

display_orders()    
    
def get_id():
    result = order_history.get(keyword)
    result_table = pd.DataFrame(result,copy=False)
    st.dataframe(result_table)
    #st.code(result_table,'text')



with form:
    keyword = st.text_input("")
    search = st.form_submit_button("Search")
    if form: 
        try:   
            get_id()
        except ValueError:
            st.warning('Enter a valid order id')





    
