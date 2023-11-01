import streamlit as st
import threading
# from azure_websocket import websocket_azure

companies = ["Apple", "Google", "Microsoft"] 

st.title("Websocket App")

if st.button("Update List"):
    companies = st.text_input("Enter companies separated by commas").title().split(",")

st.write("Updated Companies")
for company in companies:
    st.write(company)

# Access updated list
print(companies)

import websocket2

st.title("Websocket App") 

# Start websocket in background thread
threading.Thread(target=websocket2.websocket_azure).start()


## running python script
# import websocket
# import _thread
# import time
# import rel
# import requests
# from datetime import datetime
# from bs4 import BeautifulSoup

# def on_message(ws, message):
#   '''
#   Defines the steps that need to be taken once a message is received 
#   '''
#   print('-----------------------New Message received-------------------------------------')
#   print(f'Message received  : {message}')

#   print(type(message))
#   # headers = {'Content-Type': 'text/html'}
#   url = 'https://processingmessage.azurewebsites.net/api/http_trigger'
#   response = requests.post(url, data=message)
#   print(f'request send,response: {response}')




# def on_error(ws, error):
#   print(f'-----------------------------------------Error:{error}---------------------')

# def on_close(ws, close_status_code, close_msg):
#     print("### closed ###")

# def on_open(ws):
#     print("----------------------------Opened connection-------------------------------")

# def websocket_azure():
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("wss://mfn.se/all/s",
#                               on_open=on_open,
#                               on_message=on_message,
#                               on_error=on_error,
#                               on_close=on_close)

#     ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
#     # rel.signal(2, rel.abort)  # Keyboard Interrupt
#     rel.dispatch()


# ## running website
# websocket_azure()
