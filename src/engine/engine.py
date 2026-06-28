"""
Snake Master

Engine

Responsável por coordenar os componentes centrais da Engine.
"""


class Engine:
    """
    Classe principal da Engine.

    Nesta versão inicial ela apenas registra seu estado.
    Futuramente será responsável por inicializar
    SceneManager, ResourceManager, AudioManager,
    EventManager e outros componentes.
    """

    def __init__(self) -> None:
        """Inicializa a Engine."""
        self.initialized = False

    def initialize(self) -> None:
        """Inicializa os componentes da Engine."""
        self.initialized = True
        