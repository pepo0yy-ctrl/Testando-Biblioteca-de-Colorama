# Controle de Níveis de Água 💧

Este projeto simula um sistema simples de **monitoramento de reservatório de água** utilizando Python e a biblioteca **Colorama** para destacar mensagens com cores diferentes no terminal.

## 🎯 Objetivo
O programa recebe uma **porcentagem de 0 a 100** representando o nível do reservatório e converte esse valor em um nível de alerta (de 1 a 5). Cada nível é exibido com uma cor específica para facilitar a visualização.

## 🔢 Conversão de porcentagem para nível
- **0 a 20%** → Nível 1 (Muito baixo) → Vermelho
- **21 a 40%** → Nível 2 (Baixo) → Amarelo
- **41 a 60%** → Nível 3 (Médio) → Verde
- **61 a 80%** → Nível 4 (Alto) → Ciano
- **81 a 100%** → Nível 5 (Muito alto) → Azul

## 📦 Dependências
- Python 3.x
- Biblioteca [Colorama](https://pypi.org/project/colorama/)

Instalação do Colorama:
```bash
pip install colorama
