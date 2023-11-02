import streamlit as st
import threading
import azure_websocket
import config

st.title("Company Manager") 

companies = config.companies

for company in companies:
    st.write(company)

option = st.selectbox("Select an action", ["", "Add company", "Remove company"])

if option == "Add company":
    name = st.text_input("Enter company name")
    if st.button("Add"):
        companies.append(name) 
        config.companies.append(name)
        st.success("Company added!")

elif option == "Remove company":
    name = st.selectbox("Select company to remove", companies)
    if st.button("Remove"):
        companies.remove(str(name))
        config.companies.remove(name)
        st.success("Company removed!")
        
st.button("Refresh list")

# Start websocket in background thread
threading.Thread(target=azure_websocket.websocket_azure).start()


