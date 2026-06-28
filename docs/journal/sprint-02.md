# Sprint 02

## Story 2.1

### Objetivo

Introduzir um sistema de gerenciamento de cenas.

### Resultado

A aplicação deixou de conhecer diretamente a interface e passou a utilizar um SceneManager baseado no ScreenManager do Kivy.

### Story 2.1.1

#### Refatoração

A SplashScene passou a utilizar um FloatLayout como contêiner raiz, preparando a interface para futuras evoluções como logotipo, barra de carregamento, animações e efeitos visuais.

### Próxima Story

Criar transições entre cenas e implementar uma Splash Screen temporizada.

## Story 2.2

### Objetivo

Implementar a navegação inicial da aplicação.

### Concluído

- MainMenuScene criada.
- Splash Screen temporizada.
- FadeTransition implementada.
- Navegação automática.

### Resultado

A aplicação agora possui um fluxo inicial semelhante ao de um jogo profissional.