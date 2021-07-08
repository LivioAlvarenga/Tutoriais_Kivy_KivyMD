# https://www.youtube.com/watch?v=YynbD-netKg&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=46

from kivymd.app import MDApp
from kivy.lang import Builder


class Codemy_Tutorial_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('codemy_kivyMd_33_NavBar_Icon.kv')


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
