import streamlit as st

def calculate_value(item, num, items):
    if item in items:
        return items.index(item) * num
    return "NULL"

items = ["item_0", "item_1", "item_2", "item_3", "item_4", "item_5", "item_6"]

st.title("Item Calculator")
st.write("Select the drug and enter the weight below.")

selected_item = st.selectbox("Select the drug:", items)
num = st.number_input("What is the weight:", min_value=0, step=1)

if st.button("Calculate"):
    result = calculate_value(selected_item, num, items)
    st.success(f"Result: {result}")
