import cv2
import os

pasta_entrada = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_originais_2'
pasta_saida = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\contrastar\\histograma'

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):
    if not (nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.jpeg') or nome_arquivo.endswith('.png')):
        continue

    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
    imagem = cv2.imread(caminho_entrada)

    # Processamento da imagem em tons de cinza
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    equalized_gray = cv2.equalizeHist(imagem_gray)

    # Processamento da imagem colorida em YUV
    imagem_yuv = cv2.cvtColor(imagem, cv2.COLOR_BGR2YUV)
    equalized_yuv = cv2.equalizeHist(imagem_yuv[:, :, 0])
    equalized_color = cv2.cvtColor(imagem_yuv, cv2.COLOR_YUV2BGR)

    # Nome do arquivo sem extensão e a extensão original
    nome_base, extensao = os.path.splitext(nome_arquivo)

    # Novos nomes com a extensão original
    nome_colorido = f'{nome_base}.equalized_color{extensao}'
    nome_cinza = f'{nome_base}.equalized_gray{extensao}'

    # Salvando as imagens
    cv2.imwrite(os.path.join(pasta_saida, nome_colorido), equalized_color)
    cv2.imwrite(os.path.join(pasta_saida, nome_cinza), equalized_gray)

print("Imagens com equalização de histograma processadas e salvas com sucesso!")
