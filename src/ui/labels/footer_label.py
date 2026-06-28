"""
Componente para rodapé.
"""

from kivy.uix.label import Label


class FooterLabel(Label):
    """
    Label utilizado para informações de rodapé.
    """

    def __init__(self, text: str = "", **kwargs) -> None:
        super().__init__(
            text=text,
            font_size=14,
            halign="center",
            valign="middle",
            **kwargs,
        )

        self.bind(size=self._update_text_size)

    def _update_text_size(self, *_args) -> None:
        self.text_size = self.size
        