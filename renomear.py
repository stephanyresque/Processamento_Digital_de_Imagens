import os

# Caminho da pasta onde estão as imagens
pasta_imagens = r'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_recortadas'

# Itera sobre cada arquivo na pasta
for nome_arquivo in os.listdir(pasta_imagens):
    # Verifica se o arquivo contém o texto '-removebg-preview'
    if '-removebg-preview' in nome_arquivo:
        # Cria o novo nome removendo o texto indesejado
        novo_nome = nome_arquivo.replace('-removebg-preview', '').replace('_', ' ')
        # Caminhos completos para renomear o arquivo
        caminho_antigo = os.path.join(pasta_imagens, nome_arquivo)
        caminho_novo = os.path.join(pasta_imagens, novo_nome)
        
        # Renomeia o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f'Renomeado: {nome_arquivo} -> {novo_nome}')

print("Renomeação concluída.")
