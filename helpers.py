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
            #text: "911"
            background_normal: 'resources/911.png'
            on_press: root.manager.current = "noo"
        Button:
            #text: "SOS Text"
            background_normal: 'resources/help.png'
            on_press: root.manager.current = "sos"
        Button:
            #text: "Fire"
            background_normal: 'resources/fire.png'
            on_press: root.manager.current = "fire"
        Button:
            #text: "First Aid"
            background_normal: 'resources/firstaid.png'
            on_press: root.manager.current = "first_aid"
        Button:
            #text: "Stranger Danger"
            background_normal: 'resources/strangerdanger.png'
            on_press: root.manager.current = "stranger"
        Button:
            #text: "Severe Weather"
            background_normal: 'resources/weather.png'
            on_press: root.manager.current = "weather"
        Button:
            #text: "Power Outage"
            background_normal: 'resources/powerout.png'
            on_press: root.manager.current = "power_out"
        Button:
            #text: "Locked Out"
            background_normal: 'resources/lockedout.png'
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