#!/usr/bin/env python3
"""
Exemplo Prático: Análise de Dados de Concursos Públicos
Baseado na estrutura do arquivo dbquestoes.xlsx

Funcionalidades:
- Análise de hierarquia de temas
- Cálculo de frequências e porcentagens
- Identificação de padrões de recorrência
- Geração de insights para estudos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import json
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configurações para visualização
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AnalisadorConcursos:
    """
    Classe principal para análise de dados de concursos públicos
    """
    
    def __init__(self):
        self.dados_questoes = None
        self.estatisticas = {}
        self.insights = []
    
    def criar_dados_exemplo(self):
        """
        Cria dados de exemplo baseados na estrutura do arquivo original
        """
        # Simular dados reais de análise de questões de concursos
        dados_exemplo = [
            # Direito Constitucional
            ("Direito Constitucional", "1.1", 145, 18.5, 78, 15.2, 18.5),
            ("Direito Constitucional > Princípios Fundamentais", "1.1.1", 32, 4.1, 18, 3.5, 22.6),
            ("Direito Constitucional > Direitos Fundamentais", "1.1.2", 67, 8.5, 35, 6.8, 31.1),
            ("Direito Constitucional > Organização do Estado", "1.1.3", 28, 3.6, 15, 2.9, 34.7),
            ("Direito Constitucional > Controle de Constitucionalidade", "1.1.4", 18, 2.3, 10, 1.9, 37.0),
            
            # Direito Administrativo
            ("Direito Administrativo", "1.2", 128, 16.3, 68, 13.3, 53.3),
            ("Direito Administrativo > Princípios", "1.2.1", 35, 4.5, 20, 3.9, 57.8),
            ("Direito Administrativo > Atos Administrativos", "1.2.2", 42, 5.4, 22, 4.3, 63.2),
            ("Direito Administrativo > Licitações", "1.2.3", 31, 3.9, 16, 3.1, 67.1),
            ("Direito Administrativo > Contratos", "1.2.4", 20, 2.5, 10, 1.9, 69.6),
            
            # Português
            ("Língua Portuguesa", "2.1", 98, 12.5, 52, 10.1, 82.1),
            ("Língua Portuguesa > Interpretação de Texto", "2.1.1", 38, 4.8, 20, 3.9, 86.9),
            ("Língua Portuguesa > Gramática", "2.1.2", 35, 4.5, 18, 3.5, 91.4),
            ("Língua Portuguesa > Redação Oficial", "2.1.3", 25, 3.2, 14, 2.7, 94.6),
            
            # Informática
            ("Informática", "3.1", 42, 5.4, 28, 5.4, 100.0),
            ("Informática > MS Office", "3.1.1", 18, 2.3, 12, 2.3, 100.0),
            ("Informática > Redes e Internet", "3.1.2", 15, 1.9, 10, 1.9, 100.0),
            ("Informática > Segurança", "3.1.3", 9, 1.1, 6, 1.2, 100.0),
        ]
        
        # Criar DataFrame
        colunas = [
            'Hierarquia', 'Indice', 'Quantidade_Encontrada', 
            'Porcentagem_Encontrada', 'Quantidade_Caderno', 
            'Porcentagem_Caderno', 'Frequencia_Acumulada'
        ]
        
        self.dados_questoes = pd.DataFrame(dados_exemplo, columns=colunas)
        return self.dados_questoes
    
    def calcular_estatisticas_basicas(self):
        """
        Calcula estatísticas básicas dos dados
        """
        if self.dados_questoes is None:
            raise ValueError("Dados não carregados. Execute criar_dados_exemplo() primeiro.")
        
        # Separar disciplinas principais (sem ">")
        disciplinas_principais = self.dados_questoes[
            ~self.dados_questoes['Hierarquia'].str.contains('>', na=False)
        ]
        
        # Calcular estatísticas
        stats = {
            'total_questoes_encontradas': self.dados_questoes['Quantidade_Encontrada'].sum(),
            'total_questoes_caderno': self.dados_questoes['Quantidade_Caderno'].sum(),
            'disciplinas_principais': len(disciplinas_principais),
            'subdisciplinas': len(self.dados_questoes) - len(disciplinas_principais),
            'disciplina_mais_cobrada': disciplinas_principais.loc[
                disciplinas_principais['Quantidade_Encontrada'].idxmax(), 'Hierarquia'
            ],
            'maior_porcentagem': disciplinas_principais['Porcentagem_Encontrada'].max()
        }
        
        self.estatisticas = stats
        return stats
    
    def identificar_padroes_estudo(self):
        """
        Identifica padrões e gera insights para otimizar estudos
        """
        if self.dados_questoes is None:
            raise ValueError("Dados não carregados.")
        
        insights = []
        
        # Disciplinas de alta prioridade (>15% das questões)
        alta_prioridade = self.dados_questoes[
            (self.dados_questoes['Porcentagem_Encontrada'] >= 15) &
            (~self.dados_questoes['Hierarquia'].str.contains('>', na=False))
        ]
        
        if not alta_prioridade.empty:
            insights.append({
                'tipo': 'Alta Prioridade',
                'descricao': f"Disciplinas que representam ≥15% das questões: {', '.join(alta_prioridade['Hierarquia'].tolist())}",
                'acao': 'Focar 60% do tempo de estudo nestas disciplinas'
            })
        
        # Subdisciplinas com maior concentração
        subdisciplinas = self.dados_questoes[
            self.dados_questoes['Hierarquia'].str.contains('>', na=False)
        ].nlargest(3, 'Porcentagem_Encontrada')
        
        if not subdisciplinas.empty:
            insights.append({
                'tipo': 'Temas Específicos',
                'descricao': f"Subtemas mais cobrados: {', '.join(subdisciplinas['Hierarquia'].str.split(' > ').str[-1].tolist())}",
                'acao': 'Priorizar estes temas dentro de cada disciplina'
            })
        
        # Análise de eficiência (relação encontrado vs caderno)
        eficiencia = self.dados_questoes.copy()
        eficiencia['Eficiencia'] = (
            eficiencia['Porcentagem_Encontrada'] / eficiencia['Porcentagem_Caderno']
        ).round(2)
        
        mais_eficientes = eficiencia[
            (~eficiencia['Hierarquia'].str.contains('>', na=False)) &
            (eficiencia['Eficiencia'] > 1.2)
        ]
        
        if not mais_eficientes.empty:
            insights.append({
                'tipo': 'Eficiência de Estudo',
                'descricao': f"Disciplinas com maior retorno por tempo investido: {', '.join(mais_eficientes['Hierarquia'].tolist())}",
                'acao': 'Aumentar carga horária nestas disciplinas'
            })
        
        self.insights = insights
        return insights
    
    def gerar_cronograma_estudo(self, horas_semanais=40):
        """
        Gera sugestão de cronograma baseado nos dados
        """
        if self.dados_questoes is None:
            raise ValueError("Dados não carregados.")
        
        # Disciplinas principais apenas
        disciplinas = self.dados_questoes[
            ~self.dados_questoes['Hierarquia'].str.contains('>', na=False)
        ].copy()
        
        # Calcular distribuição de horas baseada na porcentagem + bônus para eficiência
        disciplinas['Eficiencia'] = (
            disciplinas['Porcentagem_Encontrada'] / disciplinas['Porcentagem_Caderno']
        )
        
        # Peso = porcentagem base + bônus por eficiência
        disciplinas['Peso'] = (
            disciplinas['Porcentagem_Encontrada'] + 
            (disciplinas['Eficiencia'] - 1) * 5
        ).clip(lower=0)
        
        # Normalizar pesos
        disciplinas['Peso_Normalizado'] = (
            disciplinas['Peso'] / disciplinas['Peso'].sum()
        )
        
        # Calcular horas
        disciplinas['Horas_Semanais'] = (
            disciplinas['Peso_Normalizado'] * horas_semanais
        ).round(1)
        
        cronograma = disciplinas[['Hierarquia', 'Horas_Semanais', 'Porcentagem_Encontrada']].copy()
        cronograma.columns = ['Disciplina', 'Horas/Semana', 'Importância (%)']
        
        return cronograma.sort_values('Horas/Semana', ascending=False)
    
    def criar_visualizacoes(self):
        """
        Cria visualizações dos dados analisados
        """
        if self.dados_questoes is None:
            raise ValueError("Dados não carregados.")
        
        # Configurar subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise de Dados - Concursos Públicos', fontsize=16, fontweight='bold')
        
        # 1. Distribuição por disciplina principal
        disciplinas = self.dados_questoes[
            ~self.dados_questoes['Hierarquia'].str.contains('>', na=False)
        ]
        
        axes[0,0].pie(
            disciplinas['Porcentagem_Encontrada'], 
            labels=disciplinas['Hierarquia'],
            autopct='%1.1f%%',
            startangle=90
        )
        axes[0,0].set_title('Distribuição de Questões por Disciplina')
        
        # 2. Comparação Encontrado vs Caderno
        x = range(len(disciplinas))
        width = 0.35
        
        axes[0,1].bar([i - width/2 for i in x], disciplinas['Porcentagem_Encontrada'], 
                     width, label='Encontrado', alpha=0.8)
        axes[0,1].bar([i + width/2 for i in x], disciplinas['Porcentagem_Caderno'], 
                     width, label='Caderno', alpha=0.8)
        
        axes[0,1].set_xlabel('Disciplinas')
        axes[0,1].set_ylabel('Porcentagem (%)')
        axes[0,1].set_title('Comparação: Questões Encontradas vs Caderno')
        axes[0,1].set_xticks(x)
        axes[0,1].set_xticklabels([d.split()[0] for d in disciplinas['Hierarquia']], rotation=45)
        axes[0,1].legend()
        
        # 3. Top 10 Subtemas
        subtemas = self.dados_questoes[
            self.dados_questoes['Hierarquia'].str.contains('>', na=False)
        ].nlargest(10, 'Quantidade_Encontrada')
        
        subtemas_nomes = [tema.split(' > ')[-1] for tema in subtemas['Hierarquia']]
        
        axes[1,0].barh(subtemas_nomes, subtemas['Quantidade_Encontrada'])
        axes[1,0].set_xlabel('Quantidade de Questões')
        axes[1,0].set_title('Top 10 Subtemas Mais Cobrados')
        axes[1,0].invert_yaxis()
        
        # 4. Eficiência por Disciplina
        disciplinas_efic = disciplinas.copy()
        disciplinas_efic['Eficiencia'] = (
            disciplinas_efic['Porcentagem_Encontrada'] / disciplinas_efic['Porcentagem_Caderno']
        )
        
        cores = ['green' if x > 1 else 'red' for x in disciplinas_efic['Eficiencia']]
        
        axes[1,1].bar(range(len(disciplinas_efic)), disciplinas_efic['Eficiencia'], color=cores, alpha=0.7)
        axes[1,1].axhline(y=1, color='black', linestyle='--', alpha=0.5)
        axes[1,1].set_xlabel('Disciplinas')
        axes[1,1].set_ylabel('Eficiência (Encontrado/Caderno)')
        axes[1,1].set_title('Eficiência de Estudo por Disciplina')
        axes[1,1].set_xticks(range(len(disciplinas_efic)))
        axes[1,1].set_xticklabels([d.split()[0] for d in disciplinas_efic['Hierarquia']], rotation=45)
        
        plt.tight_layout()
        return fig
    
    def gerar_relatorio_completo(self):
        """
        Gera relatório completo com todos os insights
        """
        if self.dados_questoes is None:
            self.criar_dados_exemplo()
        
        # Calcular todas as análises
        stats = self.calcular_estatisticas_basicas()
        insights = self.identificar_padroes_estudo()
        cronograma = self.gerar_cronograma_estudo()
        
        # Gerar relatório
        relatorio = f"""
=== RELATÓRIO DE ANÁLISE - CONCURSOS PÚBLICOS ===
Data da Análise: {datetime.now().strftime('%d/%m/%Y %H:%M')}

📊 ESTATÍSTICAS GERAIS:
• Total de questões analisadas: {stats['total_questoes_encontradas']}
• Total de questões no caderno: {stats['total_questoes_caderno']}
• Disciplinas principais: {stats['disciplinas_principais']}
• Subdisciplinas analisadas: {stats['subdisciplinas']}
• Disciplina mais cobrada: {stats['disciplina_mais_cobrada']} ({stats['maior_porcentagem']:.1f}%)

🎯 INSIGHTS ESTRATÉGICOS:
"""
        
        for i, insight in enumerate(insights, 1):
            relatorio += f"""
{i}. {insight['tipo']}:
   • {insight['descricao']}
   • Ação recomendada: {insight['acao']}
"""
        
        relatorio += f"""

📅 CRONOGRAMA SUGERIDO (40h/semana):
{cronograma.to_string(index=False)}

💡 RECOMENDAÇÕES FINAIS:
• Revisar estratégia a cada 30 dias
• Focar em simulados das disciplinas de alta prioridade  
• Manter registro de performance por tema
• Ajustar cronograma baseado em resultados dos simulados
"""
        
        return relatorio

def main():
    """
    Função principal - demonstração do sistema
    """
    print("🚀 Iniciando Análise de Dados de Concursos Públicos")
    print("=" * 60)
    
    # Criar instância do analisador
    analisador = AnalisadorConcursos()
    
    # Carregar dados de exemplo
    print("📂 Carregando dados...")
    dados = analisador.criar_dados_exemplo()
    print(f"✅ {len(dados)} registros carregados com sucesso!")
    
    # Gerar relatório completo
    print("\n📋 Gerando relatório de análise...")
    relatorio = analisador.gerar_relatorio_completo()
    print(relatorio)
    
    # Criar visualizações
    print("\n📈 Gerando visualizações...")
    fig = analisador.criar_visualizacoes()
    
    # Salvar resultados
    print("\n💾 Salvando resultados...")
    
    # Salvar dados processados
    cronograma = analisador.gerar_cronograma_estudo()
    cronograma.to_csv('cronograma_estudo.csv', index=False)
    
    # Salvar insights em JSON
    with open('insights_concursos.json', 'w', encoding='utf-8') as f:
        json.dump({
            'estatisticas': analisador.estatisticas,
            'insights': analisador.insights,
            'data_analise': datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)
    
    # Salvar relatório
    with open('relatorio_analise.txt', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print("✅ Análise concluída! Arquivos salvos:")
    print("   • cronograma_estudo.csv")
    print("   • insights_concursos.json") 
    print("   • relatorio_analise.txt")
    
    # Mostrar gráficos
    plt.show()

if __name__ == "__main__":
    main()
