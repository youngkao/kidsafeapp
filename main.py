from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

#Window.size = (300,500)

screen_helper = """
ScreenManager:
    HomeScreen:
    NOOScreen:
    SOSScreen:
    FireScreen:
    FirstAidScreen:
    StrangerScreen:
    WeatherScreen:
    PowerOutScreen:
    LockedOutScreen:
    ContactInfoScreen:
    ParentScreen:
    

<HomeScreen>:
    name: "home"
    MDGridLayout:
        cols: 2
        Button:
            text: "911"
            on_press: root.manager.current = "noo"
        Button:
            text: "SOS Text"
            on_press: root.manager.current = "sos"
        Button:
            text: "Fire"
            on_press: root.manager.current = "fire"
        Button:
            text: "First Aid"
            on_press: root.manager.current = "first_aid"
        Button:
            text: "Stranger Danger"
            on_press: root.manager.current = "stranger"
        Button:
            text: "Severe Weather"
            on_press: root.manager.current = "weather"
        Button:
            text: "Power Outage"
            on_press: root.manager.current = "power_out"
        Button:
            text: "Locked Out"
            on_press: root.manager.current = "locked_out"
        Button:
            text: "Contact Information"
            on_press: root.manager.current = "contact_info"
        Button:
            text: "Parental Control"
            on_press: root.manager.current = "parent"

<NOOScreen>:
    name: "noo"
    MDLabel:
        text: "Calling 911..."
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

<SOSScreen>:
    name: "sos"
    MDLabel:
        text: "Calling SOS Contacts..."
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<FireScreen>:
    name: "fire"
    MDLabel:
        text: "Fire info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<FirstAidScreen>:
    name: "first_aid"
    MDLabel:
        text: "First aid info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<StrangerScreen>:
    name: "stranger"
    MDLabel:
        text: "Stranger Danger!"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<WeatherScreen>:
    name: "weather"
    MDLabel:
        text: "Severe weather info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<PowerOutScreen>:
    name: "power_out"
    MDLabel:
        text: "Power out info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<LockedOutScreen>:
    name: "locked_out"
    MDLabel:
        text: "Locked out info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<ContactInfoScreen>:
    name: "contact_info"
    MDLabel:
        text: "Enter contact info here"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
        
<ParentScreen>:
    name: "parent"
    MDLabel:
        text: "Set parent credentials here"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
"""

class NOOScreen(Screen):
    pass

class SOSScreen(Screen):
    pass

class FireScreen(Screen):
    pass

class FirstAidScreen(Screen):
    pass

class StrangerScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class PowerOutScreen(Screen):
    pass

class LockedOutScreen(Screen):
    pass

class ContactInfoScreen(Screen):
    pass

class ParentScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(NOOScreen(name="noo"))
sm.add_widget(SOSScreen(name="sos"))
sm.add_widget(FireScreen(name="fire"))
sm.add_widget(FirstAidScreen(name="first_aid"))
sm.add_widget(StrangerScreen(name="stranger"))
sm.add_widget(WeatherScreen(name="weather"))
sm.add_widget(PowerOutScreen(name="power_out"))
sm.add_widget(LockedOutScreen(name="locked_out"))
sm.add_widget(ContactInfoScreen(name="contact_info"))
sm.add_widget(ParentScreen(name="parent"))

class KidSafeApp(MDApp):
   def build(self):
       self.theme_cls.primary_palette = "Green"
       self.theme_cls.primary_hue = "A700"
       self.theme_cls.theme_style = "Dark"

       screen = Builder.load_string(screen_helper)
       return screen



KidSafeApp().run()
