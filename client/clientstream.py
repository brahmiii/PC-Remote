import socket
from threading import Thread
from time import sleep

def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
    client.connect(('192.168.1.16', 8080))  # 127.0.0.1
    file = open('recieve.jpg', "wb")
    
    image_chunk = client.recv(2048)  # stream-based protocol
    
    while image_chunk:
        file.write(image_chunk)
        image_chunk = client.recv(2048)
    file.close()
    
def client_stream():
    while True:
        try:
            client()
            sleep(1.5)
        except:
            pass
srv = Thread(target=client_stream)
srv.daemon = True
srv.start()