import streamlit as st

def calculate_value(item, num, items):
    if item in items:
        return items.index(item) * num
    return "NULL"

items = ["item_0", "item_1", "item_2", "item_3", "item_4", "item_5", "item_6"]

st.title("Item Calculator")
st.write("Select your item and enter a number below.")

selected_item = st.selectbox("Select an item:", items)
num = st.number_input("What is the number:", min_value=0, step=1)

if st.button("Calculate"):
    result = calculate_value(selected_item, num, items)
    st.success(f"Result: {result}")
