---
layout: default
title: TCU 2026 - Banco de Dados de Questões
description: Análise completa e organizada das questões do TCU para 2026
---

# 📊 TCU 2026 - Banco de Dados de Questões

> **Análise completa e organizada das questões do TCU (Tribunal de Contas da União) para o concurso de 2026**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/prof-ramos/tcu-2026/blob/main/LICENSE)
[![Data](https://img.shields.io/badge/Data-Cleaned-brightgreen.svg)](https://github.com/prof-ramos/tcu-2026/tree/main/data/processed)
[![GitHub Pages](https://img.shields.io/badge/Docs-GitHub%20Pages-blue.svg)](https://prof-ramos.github.io/tcu-2026)

## 🎯 Visão Geral

Este repositório contém um **banco de dados completo e organizado** das questões do TCU para 2026, com **dados limpos e estruturados** para desenvolvimento de aplicações educacionais, análises estatísticas e ferramentas de estudo.

### ✨ Características Principais

- 📚 **1.250 registros** organizados hierarquicamente
- 🧹 **Dados 100% limpos** (zero valores nulos)
- 📊 **6 níveis hierárquicos** de organização temática
- 🔢 **Porcentagens** em formatos numérico e texto
- 📈 **293.855 questões** organizadas por disciplina

## 📊 Estatísticas dos Dados

### 📚 Disciplinas Principais

| Disciplina | Questões | Porcentagem |
|------------|----------|-------------|
| 📝 **Língua Portuguesa** | 24.913 | 21.43% |
| 🏛️ **Direito Administrativo** | 22.987 | 19.77% |
| 🏢 **Administração Geral** | 15.938 | 13.71% |
| ⚖️ **Direito Constitucional** | 15.353 | 13.21% |
| 💻 **Informática** | 8.469 | 7.28% |
| 🇺🇸 **Língua Inglesa** | 5.139 | 4.42% |
| 🔍 **Auditoria Governamental** | 2.936 | 2.53% |

### 📈 Distribuição Hierárquica

- **Nível 0** (Categorias principais): 7 registros
- **Nível 1**: 117 registros  
- **Nível 2**: 481 registros
- **Nível 3**: 400 registros
- **Nível 4**: 225 registros
- **Nível 5**: 20 registros

## 🚀 Como Usar

### 📥 Download dos Dados

**Dados Limpos (Recomendado):**
- [📊 Excel (.xlsx)](https://github.com/prof-ramos/tcu-2026/raw/main/data/processed/db-questoes-limpo.xlsx)
- [📄 CSV](https://github.com/prof-ramos/tcu-2026/raw/main/data/processed/db-questoes-limpo.csv)

### 💻 Exemplo de Uso em Python

```python
import pandas as pd

# Carregar dados limpos
df = pd.read_csv('https://github.com/prof-ramos/tcu-2026/raw/main/data/processed/db-questoes-limpo.csv')

# Filtrar por disciplina
direito_admin = df[df['topico'].str.contains('Direito Administrativo', na=False)]

# Análise por nível hierárquico
print(df['nivel_hierarquia'].value_counts().sort_index())
```

## 📁 Estrutura do Repositório

```
tcu-2026/
├── 📂 data/
│   ├── 📂 raw/           # Dados originais
│   └── 📂 processed/     # 🎯 Dados limpos (usar estes)
├── 📂 scripts/           # Scripts Python para processamento
├── 📂 docs/              # Documentação completa
├── 📄 README.md          # Documentação principal
└── 📄 LICENSE            # Licença MIT
```

## 🎯 Casos de Uso

### 📱 **Para Desenvolvedores**
- Criar sistemas de simulados online
- Desenvolver dashboards de análise
- Construir APIs para acesso aos dados
- Integrar com plataformas educacionais

### 📊 **Para Analistas de Dados**
- Identificar tópicos mais cobrados
- Analisar tendências por disciplina
- Criar visualizações interativas
- Gerar relatórios estatísticos

### 🎓 **Para Estudantes**
- Focar estudos nos tópicos mais importantes
- Entender a distribuição das questões
- Preparar simulados direcionados
- Acompanhar progresso de estudos

## 🔧 Qualidade dos Dados

✅ **Processo de Limpeza Aplicado:**

1. **Padronização** - Colunas renomeadas e formatos consistentes
2. **Limpeza** - Remoção de valores nulos e colunas vazias
3. **Enriquecimento** - Adição de níveis hierárquicos e porcentagens numéricas
4. **Validação** - Verificação de consistência e integridade dos dados

> 📋 **Relatório completo**: [Ver documentação detalhada](relatorio_limpeza.md)

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja nosso [Guia de Contribuição](CONTRIBUTING.md) para começar.

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](https://github.com/prof-ramos/tcu-2026/blob/main/LICENSE) para detalhes.

## 🔗 Links Úteis

- 🏠 [Repositório Principal](https://github.com/prof-ramos/tcu-2026)
- 📚 [Documentação Completa](https://github.com/prof-ramos/tcu-2026/tree/main/docs)
- 🐛 [Reportar Issues](https://github.com/prof-ramos/tcu-2026/issues)
- 💬 [Discussões](https://github.com/prof-ramos/tcu-2026/discussions)

---

<div align="center">
<strong>🎯 TCU 2026 - Dados organizados para o seu sucesso! 🚀</strong>
<br><br>
<a href="https://github.com/prof-ramos/tcu-2026/stargazers">⭐ Star</a> ·
<a href="https://github.com/prof-ramos/tcu-2026/fork">🍴 Fork</a> ·
<a href="https://github.com/prof-ramos/tcu-2026/issues">🐛 Issues</a>
</div>