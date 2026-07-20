# ✈️ OpenSky - Sistema de Monitoramento de Tráfego Aéreo

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![API](https://img.shields.io/badge/OpenSky-API-orange.svg)](https://opensky-network.org/)

> Pipeline de dados em Python para coleta, análise e monitoramento de voos em tempo real sobre o Brasil.

---

## 📋 Sobre o Projeto

Este projeto implementa um sistema completo de monitoramento de tráfego aéreo utilizando a API pública da [OpenSky Network](https://opensky-network.org/). Ele coleta dados de voos em tempo real sobre o Brasil, identifica rotas congestionadas e detecta anomalias em altitudes.

### 🎯 Objetivos

- ✅ Coletar dados de voos em tempo real via API REST
- ✅ Identificar as rotas mais congestionadas do espaço aéreo brasileiro
- ✅ Detectar anomalias como quedas bruscas de altitude
- ✅ Gerar relatórios e visualizações para análise
- ✅ Criar uma base de dados histórica para estudos futuros

---

## 🚀 Tecnologias Utilizadas

| Tecnologia  | Versão | Finalidade                     |
| ----------- | ------ | ------------------------------ |
| Python      | 3.8+   | Linguagem principal            |
| Requests    | 2.28+  | Consumo da API OpenSky         |
| JSON        | -      | Armazenamento de dados         |
| Matplotlib  | 3.5+   | Visualização de gráficos       |
| Pandas      | 1.5+   | Análise e manipulação de dados |
| Collections | -      | Contagem de frequência         |

---

## 🛠️ Instalação e Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/Julijolie/OpenSky.git
cd OpenSky
```
