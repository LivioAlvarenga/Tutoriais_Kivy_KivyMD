# Tutorial Kivy 008: Mais linguagem kv
# http://inclem.net/2019/12/18/kivy/kivy_tutorial_008_more_kv_language/

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from random import random
from kivy.lang import Builder

Builder.load_file('08kivy.kv')


class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        if not self.collide_point(*touch.pos):
            return

        with self.canvas:
            Color(random(), random(), random())
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return

        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


class Interface(BoxLayout):
    pass


class HashLDash_Tutorial_App(App):

    def build(self):
        root_widget = Interface()
        return root_widget


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
