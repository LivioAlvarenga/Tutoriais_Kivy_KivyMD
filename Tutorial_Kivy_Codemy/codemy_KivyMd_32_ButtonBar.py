# https://www.youtube.com/watch?v=G-Rp41BzGxg&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=44

from kivymd.app import MDApp
from kivy.lang import Builder


class Codemy_Tutorial_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('codemy_KivyMd_32_ButtonBar.kv')

    def presser(self):
        self.root.ids.my_label.text = 'Botão toolbar pressionado!'
        self.root.ids.top_toolbar.title = 'Botão toolbar pressionado!'

    def presser1(self):
        self.root.ids.my_label.text = 'Botão menu pressionado!'
        self.root.ids.top_toolbar.title = 'Botão menu pressionado!'


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
