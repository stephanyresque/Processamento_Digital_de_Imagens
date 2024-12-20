import cv2
import os

pasta_entrada = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_originais_2'
pasta_saida = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\suavizacao\\bilateral'

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):
    if not (nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.jpeg') or nome_arquivo.endswith('.png')):
        continue

    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
    imagem = cv2.imread(caminho_entrada)

    # Aplicação dos filtros com suavização menor
    bilateral_blur_color = cv2.bilateralFilter(imagem, 9, 50, 50)
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    bilateral_blur_gray = cv2.bilateralFilter(imagem_gray, 9, 50, 50)

    # Nome do arquivo sem extensão e a extensão original
    nome_base, extensao = os.path.splitext(nome_arquivo)

    # Novos nomes com a extensão original
    nome_colorido = f'{nome_base}.bilateral_blur_color{extensao}'
    nome_cinza = f'{nome_base}.bilateral_blur_gray{extensao}'

    # Salvando as imagens
    cv2.imwrite(os.path.join(pasta_saida, nome_colorido), bilateral_blur_color)
    cv2.imwrite(os.path.join(pasta_saida, nome_cinza), bilateral_blur_gray)

print("Imagens com filtro Bilateral Filter processadas e salvas com sucesso!")
