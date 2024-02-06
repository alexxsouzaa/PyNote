import os
from pdf2image import convert_from_path
 
# Caminho do arquivo PDF
pdf_path = 'PDF_TESTE.pdf'

# Extrai o nome do arquivo
extensao_arquivo = pdf_path.find('.')
nome_arquivo= pdf_path[0:extensao_arquivo]

# Armazena o arquivo a ser convertido
images = convert_from_path(pdf_path)

# Diretório para onde o arquivo sera exportado
output_diretorio = "./OUTPUT_FOLDER"

if not os.path.exists(output_diretorio):
    os.makedirs(output_diretorio)

for i in range(len(images)):
    # Salva a imagem
    images[i].save(os.path.join(output_diretorio, f'{nome_arquivo}_page{i}.jpg'), 'JPEG')
