from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import screen_helper

Window.size = (300, 500)


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(screen_helper)

        return screen

    def navigation_draw(self):
        print("Navigation")


if __name__ == '__main__':
    DemoApp().run()

'''
Flow of Toolbar

Screen -> Boxlayout (orientation:vertical) -> MDToolbar

Notes
1) Create a simple toolbar with a Label
2) left_action_items - Adding icon on left
- Explain lambda
- Call the navigation draw function in app.callback
3) right_action_items
4) Elevation
5) Change theme from blue to red

Bottom Toolbar
1) MDBottomAppBar
2) type:bottom
3) Change position of button - mode (end and free-end)
4) on_action_button
'''
