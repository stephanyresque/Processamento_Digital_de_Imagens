import cv2
import os

pasta_entrada = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_originais'
pasta_saida = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\contrastar\\histograma'

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):
    
    if not (nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.png')):
        continue
    
    
    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
    
    imagem = cv2.imread(caminho_entrada)
    
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    equalized_gray = cv2.equalizeHist(imagem_gray)
    
    imagem_yuv = cv2.cvtColor(imagem, cv2.COLOR_BGR2YUV)
    imagem_yuv[:, :, 0] = cv2.equalizeHist(imagem_yuv[:, :, 0])  
    equalized_color = cv2.cvtColor(imagem_yuv, cv2.COLOR_YUV2BGR)
    
    nome_colorido = f'equalized_color_{nome_arquivo}'
    nome_cinza = f'equalized_gray_{nome_arquivo}'
    
    cv2.imwrite(os.path.join(pasta_saida, nome_colorido), equalized_color)
    cv2.imwrite(os.path.join(pasta_saida, nome_cinza), equalized_gray)

print("Imagens com equalização de histograma processadas e salvas com sucesso!")
