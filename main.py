from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class AppHomeWindow(GridLayout):
   # Override parent method
   def __init__(self, **kwargs):
       # Call super to implement original functionality
       super(AppHomeWindow, self).__init__(**kwargs)

       # New functionality
       self.cols = 2
       # Define 911 button/functionality
       noo_btn = Button(text='911')
       noo_btn.bind(on_press=self.noo_fun)
       self.add_widget(noo_btn)
       #Define SOS button/functionality
       sos_btn = Button(text='SOS text')
       sos_btn.bind(on_press = self.sos_fun)
       self.add_widget(sos_btn)
       # Define fire button/functionality
       fire_btn = Button(text='Fire')
       fire_btn.bind(on_press=self.fire_fun)
       self.add_widget(fire_btn)
       # Define first aid button/functionality
       first_aid_btn = Button(text='First Aid')
       first_aid_btn.bind(on_press=self.first_aid_fun)
       self.add_widget(first_aid_btn)
       # Define stranger danger button/functionality
       stranger_btn = Button(text='Stranger Danger')
       stranger_btn.bind(on_press=self.stranger_fun)
       self.add_widget(stranger_btn)
       # Define severe weather button/functionality
       weather_btn = Button(text='Severe Weather')
       weather_btn.bind(on_press=self.weather_fun)
       self.add_widget(weather_btn)
       # Define power out button/functionality
       power_out_btn = Button(text='Power Outage')
       power_out_btn.bind(on_press=self.power_out_fun)
       self.add_widget(power_out_btn)
       # Define locked out button/functionality
       locked_out_btn = Button(text='Locked Out')
       locked_out_btn.bind(on_press=self.locked_out_fun)
       self.add_widget(locked_out_btn)
       # Define contact info button/functionality
       contact_info_btn = Button(text='Contact Information')
       contact_info_btn.bind(on_press=self.contact_info_fun)
       self.add_widget(contact_info_btn)
       # Define parental control button/functionality
       parent_btn = Button(text='Parental Control')
       parent_btn.bind(on_press=self.parent_fun)
       self.add_widget(parent_btn)

   def noo_fun(self, event):
       print("button pressed, 911")

   def sos_fun(self, event):
       print("button pressed, SOS")

   def fire_fun(self, event):
       print("button pressed, fire")

   def first_aid_fun(self, event):
       print("button pressed, first aid")

   def stranger_fun(self, event):
       print("button pressed, stranger danger")

   def weather_fun(self, event):
       print("button pressed, severe weather")

   def power_out_fun(self, event):
       print("button pressed, power out")

   def locked_out_fun(self, event):
       print("button pressed, locked out")

   def contact_info_fun(self, event):
       print("button pressed, contact info")

   def parent_fun(self, event):
       print("button pressed, parental control")


class KidSafeApp(App):
   def build(self):
       return AppHomeWindow()

KidSafeApp().run()
