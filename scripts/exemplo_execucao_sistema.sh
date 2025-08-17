#!/bin/bash
# Script de Exemplo - Execução do Sistema de Análise de Concursos Públicos
# Otimizado para macOS (Apple Silicon M3) com Homebrew

echo "🚀 CONFIGURAÇÃO DO AMBIENTE - ANÁLISE DE CONCURSOS PÚBLICOS"
echo "================================================================"

# Verificar se está no macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "⚠️  Este script é otimizado para macOS"
fi

# Verificar Homebrew
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew não encontrado. Instalando..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅ Homebrew encontrado"
fi

# Atualizar Homebrew
echo "📦 Atualizando Homebrew..."
brew update

# Instalar dependências do sistema
echo "🔧 Instalando dependências do sistema..."
brew install python@3.11
brew install postgresql
brew install redis
brew install git

# Verificar Python
PYTHON_VERSION=$(python3 --version 2>&1)
echo "🐍 Python: $PYTHON_VERSION"

# Configurar projeto
echo "📁 Configurando projeto..."
PROJECT_DIR="analise_concursos_$(date +%Y%m%d)"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# Criar ambiente virtual
echo "🏗️  Criando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

# Criar requirements.txt
echo "📋 Criando requirements.txt..."
cat > requirements.txt << EOF
# Análise de Dados
pandas>=2.0.0
numpy>=1.24.0
polars>=0.20.0

# Visualização
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0
altair>=5.0.0

# Processamento de Arquivos
openpyxl>=3.1.0
xlsxwriter>=3.1.0
PyPDF2>=3.0.0
pdfplumber>=0.9.0
tabula-py>=2.8.0

# Web Scraping
beautifulsoup4>=4.12.0
requests>=2.31.0
scrapy>=2.11.0
selenium>=4.15.0

# Machine Learning e NLP
scikit-learn>=1.3.0
nltk>=3.8.0
spacy>=3.7.0
transformers>=4.35.0

# Dashboards e Apps
streamlit>=1.28.0
dash>=2.14.0
gradio>=3.50.0

# Banco de Dados
psycopg2-binary>=2.9.0
SQLAlchemy>=2.0.0

# Utilitários
python-dotenv>=1.0.0
tqdm>=4.66.0
schedule>=1.2.0
click>=8.1.0

# Jupyter
jupyter>=1.0.0
jupyterlab>=4.0.0
EOF

# Instalar dependências Python
echo "⬇️  Instalando dependências Python..."
pip install --upgrade pip
pip install -r requirements.txt

# Baixar modelos de NLP (se necessário)
echo "📚 Configurando modelos de NLP..."
python -c "
import nltk
try:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    print('✅ Modelos NLTK baixados')
except:
    print('⚠️ Erro ao baixar modelos NLTK')
"

# Criar estrutura de diretórios
echo "📂 Criando estrutura de diretórios..."
mkdir -p {dados,scripts,resultados,notebooks,config,logs,temp}

# Criar arquivo de configuração
echo "⚙️  Criando arquivo de configuração..."
cat > config/config.py << 'EOF'
"""
Configurações do Sistema de Análise de Concursos
"""
import os
from pathlib import Path

# Diretórios
BASE_DIR = Path(__file__).parent.parent
DADOS_DIR = BASE_DIR / "dados"
RESULTADOS_DIR = BASE_DIR / "resultados"
LOGS_DIR = BASE_DIR / "logs"
TEMP_DIR = BASE_DIR / "temp"

# Configurações de Análise
BANCAS_PRINCIPAIS = [
    'CESPE/CEBRASPE',
    'FCC',
    'VUNESP', 
    'FGV',
    'CONSULPLAN',
    'IBFC',
    'IADES',
    'AOCP'
]

DISCIPLINAS_CORE = [
    'Direito Constitucional',
    'Direito Administrativo',
    'Língua Portuguesa',
    'Informática',
    'Legislação Específica',
    'Raciocínio Lógico',
    'Conhecimentos Gerais'
]

# Configurações de Visualização
FIGURA_DPI = 300
FIGURA_SIZE = (16, 12)
CORES_PALETTE = "husl"

# Configurações de Processamento
MAX_WORKERS = 4  # Otimizado para M3 com 8GB RAM
CHUNK_SIZE = 1000
CACHE_ENABLED = True

# Configurações de Exportação
FORMATOS_EXPORT = ['csv', 'excel', 'json', 'pdf']
ENCODING_DEFAULT = 'utf-8'

# Configurações de Log
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
EOF

# Copiar o arquivo de exemplo (se existir)
if [ -f "../dbquestoes.xlsx" ]; then
    echo "📄 Copiando arquivo de dados..."
    cp "../dbquestoes.xlsx" dados/
    echo "✅ Arquivo dbquestoes.xlsx copiado para dados/"
else
    echo "⚠️  Arquivo dbquestoes.xlsx não encontrado no diretório pai"
    echo "📝 Coloque seus arquivos Excel na pasta 'dados/'"
fi

# Criar script principal
echo "🐍 Criando script principal..."
cat > scripts/analisar_concursos.py << 'EOF'
#!/usr/bin/env python3
"""
Script Principal - Análise de Concursos Públicos
Uso: python scripts/analisar_concursos.py [arquivo.xlsx]
"""

import sys
import argparse
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.append(str(Path(__file__).parent.parent))

from scripts.processador_excel_concursos import ProcessadorExcelConcursos

def main():
    parser = argparse.ArgumentParser(description='Análise de Dados de Concursos Públicos')
    parser.add_argument('arquivo', nargs='?', default='dados/dbquestoes.xlsx',
                       help='Arquivo Excel para análise')
    parser.add_argument('--output', '-o', default='resultados',
                       help='Diretório de saída')
    parser.add_argument('--horas', '-h', type=int, default=40,
                       help='Horas semanais de estudo')
    parser.add_argument('--visualizar', '-v', action='store_true',
                       help='Mostrar gráficos')
    
    args = parser.parse_args()
    
    print(f"🎯 Analisando arquivo: {args.arquivo}")
    print(f"💾 Resultados em: {args.output}")
    print(f"⏰ Cronograma para: {args.horas}h/semana")
    
    # Executar análise
    processador = ProcessadorExcelConcursos(args.arquivo)
    
    try:
        # Carregar dados
        dados = processador.carregar_dados()
        
        # Gerar relatório
        relatorio = processador.gerar_relatorio_executivo()
        print("\n" + "="*60)
        print("📊 RESUMO DA ANÁLISE:")
        print("="*60)
        
        # Mostrar primeiras linhas do relatório
        for linha in relatorio.split('\n')[:20]:
            print(linha)
        
        # Exportar resultados
        arquivos = processador.exportar_resultados(args.output)
        print(f"\n✅ {len(arquivos)} arquivo(s) gerado(s) em {args.output}/")
        
        # Gerar visualizações se solicitado
        if args.visualizar:
            try:
                import matplotlib.pyplot as plt
                fig = processador.criar_visualizacoes_completas()
                plt.show()
            except ImportError:
                print("⚠️ Matplotlib não disponível para visualizações")
        
    except Exception as e:
        print(f"❌ Erro na análise: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
EOF

# Criar Jupyter Notebook de exemplo
echo "📓 Criando notebook de exemplo..."
cat > notebooks/exemplo_analise.ipynb << 'EOF'
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Análise de Concursos Públicos - Exemplo Prático\n",
    "\n",
    "Este notebook demonstra como usar o sistema de análise de dados de concursos públicos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Importações\n",
    "import sys\n",
    "sys.path.append('..')\n",
    "\n",
    "from scripts.processador_excel_concursos import ProcessadorExcelConcursos\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Configurações\n",
    "plt.style.use('default')\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Carregar e analisar dados\n",
    "processador = ProcessadorExcelConcursos('../dados/dbquestoes.xlsx')\n",
    "dados = processador.carregar_dados()\n",
    "\n",
    "print(f\"📊 Dados carregados: {len(dados)} planilha(s)\")\n",
    "for nome, df in dados.items():\n",
    "    print(f\"   • {nome}: {len(df)} registros\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Análise de distribuição\n",
    "for nome_planilha in dados.keys():\n",
    "    analise = processador.analisar_distribuicao_temas(nome_planilha)\n",
    "    \n",
    "    print(f\"\\n📋 Planilha: {nome_planilha}\")\n",
    "    print(f\"Disciplinas principais: {len(analise['disciplinas_principais'])}\")\n",
    "    print(f\"Subdisciplinas: {len(analise['subdisciplinas'])}\")\n",
    "    print(f\"Total de questões: {analise['total_questoes']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Gerar cronograma otimizado\n",
    "cronograma = processador.gerar_cronograma_otimizado()\n",
    "display(cronograma)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Criar visualizações\n",
    "fig = processador.criar_visualizacoes_completas()\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Pontos críticos\n",
    "pontos = processador.identificar_pontos_criticos()\n",
    "\n",
    "print(\"🎯 Pontos Críticos Identificados:\")\n",
    "for i, ponto in enumerate(pontos, 1):\n",
    "    print(f\"\\n{i}. {ponto['tipo']}: {ponto['tema']}\")\n",
    "    print(f\"   Recomendação: {ponto['recomendacao']}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF

# Criar Makefile para automatização
echo "🛠️  Criando Makefile..."
cat > Makefile << 'EOF'
# Makefile para Sistema de Análise de Concursos Públicos

.PHONY: help install setup test analyze clean

# Variáveis
PYTHON = python3
VENV = venv
ARQUIVO_DEFAULT = dados/dbquestoes.xlsx

help: ## Mostrar esta ajuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $1, $2}'

install: ## Instalar dependências
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

setup: ## Configuração inicial completa
	@echo "🚀 Configuração inicial..."
	make install
	mkdir -p {dados,resultados,logs,temp}
	@echo "✅ Configuração concluída!"

test: ## Testar sistema com dados de exemplo
	$(PYTHON) scripts/analisar_concursos.py --visualizar

analyze: ## Analisar arquivo específico (use ARQUIVO=caminho/arquivo.xlsx)
	$(PYTHON) scripts/analisar_concursos.py $(or $(ARQUIVO),$(ARQUIVO_DEFAULT)) --visualizar

notebook: ## Iniciar Jupyter Lab
	jupyter lab notebooks/

clean: ## Limpar arquivos temporários
	rm -rf temp/*
	rm -rf __pycache__
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

export: ## Exportar ambiente
	pip freeze > requirements-freeze.txt
	@echo "✅ Dependências exportadas para requirements-freeze.txt"

backup: ## Backup dos resultados
	tar -czf backup_$(shell date +%Y%m%d_%H%M%S).tar.gz resultados/ dados/
	@echo "✅ Backup criado"

# Exemplos de uso:
# make setup          # Configuração inicial
# make test           # Teste com dados de exemplo  
# make analyze        # Analisar arquivo padrão
# make analyze ARQUIVO=dados/meu_arquivo.xlsx  # Analisar arquivo específico
# make notebook       # Abrir Jupyter Lab
EOF

# Criar script de atualização
echo "🔄 Criando script de atualização..."
cat > scripts/update_system.py << 'EOF'
#!/usr/bin/env python3
"""
Script de Atualização do Sistema
"""

import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Executa comando e mostra progresso"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} concluído")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro em {description}: {e}")
        return False

def main():
    print("🚀 ATUALIZADOR DO SISTEMA DE ANÁLISE")
    print("="*50)
    
    # Atualizar pip
    run_command("pip install --upgrade pip", "Atualizando pip")
    
    # Atualizar dependências
    run_command("pip install --upgrade -r requirements.txt", "Atualizando dependências")
    
    # Atualizar modelos NLTK
    run_command('python -c "import nltk; nltk.download(\'punkt\'); nltk.download(\'stopwords\')"', 
                "Atualizando modelos NLTK")
    
    # Limpar cache
    run_command("find . -name '__pycache__' -type d -exec rm -rf {} +", "Limpando cache")
    
    # Verificar integridade
    print("\n🔍 Verificando integridade do sistema...")
    
    try:
        import pandas, numpy, matplotlib, seaborn
        print("✅ Bibliotecas principais OK")
    except ImportError as e:
        print(f"❌ Erro nas bibliotecas: {e}")
    
    print("\n🎉 Atualização concluída!")

if __name__ == "__main__":
    main()
EOF

# Criar README
echo "📖 Criando README..."
cat > README.md << 'EOF'
# Sistema de Análise de Concursos Públicos

Sistema automatizado para análise de dados de questões de concursos públicos, otimizado para identificar padrões, tendências e gerar cronogramas de estudo personalizados.

## 🚀 Funcionalidades

- **Análise de Distribuição**: Identificação de temas mais cobrados
- **Cronograma Otimizado**: Geração automática baseada em dados históricos
- **Pontos Críticos**: Identificação de áreas prioritárias
- **Visualizações**: Gráficos interativos e relatórios
- **Exportação**: Múltiplos formatos (CSV, Excel, JSON, PDF)

## 💻 Requisitos

- macOS (otimizado para Apple Silicon M3)
- Python 3.11+
- Homebrew
- 8GB RAM mínimo

## 🛠️ Instalação Rápida

```bash
# Clone ou baixe este projeto
git clone [repositório] analise_concursos
cd analise_concursos

# Execute o setup automatizado
make setup

# Ative o ambiente virtual
source venv/bin/activate
```

## 📊 Uso Básico

### 1. Análise Simples
```bash
# Analisar arquivo padrão
make test

# Analisar arquivo específico
make analyze ARQUIVO=dados/meu_arquivo.xlsx
```

### 2. Jupyter Notebook
```bash
# Abrir ambiente interativo
make notebook
```

### 3. Script Python
```python
from scripts.processador_excel_concursos import ProcessadorExcelConcursos

# Carregar e analisar
processador = ProcessadorExcelConcursos('dados/dbquestoes.xlsx')
dados = processador.carregar_dados()

# Gerar cronograma
cronograma = processador.gerar_cronograma_otimizado()
print(cronograma)

# Exportar resultados
arquivos = processador.exportar_resultados()
```

## 📁 Estrutura do Projeto

```
analise_concursos/
├── dados/              # Arquivos Excel de entrada
├── scripts/            # Scripts Python
├── notebooks/          # Jupyter Notebooks
├── resultados/         # Relatórios e exports
├── config/             # Configurações
├── logs/               # Logs do sistema
└── temp/               # Arquivos temporários
```

## 📈 Exemplo de Saída

### Cronograma Gerado
| Disciplina | Horas/Semana | Importância (%) |
|------------|--------------|-----------------|
| Direito Constitucional | 12.5h | 19.8% |
| Direito Administrativo | 11.2h | 18.0% |
| Língua Portuguesa | 9.8h | 15.0% |

### Insights Identificados
- **Alta Prioridade**: Direito Constitucional (19.8%)
- **Eficiência Máxima**: Direitos Fundamentais
- **Tema Emergente**: Controle de Constitucionalidade

## 🔧 Comandos Úteis

```bash
make help          # Ver todos os comandos
make clean         # Limpar arquivos temporários
make backup        # Backup dos resultados
make export        # Exportar dependências
```

## 📊 Formatos Suportados

- **Entrada**: Excel (.xlsx), CSV
- **Saída**: CSV, Excel, JSON, PDF, TXT

## 🎯 Bancas Suportadas

- CESPE/CEBRASPE
- FCC (Fundação Carlos Chagas)
- VUNESP
- FGV
- CONSULPLAN
- IBFC, IADES, AOCP

## 📝 Configuração Avançada

Edite `config/config.py` para personalizar:
- Bancas analisadas
- Disciplinas principais
- Parâmetros de visualização
- Configurações de performance

## 🆘 Suporte

### Problemas Comuns

1. **Erro de Memória**: Reduza `CHUNK_SIZE` em `config.py`
2. **Dependências**: Execute `make install`
3. **Visualizações**: Instale `brew install python-tk`

### Atualização
```bash
python scripts/update_system.py
```

## 📄 Licença

Sistema desenvolvido para otimização de estudos em concursos públicos.

---

**Desenvolvido com ❤️ para concurseiros brasileiros**
EOF

# Finalizar configuração
echo "🎯 Criando arquivo .env de exemplo..."
cat > .env.example << 'EOF'
# Configurações do Sistema de Análise de Concursos

# Diretórios
DATA_DIR=dados
RESULTS_DIR=resultados
LOG_DIR=logs

# Performance (ajuste conforme seu hardware)
MAX_WORKERS=4
CHUNK_SIZE=1000
CACHE_SIZE=100

# Visualizações
FIGURE_DPI=300
SHOW_PLOTS=true

# Exportação
DEFAULT_FORMAT=csv
ENCODING=utf-8

# Logging
LOG_LEVEL=INFO
DEBUG_MODE=false
EOF

# Permissões de execução
chmod +x scripts/*.py

echo ""
echo "🎉 CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!"
echo "================================================================"
echo ""
echo "📁 Projeto criado em: $(pwd)"
echo ""
echo "🚀 PRÓXIMOS PASSOS:"
echo "   1. cd $PROJECT_DIR"
echo "   2. source venv/bin/activate"
echo "   3. Copie seus arquivos Excel para a pasta 'dados/'"
echo "   4. Execute: make test"
echo ""
echo "📚 COMANDOS ÚTEIS:"
echo "   • make help          # Ver todos os comandos"
echo "   • make test          # Testar com dados de exemplo"
echo "   • make notebook      # Abrir Jupyter Lab"
echo "   • make analyze       # Analisar seus dados"
echo ""
echo "📖 DOCUMENTAÇÃO:"
echo "   • README.md          # Guia completo"
echo "   • notebooks/         # Exemplos interativos"
echo "   • config/config.py   # Configurações"
echo ""
echo "✅ Sistema pronto para uso!"