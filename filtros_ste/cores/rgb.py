import cv2
import os

pasta_entrada = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_originais_2'
pasta_saida = 'C:\\Users\\steph\\OneDrive\\Documentos\\imagens_filtros\\canais_rgb'

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):
    if not (nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.jpeg') or nome_arquivo.endswith('.png')):
        continue

    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
    imagem = cv2.imread(caminho_entrada)

    # Separação dos canais RGB
    b, g, r = cv2.split(imagem)

    imagem_b = cv2.merge([b, b, b])  # Canal azul isolado
    imagem_g = cv2.merge([g, g, g])  # Canal verde isolado
    imagem_r = cv2.merge([r, r, r])  # Canal vermelho isolado

    # Nome do arquivo sem extensão e a extensão original
    nome_base, extensao = os.path.splitext(nome_arquivo)

    # Novos nomes com a extensão original
    nome_azul = f'{nome_base}.canal_azul{extensao}'
    nome_verde = f'{nome_base}.canal_verde{extensao}'
    nome_vermelho = f'{nome_base}.canal_vermelho{extensao}'

    # Salvando as imagens
    cv2.imwrite(os.path.join(pasta_saida, nome_azul), imagem_b)
    cv2.imwrite(os.path.join(pasta_saida, nome_verde), imagem_g)
    cv2.imwrite(os.path.join(pasta_saida, nome_vermelho), imagem_r)

print("Imagens dos canais RGB processadas e salvas com sucesso!")
