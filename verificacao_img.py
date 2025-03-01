from PIL import Image

def verificar_rotacionar(image_path):
    
    try:
        with Image.open(image_path) as img:
            largura, altura = img.size

            if largura > altura:
                return 'Horizontal'
            elif largura < altura:
                
                img_rotacionada = img.rotate(-90, expand=True)
                
                novo_caminho = image_path.replace(".", "_horizontal.")
                
                img_rotacionada.save(novo_caminho)

                return f"A imagem estava na vertical e foi rotacionada. Nova imagem salva em: {novo_caminho}"
            else:
                return "A imagem é quadrada. Nenhuma alteração foi feita."
            
    except Exception as e:
        return f'Erro ao carregar a imagem {e}'

caminho_da_imagem = "C:\\Users\\steph\\Downloads\\teste1_vertical.jpeg"  
resultado = verificar_rotacionar(caminho_da_imagem)
print(f"A imagem está: {resultado}")
        