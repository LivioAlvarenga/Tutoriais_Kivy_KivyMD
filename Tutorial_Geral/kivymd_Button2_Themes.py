from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.button import (MDIconButton, MDFloatingActionButton,
                               MDFlatButton, MDRectangleFlatButton)


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = '900'
        self.theme_cls.theme_style = 'Dark'

        tela = Screen()

        btn1 = MDFlatButton(text='Hello World',
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})

        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.5,
                                               'center_y': 0.4})

        btn3 = MDIconButton(icon="language-python",
                            pos_hint={'center_x': 0.5, 'center_y': 0.3})

        btn2 = MDRectangleFlatButton(text='Hello World',
                                     pos_hint={'center_x': 0.5,
                                               'center_y': 0.6})

        tela.add_widget(btn)
        tela.add_widget(btn1)
        tela.add_widget(btn2)
        tela.add_widget(btn3)

        return tela


if __name__ == '__main__':
    DemoApp().run()

# 1) What is a theme?
# 2) primary_palette on buttons
# 3) Color Options in primary_palette - Available options are: ‘Red’, ‘Pink’,
#    ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’,
#    ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’,
#    ‘Brown’, ‘Gray’, ‘BlueGray’.
# 4) Primary hue option - ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’,
#    ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’.
# 4) theme_style - Dark or Light two options
