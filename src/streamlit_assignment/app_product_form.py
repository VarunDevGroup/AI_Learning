import streamlit as st

st.sidebar.title("Welcome to Streamlit!")
product_name = st.sidebar.text_input("Enter the product name:")

category = st.sidebar.selectbox("Select a category:", ["Electronics", "Clothing", "Home & Kitchen"])
price=st.sidebar.number_input("Enter the product price:", min_value=0.0, step=10.0)

if (st.sidebar.button("Submit Product")):
    st.write(f"Product Name: {product_name}")
    st.write(f"Category: {category}")
    st.write(f"Price: ${price:.2f}")