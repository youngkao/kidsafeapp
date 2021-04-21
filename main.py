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
       #Define SOS button/functionality
       sos_btn = Button(text='SOS text')
       sos_btn.bind(on_press = self.sos_fun)
       self.add_widget(sos_btn)
       # Define 911 button/functionality
       noo_btn = Button(text='911')
       noo_btn.bind(on_press=self.noo_fun)
       self.add_widget(noo_btn)
       # Define fire button/functionality
       fire_btn = Button(text='Fire Option')
       fire_btn.bind(on_press=self.fire_fun)
       self.add_widget(fire_btn)
       # Define locked out button/functionality
       locked_out_btn = Button(text='Locked Out')
       locked_out_btn.bind(on_press=self.locked_out_fun)
       self.add_widget(locked_out_btn)
       # Define power out button/functionality
       power_out_btn = Button(text='Power Outage')
       power_out_btn.bind(on_press=self.power_out_fun)
       self.add_widget(power_out_btn)
       # Define contact info button/functionality
       contact_info_btn = Button(text='Contact Information')
       contact_info_btn.bind(on_press=self.contact_info_fun)
       self.add_widget(contact_info_btn)

   def sos_fun(self, event):
       print("button pressed, SOS")

   def noo_fun(self, event):
       print("button pressed, 911")

   def fire_fun(self, event):
       print("button pressed, fire")

   def locked_out_fun(self, event):
       print("button pressed, locked out")

   def power_out_fun(self, event):
       print("button pressed, power out")

   def contact_info_fun(self, event):
       print("button pressed, contact info")

class KidSafeApp(App):
   def build(self):
       return AppHomeWindow()

KidSafeApp().run()
