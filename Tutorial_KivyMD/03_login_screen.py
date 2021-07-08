from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('03_login_screen.kv')


class Gerenciador(ScreenManager):
    pass


class Login(Screen):
    pass


class Tarefas(Screen):

    def robot_function(self):
        print('robot_function ACTIVATE')

    def left_function(self):
        print('left_function ACTIVATE')

    def right_function(self):
        print('right_function ACTIVATE')


class Test_KivyMD_App(MDApp):
    icon = 'Tutoriais_Kivy_KivyMD/Icones/Produtivese.png'

    def build(self):
        self.title = 'My KivyMD APP'
        self.theme_cls.theme_style = 'Light'
        return Gerenciador()


if __name__ == '__main__':
    Test_KivyMD_App().run()
