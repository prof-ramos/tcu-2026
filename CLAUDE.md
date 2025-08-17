# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Sobre o Projeto

Este repositório contém um banco de dados de questões do TCU (Tribunal de Contas da União) para 2026, com dados limpos e organizados para desenvolvimento de aplicações educacionais.

## Estrutura do Projeto

```
tcu-2026/
├── data/
│   ├── raw/                    # Dados originais (não modificar)
│   │   ├── db-questoes.xlsx   # Banco original de questões
│   │   ├── tcu-verticalizado.xlsx
│   │   ├── tcu.csv
│   │   └── outros arquivos de dados brutos
│   └── processed/              # Dados processados e limpos
│       ├── db-questoes-limpo.xlsx  # Dados limpos (usar este)
│       └── db-questoes-limpo.csv   # Versão CSV dos dados limpos
├── scripts/                    # Scripts Python para processamento
│   ├── clean_data.py          # Script principal de limpeza
│   └── requirements.txt       # Dependências Python
├── docs/                      # Documentação
│   ├── relatorio_limpeza.md   # Relatório da limpeza de dados
│   └── TCU_2021.pdf          # Documentação adicional
├── CLAUDE.md                  # Este arquivo
└── README.md                  # Documentação do projeto
```

## Comandos Principais

### Ambiente Python
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r scripts/requirements.txt
```

### Processamento de Dados
```bash
# Limpar dados (se necessário reprocessar)
cd scripts/
python clean_data.py
```

## Dados Disponíveis

### Dados Limpos (usar estes)
- **`data/processed/db-questoes-limpo.xlsx`**: Dados principais limpos e organizados
- **`data/processed/db-questoes-limpo.csv`**: Versão CSV dos dados limpos

### Estrutura dos Dados Limpos
- `hierarquia`: Código hierárquico do tópico
- `topico`: Nome do tópico/assunto
- `quantidade_encontrada`: Número de questões encontradas
- `porcentagem_encontrada`: Porcentagem em formato texto
- `quantidade_caderno`: Quantidade no caderno
- `porcentagem_caderno`: Porcentagem do caderno
- `porcentagem_encontrada_num`: Porcentagem como número (0-100)
- `porcentagem_caderno_num`: Porcentagem do caderno como número
- `nivel_hierarquia`: Nível hierárquico (0=categoria principal, 1-5=subcategorias)

## Arquitetura de Desenvolvimento

Para desenvolvimento futuro:
- **Frontend**: React/Vue.js para interface web
- **Backend**: Python (Flask/FastAPI) ou Node.js
- **Banco de Dados**: PostgreSQL ou SQLite para desenvolvimento
- **Extensão Chrome**: Para estudos integrados ao navegador
- **API**: REST ou GraphQL para acesso aos dados

## Funcionalidades Sugeridas

1. **Sistema de Estudos**
   - Simulados baseados na hierarquia
   - Filtros por nível hierárquico
   - Acompanhamento de progresso

2. **Análise de Dados**
   - Dashboard com estatísticas
   - Gráficos de distribuição por tópico
   - Relatórios de performance

3. **Busca e Filtragem**
   - Busca por texto nos tópicos
   - Filtros por quantidade de questões
   - Ordenação por diferentes critérios

## Qualidade dos Dados

✅ **Dados limpos e validados**
- 1.250 registros organizados
- 0 valores nulos
- Hierarquia padronizada (6 níveis)
- Porcentagens em formatos numérico e texto
- Documentação completa do processo de limpeza