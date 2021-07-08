# https://www.youtube.com/watch?v=G-Rp41BzGxg&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=44

from kivymd.app import MDApp
from kivy.lang import Builder


class Codemy_Tutorial_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('codemy_KivyMd_31_Login.kv')

    def logger(self):
        self.root.ids.my_label.text = f'{self.root.ids.user.text}'

    def clear(self):
        self.root.ids.my_label.text = 'WELCOME'
        self.root.ids.user.text = ''
        self.root.ids.password.text = ''


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
