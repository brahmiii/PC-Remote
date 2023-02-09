from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import clientstream
import clientt
from threading import Thread
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
speed=0
connected=0
upd_stream=0

#self.manager.get_screen("third").ids.live.source="recieve.png"
#Define our different screens
class FirstWindow(Screen):
    def __init__(self, **kwargs):
        super(FirstWindow, self).__init__(**kwargs)
        Window.bind(mouse_pos = self.on_mouse_pos)
    def on_mouse_pos(self, instance, pos):
        #if self.ids.control.collide_point(*pos)and self.manager.current=="first" :
        pass
    def spinner_clicked(self, value):
        self.manager.transition.direction = "left"
        if value=="Control":
            self.manager.current="second"
        if value=="Stream":
            self.manager.current="third"
        self.ids.spinner_id.text=""
    def connect(self):
        global connected
        if connected==0:
            try:
                clientt.main(self.ids.text.text)
                self.ids.input_sign.text="Connected!"
                self.ids.input_sign.color="green"
                self.ids.connection_img.source="disconnect.jpg"
                self.ids.spinner_id.disabled=False
                
                connected=1
            except:
                self.ids.input_sign.text="Host Not Found! try again"
                self.ids.input_sign.color="red"
                
                clientt.s.close()
        elif connected==1:
            clientt.send_text("disconnect")
            try:
                clientt.s.close()
                
            except:
                pass
            connected=0
            self.ids.connection_img.source="connect.jpg"
            self.ids.input_sign.text="Disconnected!"
            self.ids.input_sign.color="red"
            self.ids.spinner_id.disabled=True
            
    def valide(self):
        if len(self.ids.text.text)!=0:
            self.ids.stats.disabled=False
        else:
            self.ids.stats.disabled=True
    def quit(self):
        clientt.send_text("disconnect")
        try:
            clientt.s.close()
            
        except:
            pass
        exit()

class SecondWindow(Screen):
    def spinner_clicked(self, value):
        
        
        if value=="Stream":
            self.manager.transition.direction = "left"
            self.manager.current="third"
        if value=="Leave":
            self.manager.transition.direction = "right"
            self.manager.current="first"
        self.ids.spinner_id.text=""
    def scrollup(self):
        clientt.send_click("scrollup")
    def scrolldown(self):
        clientt.send_click("scrolldown")
        
        
        
    def up_press(self):
        clientt.send_click("up")
        self.ids.up_img.source="up_pressed.jpg"
    def up_release(self):
        self.ids.up_img.source="up_normal.jpg"
        
    def left_press(self):
        clientt.send_click("left")
        self.ids.left_img.source="left_pressed.jpg"
    def left_release(self):
        self.ids.left_img.source="left_normal.jpg"
        
    def right_press(self):
        clientt.send_click("right")
        self.ids.right_img.source="right_pressed.jpg"
    def right_release(self):
        self.ids.right_img.source="right_normal.jpg"
        
    def down_press(self):
        clientt.send_click("down")
        self.ids.down_img.source="down_pressed.jpg"
    def down_release(self):
        self.ids.down_img.source="down_normal.jpg"
        
        
        

    def right_click(self):
        clientt.send_click("right_click")
    def left_click(self):
        clientt.send_click("left_click")
    def text(self,widget):
        clientt.send_text("text"+self.ids.sendingmsg.text)
        
    def enter(self):
        clientt.send_text("enter")
    def backspace(self):
        clientt.send_text("backspace")
        try:
            self.ids.sendingmsg.text=self.ids.sendingmsg.text.replace(self.ids.sendingmsg.text[-1],"")
        except:
            pass
    def speed(self):
        global speed
        if speed==0:
            speed=1
            clientt.send_text("speedup")
        else:
            speed=0
            clientt.send_text("speednormal")
class ThirdWindow(Screen):
    def spinner_clicked(self, value):
        self.manager.transition.direction = "right"
        if value=="Control":
            self.manager.current="second"
        if value=="Leave":
            self.manager.current="first"
        self.ids.spinner_id.text=""
    def live_stream(self):
        self.ids.live.reload()
    
class WindowManager(ScreenManager):
	pass

# Designate Our .kv design file 
kv = Builder.load_file('client.kv')


class client(App):
    def on_start(self):
        self.function_interval=Clock.schedule_interval(self.update_label, 1)
    def update_label(self, *args):
        pass
        
        
        
        
    def build(self):
        return kv

if __name__ == '__main__':
	client().run()