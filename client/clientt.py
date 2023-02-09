import socket

from threading import Thread


s = socket.socket()




def listen_for_messages():
    global s
    image = s.recv(1024)
    #f = open("stream.png","wb")
    #while True:
        #f.close()
        #image = s.recv(1024)
        #f.write(image) 







    
        
        
        




def send_click(to_send):
    global s
    s.send(to_send.encode())

def send_text(to_send):
    global s
    s.send(to_send.encode())

def main(SERVER_HOST):
    global s
    s = socket.socket()
    SERVER_PORT = 5050 # server's port
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")
    t = Thread(target=listen_for_messages)
    t.daemon = True
    t.start()
