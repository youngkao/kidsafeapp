from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import Button

class KidSafeApp(MDApp):
   def build(self):
       self.theme_cls.primary_palette = "Green"
       self.theme_cls.primary_hue = "A700"
       self.theme_cls.theme_style = "Dark"

       screen = Screen()
       btn_grid = MDGridLayout(cols=2)
       screen.add_widget(btn_grid)

       # Define 911 button/functionality
       noo_btn = Button(text='911', on_press=self.noo_fun)
       btn_grid.add_widget(noo_btn)
       # Define SOS button/functionality
       sos_btn = Button(text='SOS text', on_press=self.sos_fun)
       btn_grid.add_widget(sos_btn)
       # Define fire button/functionality
       fire_btn = Button(text='Fire', on_press=self.fire_fun)
       btn_grid.add_widget(fire_btn)
       # Define first aid button/functionality
       first_aid_btn = Button(text='First Aid', on_press=self.first_aid_fun)
       btn_grid.add_widget(first_aid_btn)
       # Define stranger danger button/functionality
       stranger_btn = Button(text='Stranger Danger', on_press=self.stranger_fun)
       btn_grid.add_widget(stranger_btn)
       # Define severe weather button/functionality
       weather_btn = Button(text='Severe Weather', on_press=self.weather_fun)
       btn_grid.add_widget(weather_btn)
       # Define power out button/functionality
       power_out_btn = Button(text='Power Outage', on_press=self.power_out_fun)
       btn_grid.add_widget(power_out_btn)
       # Define locked out button/functionality
       locked_out_btn = Button(text='Locked Out', on_press=self.locked_out_fun)
       btn_grid.add_widget(locked_out_btn)
       # Define contact info button/functionality
       contact_info_btn = Button(text='Contact Information', on_press=self.contact_info_fun)
       btn_grid.add_widget(contact_info_btn)
       # Define parental control button/functionality
       parent_btn = Button(text='Parental Control', on_press=self.parent_fun)
       btn_grid.add_widget(parent_btn)

       return screen


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

KidSafeApp().run()
