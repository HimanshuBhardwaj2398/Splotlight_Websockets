import websocket
# import threading 
import requests
def on_message(ws, message):
  '''
  Defines the steps that need to be taken once a message is received 
  '''
  print('-----------------------New Message received-------------------------------------')
  print(f'Message received  : {message}')

  print(type(message))
  # headers = {'Content-Type': 'text/html'}
#   url = 'https://processingmessage.azurewebsites.net/api/http_trigger'
#   response = requests.post(url, data=message)
  print(f'request send,response: {response}')


def on_error(ws, error):
  print(f'-----------------------------------------Error:{error}---------------------')

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("----------------------------Opened connection-------------------------------")
  
  # websocket logic

def websocket_azure():
  while True:
    try:
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://mfn.se/all/s",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,)
        ws.run_forever(ping_interval=10,reconnect=1)
    except Exception as e:
       print(f"Error: {e}")
