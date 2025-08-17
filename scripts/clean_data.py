import pandas as pd
import numpy as np
import re

def clean_dataframe(df):
    """
    Aplica boas práticas de limpeza de dados no dataframe de questões TCU
    """
    print("=== INICIANDO LIMPEZA DO DATAFRAME ===")
    print(f"Dimensões originais: {df.shape}")
    
    # Criar uma cópia para não modificar o original
    df_clean = df.copy()
    
    # 1. RENOMEAR COLUNAS PARA NOMES MAIS CLAROS
    print("\n1. Renomeando colunas...")
    df_clean.columns = [
        'hierarquia',
        'topico',
        'quantidade_encontrada', 
        'porcentagem_encontrada',
        'quantidade_caderno',
        'porcentagem_caderno',
        'frequencia_acumulada'
    ]
    
    # 2. REMOVER COLUNA TOTALMENTE VAZIA
    print("\n2. Removendo coluna 'frequencia_acumulada' (totalmente vazia)...")
    df_clean = df_clean.drop('frequencia_acumulada', axis=1)
    
    # 3. LIMPAR E PADRONIZAR COLUNAS DE TEXTO
    print("\n3. Limpando espaços em branco...")
    df_clean['topico'] = df_clean['topico'].str.strip()
    df_clean['hierarquia'] = df_clean['hierarquia'].astype(str).str.strip()
    
    # 4. TRATAR VALORES NULOS NA HIERARQUIA
    print("\n4. Tratando valores nulos na hierarquia...")
    # Substituir 'nan' string por valores apropriados
    df_clean.loc[df_clean['hierarquia'] == 'nan', 'hierarquia'] = 'CATEGORIA_PRINCIPAL'
    
    # 5. CONVERTER PORCENTAGENS PARA FORMATO NUMÉRICO
    print("\n5. Convertendo porcentagens para formato numérico...")
    
    def convert_percentage(pct_str):
        """Converte string de porcentagem para float"""
        if pd.isna(pct_str):
            return 0.0
        try:
            # Remove % e converte vírgula para ponto
            clean_pct = str(pct_str).replace('%', '').replace(',', '.')
            return float(clean_pct)
        except:
            return 0.0
    
    df_clean['porcentagem_encontrada_num'] = df_clean['porcentagem_encontrada'].apply(convert_percentage)
    df_clean['porcentagem_caderno_num'] = df_clean['porcentagem_caderno'].apply(convert_percentage)
    
    # 6. VALIDAR CONSISTÊNCIA DOS DADOS
    print("\n6. Validando consistência dos dados...")
    
    # Verificar se porcentagens estão entre 0 e 100
    invalid_pct = (df_clean['porcentagem_encontrada_num'] < 0) | (df_clean['porcentagem_encontrada_num'] > 100)
    if invalid_pct.any():
        print(f"AVISO: {invalid_pct.sum()} linhas com porcentagens fora do range 0-100")
    
    # Verificar consistência entre quantidade e porcentagem
    total_encontrada = df_clean['quantidade_encontrada'].sum()
    total_caderno = df_clean['quantidade_caderno'].sum()
    
    print(f"Total questões encontradas: {total_encontrada}")
    print(f"Total questões no caderno: {total_caderno}")
    print(f"Diferença: {abs(total_encontrada - total_caderno)}")
    
    # 7. ADICIONAR COLUNAS DERIVADAS ÚTEIS
    print("\n7. Adicionando colunas derivadas...")
    
    # Nível hierárquico (baseado no padrão da hierarquia)
    def get_hierarchy_level(hierarquia):
        if hierarquia == 'CATEGORIA_PRINCIPAL':
            return 0
        if pd.isna(hierarquia) or hierarquia == 'nan':
            return 0
        
        # Contar pontos para determinar nível
        dots = str(hierarquia).count('.')
        return dots + 1
    
    df_clean['nivel_hierarquia'] = df_clean['hierarquia'].apply(get_hierarchy_level)
    
    # Categoria principal (primeiro nível)
    def get_main_category(row):
        if row['nivel_hierarquia'] == 0:
            return row['topico']
        else:
            # Buscar a categoria principal correspondente
            main_cats = df_clean[df_clean['nivel_hierarquia'] == 0]['topico'].unique()
            # Lógica simplificada - você pode refinar isso
            return 'Categoria Não Identificada'
    
    # 8. ORDENAR POR HIERARQUIA
    print("\n8. Ordenando dados por hierarquia...")
    
    def hierarchy_sort_key(h):
        """Cria chave de ordenação para hierarquia"""
        if h == 'CATEGORIA_PRINCIPAL':
            return (0, 0, 0, 0)
        
        try:
            parts = str(h).split('.')
            # Preenche com zeros para garantir ordenação correta
            parts = [int(p) if p.isdigit() else 999 for p in parts]
            # Garante 4 níveis
            while len(parts) < 4:
                parts.append(0)
            return tuple(parts[:4])
        except:
            return (999, 999, 999, 999)
    
    df_clean['sort_key'] = df_clean['hierarquia'].apply(hierarchy_sort_key)
    df_clean = df_clean.sort_values('sort_key').drop('sort_key', axis=1)
    df_clean = df_clean.reset_index(drop=True)
    
    # 9. REMOVER DUPLICATAS (se existirem)
    print("\n9. Verificando duplicatas...")
    duplicates = df_clean.duplicated().sum()
    if duplicates > 0:
        print(f"Removendo {duplicates} linhas duplicadas...")
        df_clean = df_clean.drop_duplicates()
    else:
        print("Nenhuma duplicata encontrada")
    
    # 10. VALIDAÇÃO FINAL
    print("\n10. Validação final...")
    print(f"Dimensões finais: {df_clean.shape}")
    print(f"Valores nulos restantes:")
    print(df_clean.isnull().sum())
    
    # Estatísticas de qualidade
    print(f"\nResumo da limpeza:")
    print(f"- Colunas removidas: 1 (frequencia_acumulada)")
    print(f"- Colunas adicionadas: 3 (porcentagens numéricas + nível hierárquico)")
    print(f"- Valores nulos na hierarquia tratados: Substituídos por 'CATEGORIA_PRINCIPAL'")
    print(f"- Dados ordenados por hierarquia")
    print(f"- Porcentagens convertidas para formato numérico")
    
    return df_clean

# Executar limpeza
if __name__ == "__main__":
    # Carregar dados originais
    df_original = pd.read_excel('db-questoes.xlsx')
    
    # Aplicar limpeza
    df_cleaned = clean_dataframe(df_original)
    
    # Salvar resultado
    print("\n=== SALVANDO DADOS LIMPOS ===")
    
    # Salvar em múltiplos formatos
    df_cleaned.to_excel('db-questoes-limpo.xlsx', index=False)
    df_cleaned.to_csv('db-questoes-limpo.csv', index=False, encoding='utf-8')
    
    print("Arquivos salvos:")
    print("- db-questoes-limpo.xlsx")
    print("- db-questoes-limpo.csv")
    
    # Mostrar amostra dos dados limpos
    print("\n=== AMOSTRA DOS DADOS LIMPOS ===")
    print(df_cleaned.head(10).to_string())
    
    # Estatísticas finais
    print("\n=== ESTATÍSTICAS FINAIS ===")
    print(f"Total de registros: {len(df_cleaned)}")
    print(f"Total de tópicos únicos: {df_cleaned['topico'].nunique()}")
    print(f"Distribuição por nível hierárquico:")
    print(df_cleaned['nivel_hierarquia'].value_counts().sort_index())
    
    print("\n=== LIMPEZA CONCLUÍDA COM SUCESSO ===")