import websocket
import _thread
import time
# import rel
import logging
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def on_message(ws, message):
  '''
  Defines the steps that need to be taken once a message is received 
  '''
  print('-----------------------New Message received-------------------------------------')
  print(f'Message received  : {message}')
  logging.info(f'Message received  : {message}')
  print(type(message))
  # headers = {'Content-Type': 'text/html'}
  # url = 'https://processingmessage.azurewebsites.net/api/http_trigger'
  # response = requests.post(url, data=message)
  # print(f'request send,response: {response}')




def on_error(ws, error):
  print(f'-----------------------------------------Error:{error}---------------------')

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("----------------------------Opened connection-------------------------------")

def websocket_azure():
    


    max_retries = 5
    retries = 0

    while True:

      try:
        ws = ws = websocket.WebSocketApp("wss://mfn.se/all/s",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close) 
        ws.run_forever(reconnect=0)

      except websocket._exceptions.WebSocketBadStatusException as e:

        print(f'Exception :: {e}')
        retries += 1
        if retries > max_retries:
          print("Maximum retries reached, giving up")
          break
          
        print("WebSocket disconnected, reconnecting...")
        time.sleep(min(2 ** retries, 60))
        continue

      except KeyboardInterrupt:
        ws.close()
        break
    

    # websocket.enableTrace(True)
    # ws = websocket.WebSocketApp("wss://mfn.se/all/s",
    #                           on_open=on_open,
    #                           on_message=on_message,
    #                           on_error=on_error,
    #                           on_close=on_close)

    # ws.run_forever(reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    # rel.signal(2, rel.abort)  # Keyboard Interrupt
    # rel.dispatch()
# websocket_azure()
