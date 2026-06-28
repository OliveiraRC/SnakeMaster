"""
Snake Master

Application

Responsável pelo ciclo de vida da aplicação.
"""

from kivy.app import App
from src.config.settings import Settings

from src.engine.engine import Engine
from src.managers.scene_manager import SceneManager


class Application(App):
    """
    Classe principal da aplicação.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.engine = Engine()

    def build(self):
        """
        Inicializa a aplicação.
        """
        self.title = Settings.APP_TITLE

        self.engine.initialize()

        return SceneManager()
        