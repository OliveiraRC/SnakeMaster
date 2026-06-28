"""
Layout reutilizável centralizado.
"""

from kivy.uix.floatlayout import FloatLayout


class CenteredLayout(FloatLayout):
    """
    Layout base para telas do jogo.

    Todos os widgets adicionados a este layout
    utilizam posicionamento livre do FloatLayout.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        