import os
import shutil

# Pasta com os arquivos .txt originais
pasta_txt_origem = 'C:\\Users\\steph\\OneDrive\\Documentos\\labels_txt'
# Pasta onde os arquivos .txt duplicados serão salvos (ex: pasta de filtros Cores RGB)
pasta_txt_destino = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\canais_rgb'

# Definir as variações específicas para o filtro Cores RGB
variacoes = ["canal_vermelho", "canal_verde", "canal_azul"]

# Iterar sobre cada arquivo .txt na pasta de origem
for nome_txt_origem in os.listdir(pasta_txt_origem):
    if nome_txt_origem.endswith('.txt'):
        # Extrair o nome base (ex: "img 0") sem a extensão
        nome_base = os.path.splitext(nome_txt_origem)[0]

        # Para cada variação, criar uma cópia do arquivo .txt original
        for variacao in variacoes:
            # Nome do novo arquivo .txt com a variação
            nome_txt_destino = f"{nome_base}.{variacao}.txt"
            caminho_txt_origem = os.path.join(pasta_txt_origem, nome_txt_origem)
            caminho_txt_destino = os.path.join(pasta_txt_destino, nome_txt_destino)

            # Copiar e renomear o arquivo .txt
            shutil.copy(caminho_txt_origem, caminho_txt_destino)
            print(f'Arquivo {nome_txt_origem} copiado como {nome_txt_destino}')
