# https://www.youtube.com/watch?v=YynbD-netKg&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=46

from kivymd.app import MDApp
from kivy.lang import Builder


class Codemy_Tutorial_App(MDApp):

    data = {
        'Python': 'language-python',
        'Ruby': 'language-ruby',
        'JS': 'language-javascript'
    }

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('codemy_kivyMd_34_Dial_Button.kv')

    def callback(self, instance):

        if instance.icon == 'language-python':
            lang = 'Python'
        elif instance.icon == 'language-ruby':
            lang = 'Ruby'
        else:
            lang = 'JS'

        self.root.ids.my_label.text = f'A instancia é {instance.icon}'
        self.root.ids.my_mdtoolbar.title = lang

    def open(self):
        self.root.ids.my_label.text = 'Botton Open!!!'
        self.root.ids.my_mdtoolbar.title = 'Botton Open!!!'

    def close(self):
        self.root.ids.my_label.text = 'Botton Close!!!'
        self.root.ids.my_mdtoolbar.title = 'Botton Close!!!'


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
