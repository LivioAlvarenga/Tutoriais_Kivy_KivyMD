# Tutorial 007 do Kivy: Apresentando a linguagem kv
# http://inclem.net/2019/12/18/kivy/kivy_tutorial_007_introducing_kv_language/

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('07kivy.kv')


class DrawingWidget(Widget):
    pass


class Interface(BoxLayout):
    pass


class HashLDash_Tutorial_App(App):

    def build(self):
        root_widget = Interface()
        return root_widget


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
