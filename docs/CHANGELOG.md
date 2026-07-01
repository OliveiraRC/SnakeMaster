# Changelog

Todas as mudanças importantes deste projeto serão registradas neste documento.

---

## [0.1.0] - 2026-06

### Added

- Estrutura inicial
- Organização do projeto
- Classe Application
- Classe Engine
- Primeira janela

### Changed

- Remoção do emoji inicial


## [0.2.0] - Em desenvolvimento

### Added

- SceneManager
- BaseScene
- SplashScene
- MainMenuScene
- Sistema de transição entre cenas
- Configurações centralizadas
- FadeTransition

### Changed

- Application agora delega a navegação ao SceneManager.
- SplashScene reorganizada para utilizar FloatLayout como layout raiz.
- A Splash Screen agora navega automaticamente para o Menu Principal.


## [0.3.0] - Em desenvolvimento

### Added

- Estrutura inicial do UI Kit.
- Componente `CenteredLayout`.
- Componente `TitleLabel`.
- Componente `SubtitleLabel`.
- Componente `FooterLabel`.

### Changed

- Definida a arquitetura de componentes reutilizáveis para a interface.

### Changed

- Criado o componente BaseLabel para centralizar o comportamento comum dos componentes de texto.
- Os componentes TitleLabel, SubtitleLabel e FooterLabel passaram a herdar de BaseLabel.