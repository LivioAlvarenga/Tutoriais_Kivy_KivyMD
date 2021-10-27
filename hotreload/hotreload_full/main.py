import os
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp
from manager_screens import ManagerScreens


class HotReload(App, MDApp):
    KV_FILES = {
        os.path.join(os.getcwd(), 'Tutoriais_Kivy_KivyMD',
                     'hotreload', 'hotreload_full', 'manager_screens.kv'),
        os.path.join(os.getcwd(), 'Tutoriais_Kivy_KivyMD',
                     'hotreload', 'hotreload_full', 'teste.kv'),
    }

    CLASSES = {
        "LoginScreen": 'teste',
    }
    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]

    DEBUG = 1

    def build_app(self):
        Window.bind(on_keyboard=self._rebuild)
        self.manager_screens = ManagerScreens()
        return self.manager_screens

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()


HotReload().run()
