# Tutorial de Kivy 009: Concluindo o aplicativo de desenho
# http://inclem.net/2019/12/18/kivy/kivy_tutorial_009_finishing_the_drawing_app/

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import ListProperty, NumericProperty
from kivy.lang import Builder

Builder.load_file('09kivy.kv')


class DrawingWidget(Widget):
    target_colour_rgb = ListProperty([0, 0, 0])
    target_width_px = NumericProperty(0)

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        if not self.collide_point(*touch.pos):
            return

        with self.canvas:
            Color(*self.target_colour_rgb)
            self.line = Line(points=[touch.pos[0], touch.pos[1]],
                             width=self.target_width_px)

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return

        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]

    def on_target_colour_rgb(self, instance, value):
        print(f"target_colour_rgb changed to {self.target_colour_rgb}")


class Interface(BoxLayout):
    pass


class HashLDash_Tutorial_App(App):

    def build(self):
        root_widget = Interface()
        return root_widget


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
