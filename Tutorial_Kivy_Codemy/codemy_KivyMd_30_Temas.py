# https://www.youtube.com/watch?v=bcWi_H2OqLQ&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=43

from kivymd.app import MDApp
from kivy.lang import Builder


class Codemy_Tutorial_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Red'
        return Builder.load_file('codemy_KivyMd_30_Temas.kv')


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
