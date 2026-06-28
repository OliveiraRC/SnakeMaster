"""
Gerenciador de cenas do Snake Master.
"""

from kivy.uix.screenmanager import FadeTransition, ScreenManager

from src.scenes.main_menu_scene import MainMenuScene
from src.scenes.splash_scene import SplashScene


class SceneManager(ScreenManager):
    """
    Gerencia todas as telas do jogo.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(
            transition=FadeTransition(duration=0.6),
            **kwargs,
        )

        self.add_widget(SplashScene())
        self.add_widget(MainMenuScene())

        self.current = "splash"
        