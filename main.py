from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class AppHomeWindow(GridLayout):
   # Override parent method
   def __init__(self, **kwargs):
       # Call super to implement original functionality
       super(AppHomeWindow, self).__init__(**kwargs)

       # New functionality
       self.rows = 3
       self.add_widget(Button(text='SOS text'))
       self.add_widget(Button(text='911'))
       self.add_widget(Button(text='Fire Option'))
       self.add_widget(Button(text='Locked Out'))
       self.add_widget(Button(text='Power Outage'))
       self.add_widget(Button(text='Contact Information'))



class KidSafeApp(App):
   def build(self):
       return AppHomeWindow()

KidSafeApp().run()
