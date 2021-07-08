from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from helpers import username_helper


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        '''username = MDTextField(text='Coloque seu nome',
                               pos_hint={'center_x': 0.5, 'center_y': 0.5}, 
                               size_hint_x=None, width=200)'''

        botão = MDRectangleFlatButton(text='Hello World',
                                      pos_hint={'center_x': 0.5,
                                                'center_y': 0.4},
                                      on_release=self.show_data)

        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(botão)
        return screen

    def show_data(self, obj):

        if self.username.text == "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + ' user does not exist.'

        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Conferir usuário',
                               text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog


if __name__ == '__main__':
    DemoApp().run()

'''
1) Create a simple dialog box that opens when a button is clicked
2) Creating buttons
3) Close that dialog box when button is clicked - self.dialog.dismiss()
4) Check if username is empty or not
'''
