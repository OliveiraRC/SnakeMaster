"""
Classe base para todas as cenas do Snake Master.
"""

from kivy.uix.screenmanager import Screen


class BaseScene(Screen):
    """
    Classe base de todas as cenas.

    Centraliza comportamentos comuns e facilita a
    evolução futura da arquitetura.
    """

    def on_enter(self):
        """Executado quando a cena se torna ativa."""
        pass

    def on_leave(self):
        """Executado quando a cena deixa de ser ativa."""
        pass
    