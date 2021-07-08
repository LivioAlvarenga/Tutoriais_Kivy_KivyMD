from kivymd.app import MDApp
from kivymd.uix.list import (TwoLineIconListItem,
                             IconLeftWidget, ImageLeftWidget)
from helpers import list_helper3
from kivy.lang.builder import Builder


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper3)
        return screen

    def on_start(self):
        for i in range(20):

            icons2 = ImageLeftWidget(
                source='Tutoriais_Kivy_KivyMD/Icones/Símbolo_2_ProdutiveSE.png'
            )
            icons = IconLeftWidget(icon="android")
            items = TwoLineIconListItem(
                text=str(i + 1) + ' - Item ',
                secondary_text=f'Segundo texto da lista {str(i + 1)}'
            )

            if (i + 1) % 2 == 0:  # Se par
                items.add_widget(icons)
            else:
                items.add_widget(icons2)

            self.root.ids.container.add_widget(items)


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
