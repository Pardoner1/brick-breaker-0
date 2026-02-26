# Brick Breaker Game 🧱

Um clássico jogo Brick Breaker desenvolvido em Python com Pygame. Disponível para Desktop e Mobile!

## 🎮 Sobre o Projeto

Este é um jogo Brick Breaker onde o jogador controla uma raquete para rebater uma bola e destruir todos os blocos na tela. O jogo conta com:
- Múltiplas fases
- Sistema de pontuação
- Efeitos sonoros
- Versão otimizada para dispositivos móveis

## 🚀 Versões

- **Desktop**: Versão principal com controles por teclado
- **Mobile**: Branch separada com controles touch e otimizações para celular

## 📋 Pré-requisitos

- Python 3.8+
- Pygame 2.0+

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Pardoner1/brick-breaker-0.git
cd brick-breaker-0
```
2. Instale as dependências:
```
pip install pygame
```
🎯 Como Jogar
Versão Desktop:
Use as setas ← → para mover a raquete

Pressione ESPAÇO para iniciar/sacar a bola

ESC para pausar

Versão Mobile (branch mobile):
Arraste o dedo na tela para mover a raquete

Toque para iniciar o jogo

🏗️ Estrutura do Projeto
```
brick-breaker-0/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── sprites.py
│   └── utils.py
├── assets/
│   ├── sounds/
│   └── images/
├── .gitignore
└── README.md
```
🤝 Contribuindo
Contribuições são sempre bem-vindas! Veja como:

Faça um fork do projeto

Crie sua branch de feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📌 Roadmap
Adicionar power-ups

Modo multiplayer local

Ranking de pontuações

Mais níveis com layouts diferentes

Efeitos visuais avançados

✨ Melhorias Futuras
Sistema de salvamento de progresso

Temas customizáveis

Diferentes tipos de blocos (indestrutíveis, especiais)

Modo infinito

📝 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

📧 Contato
Link do Projeto: https://github.com/Pardoner1/brick-breaker-0

🎯 Agradecimentos
Pygame community

Todos os contribuidores


## 💡 Dicas Adicionais para Versionamento

1. **Para a branch mobile**, certifique-se de que o `.gitignore` também inclua:
   - Arquivos do buildozer (se usar para Android)
   - Pastas `.buildozer` e `bin/`
   - Arquivos `.apk` gerados

2. **Antes de fazer commit**, sempre verifique com:
```bash
git status
```
