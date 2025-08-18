# 📊 TCU 2026 - Banco de Dados de Questões

> **Análise completa e organizada das questões do TCU (Tribunal de Contas da União) para o concurso de 2026**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Data](https://img.shields.io/badge/Data-Cleaned-brightgreen.svg)](data/processed/)
[![GitHub release](https://img.shields.io/github/v/release/prof-ramos/tcu-2026?color=blue)](https://github.com/prof-ramos/tcu-2026/releases)
[![GitHub Pages](https://img.shields.io/badge/Docs-GitHub%20Pages-blue.svg)](https://prof-ramos.github.io/tcu-2026)
[![Dataset Size](https://img.shields.io/badge/Dataset-293k%20questões-orange.svg)](data/processed/db-questoes-limpo.csv)
[![GitHub last commit](https://img.shields.io/github/last-commit/prof-ramos/tcu-2026)](https://github.com/prof-ramos/tcu-2026/commits/main)
[![GitHub contributors](https://img.shields.io/github/contributors/prof-ramos/tcu-2026)](https://github.com/prof-ramos/tcu-2026/graphs/contributors)
[![GitHub stars](https://img.shields.io/github/stars/prof-ramos/tcu-2026?style=social)](https://github.com/prof-ramos/tcu-2026/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/prof-ramos/tcu-2026?style=social)](https://github.com/prof-ramos/tcu-2026/network)

## 🎯 Sobre o Projeto

Este repositório contém um **banco de dados completo e organizado** das questões do TCU para 2026, com **dados limpos e estruturados** para desenvolvimento de aplicações educacionais, análises estatísticas e ferramentas de estudo.

### ✨ Características Principais

- 📚 **1.250 registros** organizados hierarquicamente
- 🧹 **Dados 100% limpos** (zero valores nulos)
- 📊 **6 níveis hierárquicos** de organização temática
- 🔢 **Porcentagens** em formatos numérico e texto
- 📈 **Estatísticas completas** por disciplina e subtópico

## 📁 Estrutura do Projeto

```
tcu-2026/
├── 📂 data/
│   ├── 📂 raw/                    # Dados originais (não modificar)
│   │   ├── db-questoes.xlsx       # Banco original de questões
│   │   ├── tcu-verticalizado.xlsx # Dados verticalizados
│   │   ├── tcu.csv                # Versão CSV original
│   │   └── outros arquivos...     # Dados complementares
│   └── 📂 processed/              # 🎯 DADOS LIMPOS (usar estes)
│       ├── db-questoes-limpo.xlsx # Dados principais limpos
│       └── db-questoes-limpo.csv  # Versão CSV dos dados limpos
├── 📂 scripts/                    # Scripts Python para processamento
│   ├── clean_data.py              # Script principal de limpeza
│   ├── exemplo_analise_concursos.py
│   ├── processador_excel_concursos.py
│   └── requirements.txt           # Dependências Python
├── 📂 docs/                       # Documentação completa
│   ├── relatorio_limpeza.md       # Relatório detalhado da limpeza
│   ├── claude_code_concursos_prompt.md
│   └── TCU_2021.pdf              # Documentação adicional
├── 📄 CLAUDE.md                   # Guia para desenvolvimento
└── 📄 README.md                   # Este arquivo
```

## 🚀 Como Usar

### 1. **Clone o Repositório**
```bash
git clone https://github.com/prof-ramos/tcu-2026.git
cd tcu-2026
```

### 2. **Configure o Ambiente Python**
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\\Scripts\\activate     # Windows

# Instalar dependências
pip install -r scripts/requirements.txt
```

### 3. **Use os Dados Limpos**
```python
import pandas as pd

# Carregar dados limpos (recomendado)
df = pd.read_excel('data/processed/db-questoes-limpo.xlsx')

# Ou versão CSV
df = pd.read_csv('data/processed/db-questoes-limpo.csv')

print(f"Total de registros: {len(df)}")
print(f"Disciplinas principais: {df[df['nivel_hierarquia'] == 0]['topico'].tolist()}")
```

## 📊 Estrutura dos Dados

### 🗂️ Colunas Disponíveis

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `hierarquia` | string | Código hierárquico (ex: "02.01.03") |
| `topico` | string | Nome do tópico/assunto |
| `quantidade_encontrada` | int | Número de questões encontradas |
| `porcentagem_encontrada` | string | Porcentagem em formato texto (ex: "15.30%") |
| `quantidade_caderno` | int | Quantidade no caderno oficial |
| `porcentagem_caderno` | string | Porcentagem do caderno em texto |
| `porcentagem_encontrada_num` | float | Porcentagem como número (0-100) |
| `porcentagem_caderno_num` | float | Porcentagem do caderno como número |
| `nivel_hierarquia` | int | Nível hierárquico (0=principal, 1-5=sub) |

### 📚 Disciplinas Contempladas

- **🏛️ Direito Administrativo** (19.77% - 22.987 questões)
- **📝 Língua Portuguesa** (21.43% - 24.913 questões)  
- **💻 Informática** (7.28% - 8.469 questões)
- **🏢 Administração Geral e Pública** (13.71% - 15.938 questões)
- **🔍 Auditoria Governamental e Controle** (2.53% - 2.936 questões)
- **🇺🇸 Língua Inglesa** (4.42% - 5.139 questões)
- **⚖️ Direito Constitucional** (13.21% - 15.353 questões)

### 📈 Estatísticas Gerais

- **📊 Total de Questões**: 293.855
- **📝 Total de Registros**: 1.250
- **🎯 Tópicos Únicos**: 1.246
- **📋 Níveis Hierárquicos**: 6 (0-5)
- **✅ Qualidade**: 100% (zero valores nulos)

## 🛠️ Scripts Disponíveis

### 🧹 Limpeza de Dados
```bash
cd scripts/
python clean_data.py
```

### 📊 Análise de Exemplo
```bash
python exemplo_analise_concursos.py
```

### ⚙️ Processamento Avançado
```bash
python processador_excel_concursos.py
```

## 🎯 Casos de Uso

### 📱 **Aplicações Web**
- Sistemas de simulados online
- Dashboards de análise estatística
- Plataformas de estudo personalizadas

### 🔍 **Análise de Dados**
- Identificação de tópicos mais cobrados
- Análise de tendências por disciplina
- Relatórios de distribuição de questões

### 🌐 **Extensões e APIs**
- Extensão do Chrome para estudos
- APIs REST para acesso aos dados
- Integração com outras plataformas

### 📊 **Data Science**
- Análise preditiva de questões
- Clustering de tópicos similares
- Visualizações interativas

## 🔄 Processo de Limpeza

✅ **Aplicadas as seguintes melhorias:**

1. **📝 Padronização de Nomenclatura**
   - Colunas renomeadas para padrão snake_case
   - Remoção de caracteres especiais

2. **🧹 Qualidade dos Dados**
   - Remoção de coluna vazia (`Frequência Acumulada`)
   - Tratamento de valores nulos (substituídos por `CATEGORIA_PRINCIPAL`)
   - Limpeza de espaços em branco

3. **🔢 Conversão de Formatos**
   - Porcentagens convertidas para formato numérico
   - Padronização de tipos de dados

4. **📊 Enriquecimento**
   - Adição de coluna `nivel_hierarquia`
   - Ordenação lógica por hierarquia
   - Validação de consistência

> 📋 **Relatório completo**: Veja `docs/relatorio_limpeza.md` para detalhes

## 🤝 Contribuindo

1. **Fork** o repositório
2. **Clone** seu fork
3. **Crie** uma branch para sua feature
4. **Commit** suas mudanças
5. **Push** para a branch
6. **Abra** um Pull Request

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🎓 Relevância Acadêmica

Este dataset é especialmente útil para:

- **🎯 Candidatos ao TCU** - Auditor Federal de Controle Externo
- **📊 Pesquisadores** em análise de concursos públicos  
- **💻 Desenvolvedores** de ferramentas educacionais
- **📈 Analistas** de tendências em avaliações

## 📞 Suporte

- 📧 **Issues**: Use as Issues do GitHub para reportar bugs
- 📚 **Documentação**: Consulte a pasta `docs/` para guias detalhados
- 🔧 **Desenvolvimento**: Veja `CLAUDE.md` para guidelines

---

<div align="center">

**🎯 TCU 2026 - Dados organizados para o seu sucesso! 🚀**

[![GitHub stars](https://img.shields.io/github/stars/prof-ramos/tcu-2026?style=social)](https://github.com/prof-ramos/tcu-2026/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/prof-ramos/tcu-2026?style=social)](https://github.com/prof-ramos/tcu-2026/network)

</div>