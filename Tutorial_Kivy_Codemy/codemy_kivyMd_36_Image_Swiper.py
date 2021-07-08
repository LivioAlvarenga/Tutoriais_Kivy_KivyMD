# https://www.youtube.com/watch?v=gDLjaMF15mk&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=49

from kivymd.app import MDApp
from kivy.lang import Builder


class Codemy_Tutorial_App(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('codemy_kivyMd_36_Image_Swiper.kv')

    def on_swipe_left(self):
        indice = self.root.ids.my_swiper.get_current_index()
        # print(indice)
        if indice > 0:
            self.root.ids.my_swiper.set_current(indice-1)

        self.root.ids.my_mdtoolbar.title = 'Swiped Left ON!'
        # print('on_swipe_LEFT')

    def on_swipe_right(self):
        indice = self.root.ids.my_swiper.get_current_index()
        len_swiper = len(self.root.ids.my_swiper.get_items())-1
        # print(f'indice = {indice} - len = {len_swiper}')
        if indice < len_swiper:
            self.root.ids.my_swiper.set_current(indice+1)

        self.root.ids.my_mdtoolbar.title = 'Swiped Right ON!'
        # print('on_swipe_RIGHT')


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
