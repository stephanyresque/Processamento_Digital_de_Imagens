import cv2
import os

pasta_entrada = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_originais'
pasta_saida = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\suavizacao\\mediana'

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):
    if not (nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.png')):
        continue

    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)

    imagem = cv2.imread(caminho_entrada)

    # Aplicação dos filtros
    median_blur_color = cv2.medianBlur(imagem, 15)
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    median_blur_gray = cv2.medianBlur(imagem_gray, 15)

    # Nome do arquivo sem a extensão
    nome_base = os.path.splitext(nome_arquivo)[0]

    # Novos nomes no formato "img x.nome do filtro"
    nome_colorido = f'{nome_base}.median_blur_color.jpg'
    nome_cinza = f'{nome_base}.median_blur_gray.jpg'

    # Salvando as imagens
    cv2.imwrite(os.path.join(pasta_saida, nome_colorido), median_blur_color)
    cv2.imwrite(os.path.join(pasta_saida, nome_cinza), median_blur_gray)

print("Imagens com filtro Mediana processadas e salvas com sucesso!")
