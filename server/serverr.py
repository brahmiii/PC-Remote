import socket
from threading import Thread
import pyautogui
SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5050 # port we want to use
msg=""
separator_token = "<SEP>"
client_sockets = set()
s = socket.socket()
devices=""
kick=0
speed=25
from time import sleep
def listen_for_client(cs):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    global msg,separator_token,s,devices,kick,speed
    while True:
        
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
            if msg=="up":
                pyautogui.move(0, -speed)
            elif msg=="left":
                pyautogui.move(-speed, 0)
            elif msg=="right":
                pyautogui.move(speed, 0)
            elif msg=="down":
                pyautogui.move(0, speed)
            elif msg=="upright":
                pyautogui.move(speed, -speed)
            elif msg=="upleft":
                pyautogui.move(-speed, -speed)
            elif msg=="downright":
                pyautogui.move(speed, speed)
            elif msg=="downleft":
                pyautogui.move(-speed, speed)
            elif msg=="speedup":
                speed=speed*3
            elif msg=="speednormal":
                speed=25
            elif "text" in msg:
                text=msg.replace("text","")
                pyautogui.write(text)
            elif msg=="enter":
                pyautogui.press('enter')
            elif msg=="backspace":
                pyautogui.press('backspace')
            elif msg=="right_click":
                pyautogui.click(button='right')
            elif msg=="left_click":
                pyautogui.click(button='left')
            elif msg=="disconnect":
                client_sockets.remove(cs)
                devices=devices.replace("\n"+str(cs)[-22:-10],"")
            elif msg=="scrollup":
                pyautogui.scroll(speed)
            elif msg=="scrolldown":
                pyautogui.scroll(-speed)
            
            msg=""
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(e)
            client_sockets.remove(cs)
            devices=devices.replace("\n"+str(cs)[-22:-10],"")
        # iterate over all connected sockets
        #for client_socket in client_sockets:
            # and send the message
            #msg=msg.encode()
            #client_socket.send(msg)
        if kick==1:
            for client_socket in client_sockets:
                client_sockets.remove(cs)
                
        

def main_server():
    global msg,separator_token,s,devices
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    msg=""
    while True:
        # we keep listening for new connections all the time
        client_socket, client_address = s.accept()
        if not client_address[0] in devices:
            devices=devices +"\n" +str(client_address[0])
        print(f"[+] {client_address} connected.")
        # add the new connected client to connected sockets
        client_sockets.add(client_socket)
        # start a new thread that listens for each client's messages
        t = Thread(target=listen_for_client, args=(client_socket,))
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()


