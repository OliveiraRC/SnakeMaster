"""
Primeira tela exibida pelo jogo.
"""

from kivy.uix.label import Label

from src.scenes.base_scene import BaseScene


class SplashScene(BaseScene):
    """
    Cena inicial do Snake Master.
    """

    def __init__(self, **kwargs):
        super().__init__(name="splash", **kwargs)

        self.add_widget(
            Label(
                text="Snake Master\n\nEngine v0.1.0",
                font_size=28,
                halign="center",
                valign="middle",
            )
        )
        