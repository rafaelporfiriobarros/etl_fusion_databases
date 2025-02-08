import json
import csv

from data_processing import Data

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract

try:
    dados_empresaA = Data.data_read(path_json, 'json')
    print(dados_empresaA.column_name)
    print(dados_empresaA.rows_amount)
except Exception as e:
    print(f"Erro ao ler o arquivo JSON: {e}")

try:
    dados_empresaB = Data.data_read(path_csv, 'csv')
    print(dados_empresaB.column_name)
    print(dados_empresaB.rows_amount)
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")

# Transform

key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.column_name)

# Garantir que a chave de junção está sendo definida corretamente
try:
    dados_fusao = Data.join(dados_empresaA, dados_empresaB)
    print(dados_fusao.column_name)
    print(dados_fusao.rows_amount)
except Exception as e:
    print(f"Erro ao juntar os dados: {e}")

# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'

try:
    dados_fusao.save_data(path_dados_combinados)
    print(f"Dados salvos em: {path_dados_combinados}")
except Exception as e:
    print(f"Erro ao salvar os dados: {e}")
