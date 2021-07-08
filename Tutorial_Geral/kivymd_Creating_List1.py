from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from helpers import list_helper


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        list_item = Builder.load_string(list_helper)
        screen.add_widget(list_item)
        return screen


if __name__ == '__main__':
    DemoApp().run()

'''
1) Example of List -
https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists.png
2) Create -> OneLineListItem
https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/lists.gif

3) Flow to create a list : OneLineListItem-> MDList -> ScrollView -> Screen
4) Create a for loop to add more items
5) Create a TwoLineListItem(secondary_text), ThreeLineListItem (tertiary_text)

- Flow to Icon/Avatar list : IconLeftWidget/IconRightWidget ->
    OneLineListItem-> MDList -> ScrollView -> Screen
6) Add a OneLineIconListItem
7) Add a OneLineAvatarListItem

8) Use the Builder method to create a list
'''
