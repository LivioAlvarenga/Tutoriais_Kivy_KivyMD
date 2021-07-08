# https://www.youtube.com/watch?v=NzUTZj31AfM&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=30

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.animation import Animation

Builder.load_file('codemy_26_Animacao.kv')


class MyLayout(Widget):
    def animate_it(self, widget, *args):
        # animação 1
        animate = Animation(background_color=get_color_from_hex('#00E676'),
                            duration=1,
                            opacity=0.1)
        # animação 2
        animate += Animation(opacity=1,
                             background_color=get_color_from_hex('#6200EA'),
                             size_hint=(1, 1),
                             duration=1)
        # animação 3
        animate += Animation(background_color=get_color_from_hex('#D50000'),
                             size_hint=(0.3, 0.3),
                             pos_hint={'center_x': .1},
                             duration=1)
        # animação 4
        animate += Animation(pos_hint={'center_x': .8},
                             duration=1)
        # animação 5
        animate += Animation(pos_hint={'center_y': 0.5},
                             duration=1)
        # animação 6
        animate += Animation(background_color=get_color_from_hex('#00E676'),
                             pos_hint={'center_x': 0.5},
                             duration=1)

        animate.start(widget)

        # criando um callback
        animate.bind(on_complete=self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = 'Callback com bind funcionando!!!'


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFB74D')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
