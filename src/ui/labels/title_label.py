"""
Componente de título.
"""

from src.ui.labels.base_label import BaseLabel


class TitleLabel(BaseLabel):
    """
    Label utilizado para títulos principais.
    """

    def __init__(self, text: str = "", **kwargs) -> None:
        super().__init__(
            text=text,
            font_size=34,
            bold=True,
            **kwargs,
        )
        