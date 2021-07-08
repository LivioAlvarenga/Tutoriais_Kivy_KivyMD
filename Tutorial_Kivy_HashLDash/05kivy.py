# Tutorial de Kivy 005: um aplicativo de desenho
# http://inclem.net/2019/12/18/kivy/kivy_tutorial_005_a_drawing_app/

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)  # arguments are red, green, blue, alpha
            self.rect = Rectangle(
                size=self.size, pos=self.pos)  # retângulo branco

            Color(1, 0, 0, 1)
            Rectangle(size=(300, 100), pos=(300, 200))  # retângulo vermelho
            # posição em pixels será 300 à direita e 200 acima da parte
            #  inferior esquerda da tela. O sistema de coordenadas de Kivy
            #  segue o OpenGL usando o canto inferior esquerdo como ponto
            #  (0, 0).

        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


class DrawingApp(App):

    def build(self):
        root_widget = DrawingWidget()
        return root_widget


if __name__ == '__main__':
    DrawingApp().run()
