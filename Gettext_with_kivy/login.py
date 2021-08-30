from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from language import set_language

idioma = 'pt_BR'


class my_App(MDApp):

    _ = set_language(idioma).gettext

    language = StringProperty('pt_BR')
    label1 = StringProperty(_('BEM VINDO'))
    username = StringProperty(_('Usuário'))
    password = StringProperty(_('Senha'))
    login = StringProperty(_('Entrar'))
    cleaner = StringProperty(_('Limpar'))
    change = StringProperty(_('Trocar idioma'))

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('login.kv')

    def logger(self):
        self.root.ids.my_label.text = f'{self.root.ids.user.text}'

    def clear(self):
        self.root.ids.my_label.text = self.label1
        self.root.ids.user.text = ''
        self.root.ids.senha.text = ''

    def change_language(self, lang):
        print(f'{lang = }\n{self.language = }\n{self.label1 = }')
        self.language = lang

    def on_language(self, instance, lang):
        print(f'{lang = }\n{instance = }')


if __name__ == '__main__':
    my_App().run()
