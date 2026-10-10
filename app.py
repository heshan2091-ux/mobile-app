import streamlit as st

def calculate_value(drug, num, drugs):
    if drug in drugs:
        return drugs.index(drug) * num
    return "NULL"

drugs = ["drug_0", "drug_1", "drug_2", "drug_3", "drug_4", "drug_5", "drug_6"]

st.title("Drug Volume Calculator")
st.write("Select the drug and enter the weight below.")

selected_drug = st.selectbox("Select the drug:", drugs)
num = st.number_input("What is the weight:", min_value=0, step=1)

if st.button("Calculate"):
    result = calculate_value(selected_drug, num, drugs)
    st.success(f"Result: {result}")
