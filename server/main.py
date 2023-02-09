from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from threading import Thread
import serverr
import serverstream
from kivy.core.window import Window
Window.size = (950, 600)


class MyLayout(Widget):
    def on_press(self):
        if self.ids.stats.source=="on.png":
            self.ids.stats.source="off.png"
            serverr.devices=""
            serverr.kick=1
            serverr.s.close()
            
            self.ids.server.color="red"
        else:
            self.ids.stats.source="on.png"
            serverr.kick=0
            srv = Thread(target=serverr.main_server, args=())
            srv.daemon = True
            srv.start()
            self.ids.server.color="green"
        
        
     
     
    
       
class serverapp(App):

    
    
    
    def on_start(self):
        
            
        self.function_interval=Clock.schedule_interval(self.update_label, 0.0)
            
       


    
    def update_label(self, *args):
        self.root.ids.ip.text="Host: "+str(serverr.SERVER_HOST)
        if serverr.devices=="":
            self.root.ids.devices.text="No Devices Connected!"
        else:
            self.root.ids.devices.text="Devices Connected:  "+serverr.devices
    def stop_interval(self, *args):
        self.function_interval.cancel()
    def build(self):
        
        return MyLayout()
    
    
serverapp().run()


