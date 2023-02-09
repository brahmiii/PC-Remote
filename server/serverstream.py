import socket
from threading import Thread

import pyautogui
def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
    server.bind(('192.168.1.16', 8080))  # 127.0.0.1
    server.listen()

    client_socket, client_address = server.accept()
    im2 = pyautogui.screenshot('stream.jpg')
    
    file = open('stream.jpg', 'rb')
    image_data = file.read(2048)

    while image_data:
    
        client_socket.send(image_data)
        image_data = file.read(2048)
    file.close()
def server_stream():
    while True:
        try:
            server()
        except:
            pass
srv = Thread(target=server_stream)
srv.daemon = True
srv.start()        

    