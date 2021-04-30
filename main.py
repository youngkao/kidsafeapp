from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from helpers import screen_helper
from kivy.core.window import Window

#Window.size = (300,500)



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
