"""
Gerenciador de cenas.
"""

from kivy.uix.screenmanager import ScreenManager

from src.scenes.splash_scene import SplashScene


class SceneManager(ScreenManager):
    """
    Gerencia todas as cenas da aplicação.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(SplashScene())

        self.current = "splash"
        print(self.screen_names)
        print(self.current)
        