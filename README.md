# OpenSky - Sistema de Monitoramento de Tráfego Aéreo

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![API](https://img.shields.io/badge/OpenSky-API-orange.svg)](https://opensky-network.org/)

> Pipeline de dados em Python para coleta, análise e monitoramento de voos em tempo real sobre o Brasil.

---

## Sobre o Projeto

Pipeline de dados para coleta e análise de voos em tempo real, desenvolvido em Python, que consome a API pública da [OpenSky Network](https://opensky-network.org/).

O sistema realiza coletas programadas a cada 5 minutos, capturando dados de aeronaves ativas sobre o Brasil, e processa as informações para gerar insights sobre o tráfego aéreo nacional.

### 🎯 Funcionalidades

| Funcionalidade          | Descrição                                                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Coleta Automatizada** | Script executado a cada 5 minutos para captura contínua de dados                                                                                                                        |
| **Análise de Rotas**    | Identificação das rotas mais congestionadas via agrupamento por callsign                                                                                                                |
| **Busca Específica**    | Verificação de voos individuais pelo número de callsign                                                                                                                                 |
| **Ranking**             | Geração do Top 10 dos voos mais frequentes no espaço aéreo brasileiro                                                                                                                   |
| **Relatório**           | Geração de um relatório em JSON com estatísticas dos dados analisados, incluindo total de arquivos processados, total de voos, callsigns únicos e ranking das rotas mais congestionadas |
| **Arquitetura Modular** | Separação em módulos (coletor, analisador, verificador) para melhor manutenção                                                                                                          |

---

### Objetivos Futuros

- **Detecção de Anomalias:** Implementar algoritmo para identificar quedas bruscas de altitude e padrões suspeitos em voos
- **Banco de Dados:** Migrar o armazenamento de JSON para MySQL/PostgreSQL para consultas mais eficientes
- **Base Histórica:** Criar um dataset consolidado para análises preditivas e estudos de padrões de tráfego aéreo
- **Dashboard Interativo:** Desenvolver visualizações em tempo real com gráficos e mapas

---

## Tecnologias Utilizadas

| Tecnologia  | Versão | Finalidade             |
| ----------- | ------ | ---------------------- |
| Python      | 3.8+   | Linguagem principal    |
| Requests    | 2.28+  | Consumo da API OpenSky |
| JSON        | -      | Armazenamento de dados |
| Collections | -      | Contagem de frequência |

---

## Instalação e Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/Julijolie/OpenSky.git
cd OpenSky
```
