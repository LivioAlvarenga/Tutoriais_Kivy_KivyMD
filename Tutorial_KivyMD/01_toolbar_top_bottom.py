from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file('01_toolbar_top_bottom.kv')


class Tarefas(MDBoxLayout):

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
        # self.theme_cls.primary_palette = 'BlueGray'
        return Tarefas()


if __name__ == '__main__':
    Test_KivyMD_App().run()
