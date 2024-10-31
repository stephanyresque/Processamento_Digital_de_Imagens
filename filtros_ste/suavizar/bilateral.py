import cv2
import os

pasta_entrada = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_originais'
pasta_saida = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\suavizacao\\bilateral'

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):

    if not (nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.png')):
        continue
    
    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
    
    imagem = cv2.imread(caminho_entrada)
    
    bilateral_blur_color = cv2.bilateralFilter(imagem, 15, 75, 75)
    
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    bilateral_blur_gray = cv2.bilateralFilter(imagem_gray, 15, 75, 75)
    
    nome_colorido = f'bilateral_blur_color_{nome_arquivo}'
    nome_cinza = f'bilateral_blur_gray_{nome_arquivo}'
    
    cv2.imwrite(os.path.join(pasta_saida, nome_colorido), bilateral_blur_color)
    cv2.imwrite(os.path.join(pasta_saida, nome_cinza), bilateral_blur_gray)

print("Imagens com filtro Bilateral Filter processadas e salvas com sucesso!")
