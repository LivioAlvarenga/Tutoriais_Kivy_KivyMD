from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineListItem
from helpers import list_helper2


class DemoApp(MDApp):

    def build(self):
        scrow_list = Builder.load_string(list_helper2)
        return scrow_list

    def on_start(self):
        for i in range(20):
            item = ThreeLineListItem(
                text='Item ' + str(i + 1),
                secondary_text=f'Segundo texto da lista {str(i + 1)}',
                tertiary_text=f'Terceiro texto da lista {str(i + 1)}'
            )
            self.root.ids.container.add_widget(item)


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
