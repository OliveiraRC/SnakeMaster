"""
Snake Master

Ponto de entrada da aplicação.
"""

from src.core.application import Application


def main() -> None:
    """
    Inicializa a aplicação.
    """
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
    