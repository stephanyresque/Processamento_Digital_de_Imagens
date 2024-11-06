import cv2
import os

pasta_entrada = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_originais_2'
pasta_saida = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\realce\\high_boost'

fator_boost = 1.5
offset_brilho = 50

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):
    if not (nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.jpeg') or nome_arquivo.endswith('.png')):
        continue

    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
    imagem = cv2.imread(caminho_entrada)

    # Aplicação do filtro High Boost
    imagem_suavizada = cv2.GaussianBlur(imagem, (15, 15), 0)
    high_boost = cv2.addWeighted(imagem, fator_boost, imagem_suavizada, -1, offset_brilho)

    # Nome do arquivo sem extensão e a extensão original
    nome_base, extensao = os.path.splitext(nome_arquivo)

    # Novo nome no formato "img x.nome do filtro" com a extensão original
    nome_saida = f'{nome_base}.high_boost{extensao}'

    # Salvando a imagem
    cv2.imwrite(os.path.join(pasta_saida, nome_saida), high_boost)

print("Imagens com filtro High Boost (com ajuste de brilho) processadas e salvas com sucesso!")
