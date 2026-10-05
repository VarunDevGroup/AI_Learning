import streamlit as st

price = st.text_input("Enter Product Price:")
discount = st.slider("Select Discount Percentage:", 0, 100, 10)

if st.button("Calculate Discounted Price"):
    price=float(price)
    discounted_price = price - (price * discount / 100)
    st.write(f"Discounted Price: ${discounted_price}")
    st.table({"Original Price": [price], "Discount Percentage": [discount], "Discounted Price": [discounted_price]})

