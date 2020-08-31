from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper
from helpers import password_helper


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Brown"
        # username = MDTextField(text='Enter username',
        #                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                       size_hint_x=None, width=300)
        button = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is "" or self.password.text is "":
            check_string = 'Please enter a username and/or password.'
        else:
            check_string = self.username.text + ' is invalid'
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More', on_release=self.more_dialog)
        self.dialog = MDDialog(title="Username and Password Check", text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def more_dialog(self, obj):
        close_button = MDFlatButton(text='Close', on_release=self.close_moredialog)
        self.moredialog = MDDialog(title="Stay tuned for more features!",
                                   size_hint=(0.7, 1),
                                   buttons=[close_button])
        self.moredialog.open()

    def close_moredialog(self, obj):
        self.moredialog.dismiss()
        self.dialog.dismiss()


DemoApp().run()
