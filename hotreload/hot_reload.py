from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp

# ! Obs. Para hotreload funcionar precisamos instalar 'pip install watchdog'


class HotReload(MDApp):
    KV_FILES = ['Tutoriais_Kivy_KivyMD/hotreload/teste.kv']
    DEBUG = True  # Para mostrar os erros online.

    def build_app(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"
        return Builder.load_file('Tutoriais_Kivy_KivyMD/hotreload/teste.kv')


HotReload().run()
