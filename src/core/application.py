"""
Snake Master

Application

Responsável pelo ciclo de vida da aplicação.
"""

from kivy.app import App
from kivy.uix.label import Label

from src.engine.engine import Engine


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

        self.engine.initialize()

        self.title = "Snake Master"

        return Label(
            text="Snake Master\n\nEngine v0.1.0",
            font_size=28,
            halign="center",
            valign="middle",
        )
        