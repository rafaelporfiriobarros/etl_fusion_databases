# ETL - Fusão de Dados

Este repositório contém dois scripts em Python para processamento e fusão de dados provenientes de arquivos JSON e CSV.

## Estrutura do Repositório

- `data_processing.py`: Módulo contendo a classe `Data`, que oferece funcionalidades para leitura, manipulação e salvamento de dados.
- `fusion_data.py`: Script que utiliza a classe `Data` para carregar, transformar e combinar dados de diferentes fontes.
- `data_raw/`: Pasta onde devem ser armazenados os arquivos de entrada.
- `data_processed/`: Pasta onde serão salvos os arquivos processados.

## Descrição dos Scripts

### `data_processing.py`
Este script define a classe `Data`, que implementa os seguintes métodos:

- `data_read(path, data_type)`: Lê um arquivo JSON ou CSV e retorna um objeto `Data`.
- `rename_columns(key_mapping)`: Renomeia colunas de acordo com um dicionário de mapeamento.
- `join(dataA, dataB)`: Combina dois conjuntos de dados em um único objeto `Data`.
- `save_data(path)`: Salva os dados processados em formato CSV.

### `fusion_data.py`
Este script executa o fluxo completo de processamento de dados:

1. **Extração**: Carrega dados de um arquivo JSON e um CSV.
2. **Transformação**: Renomeia colunas do CSV para padronização.
3. **Fusão**: Une os dois conjuntos de dados.
4. **Carregamento**: Salva os dados combinados em um novo arquivo CSV na pasta `data_processed/`.

## Como Utilizar

1. Certifique-se de que os arquivos de entrada estão na pasta `data_raw/`.
2. Execute o script `fusion_data.py`:
   ```bash
   python fusion_data.py
   ```
3. O arquivo processado será salvo em `data_processed/dados_combinados.csv`.

## Dependências

- Python 3.x
- Nenhuma biblioteca externa além das padrões (`json`, `csv`)


