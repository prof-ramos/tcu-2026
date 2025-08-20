# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Sobre o Projeto

Este repositório contém um banco de dados completo de questões do TCU (Tribunal de Contas da União) para 2026, com **293.855 questões** organizadas hierarquicamente em 1.250 registros limpos e estruturados para desenvolvimento de aplicações educacionais e análises estatísticas.

## Comandos Essenciais

### Ambiente Python (obrigatório usar `uv`)
```bash
# Criar ambiente virtual (usar uv conforme instrução global)
uv venv
source .venv/bin/activate

# Instalar dependências
uv pip install pandas>=2.0.0 openpyxl>=3.1.0 numpy>=1.24.0

# Verificar se venv está ativo antes de executar qualquer script
which python  # deve apontar para .venv/bin/python
```

### Processamento e Análise de Dados
```bash
# Limpar e processar dados originais
cd scripts/
python clean_data.py

# Análise completa com visualizações
python exemplo_analise_concursos.py

# Processamento avançado do Excel
python processador_excel_concursos.py [arquivo.xlsx]

# Sistema automatizado (macOS com Homebrew)
chmod +x exemplo_execucao_sistema.sh
./exemplo_execucao_sistema.sh
```

## Arquitetura do Sistema

### Estrutura de Dados Hierárquica
- **6 níveis hierárquicos** (0=disciplina principal, 1-5=subdivisões)
- **Códigos hierárquicos** no formato "01.02.03" para navegação precisa
- **Dupla indexação** por porcentagem (texto + numérico) para flexibilidade

### Pipeline de Processamento
1. **`clean_data.py`**: Limpeza e padronização dos dados brutos
2. **`processador_excel_concursos.py`**: Análise avançada e geração de insights
3. **`exemplo_analise_concursos.py`**: Demonstração de uso com visualizações

### Classes Principais
- **`ProcessadorExcelConcursos`**: Classe central para análise de dados
  - Carregar e validar múltiplas planilhas Excel
  - Gerar cronogramas otimizados de estudo
  - Identificar pontos críticos e tendências
  - Exportar resultados em múltiplos formatos

## Dados Core do Projeto

### Arquivo Principal: `data/processed/db-questoes-limpo.xlsx`
```python
# Estrutura validada dos dados limpos:
df = pd.read_excel('data/processed/db-questoes-limpo.xlsx')
# Colunas disponíveis:
# - hierarquia (string): Ex. "02.01.03" ou "CATEGORIA_PRINCIPAL"
# - topico (string): Nome da disciplina/subtópico
# - quantidade_encontrada (int): Questões identificadas
# - porcentagem_encontrada (string): "15.30%" formato texto
# - quantidade_caderno (int): Questões oficiais do caderno
# - porcentagem_caderno (string): Porcentagem oficial
# - porcentagem_encontrada_num (float): 15.30 formato numérico
# - porcentagem_caderno_num (float): Porcentagem numérica
# - nivel_hierarquia (int): 0-5 (0=principal)
```

### Disciplinas Principais (nível 0)
- **Direito Administrativo**: 19.77% (22.987 questões)
- **Língua Portuguesa**: 21.43% (24.913 questões)  
- **Direito Constitucional**: 13.21% (15.353 questões)
- **Administração Geral e Pública**: 13.71% (15.938 questões)
- **Informática**: 7.28% (8.469 questões)
- **Língua Inglesa**: 4.42% (5.139 questões)
- **Auditoria Governamental**: 2.53% (2.936 questões)

## Padrões de Desenvolvimento

### Código Python
- Usar **type hints** em todas as funções
- **Docstrings** obrigatórias para classes e métodos públicos
- **pandas** para manipulação de dados
- **matplotlib/seaborn** para visualizações
- **Path** do pathlib para manipulação de arquivos

### Estrutura de Scripts
```python
# Padrão para novos scripts de análise:
class AnalisadorTCU:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.dados = None
    
    def carregar_dados(self) -> dict:
        """Carrega e valida dados do Excel"""
        pass
    
    def analisar_distribuicao(self) -> dict:
        """Análise estatística da distribuição"""
        pass
    
    def exportar_resultados(self, formato: str = 'csv') -> list:
        """Exporta em múltiplos formatos"""
        pass
```

### Validação de Dados
- **Sempre validar** se hierarquia está consistente
- **Verificar** se porcentagens somam 100%
- **Conferir** se dados estão ordenados por hierarquia
- **Tratar** valores nulos substituindo por 'CATEGORIA_PRINCIPAL'

## Funcionalidades Disponíveis

### Sistema de Cronograma Otimizado
```python
# Gerar cronograma baseado em dados históricos
processador = ProcessadorExcelConcursos('dados/arquivo.xlsx')
cronograma = processador.gerar_cronograma_otimizado(horas_semanais=40)
```

### Identificação de Pontos Críticos
```python
# Identificar temas de alta prioridade
pontos_criticos = processador.identificar_pontos_criticos()
```

### Visualizações Automatizadas
```python
# Gerar gráficos completos
fig = processador.criar_visualizacoes_completas()
plt.show()
```

## Testes e Validação

### Antes de Commit
```bash
# Validar qualidade dos dados
python -c "
import pandas as pd
df = pd.read_csv('data/processed/db-questoes-limpo.csv')
assert df.isnull().sum().sum() == 0, 'Dados contêm valores nulos'
assert len(df) == 1250, 'Número incorreto de registros'
print('✅ Validação dos dados OK')
"

# Testar scripts principais
python scripts/clean_data.py
python scripts/exemplo_analise_concursos.py
```

## Arquivos de Configuração

### `scripts/requirements.txt`
```
pandas>=2.0.0
openpyxl>=3.1.0
numpy>=1.24.0
```

### Sistema Automatizado (macOS)
- **`exemplo_execucao_sistema.sh`**: Setup completo otimizado para macOS M3
- **Homebrew dependencies**: python@3.11, postgresql, redis
- **Configuração automática**: venv, dependências, estrutura de pastas