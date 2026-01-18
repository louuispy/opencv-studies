# Estudos - OpenCV

# Aula 003 - Padding e Subplots

# Versões do Python e das bibliotecas usadas
# Python == 3.9.25
# Opencv == 4.12.0.88
# Numpy == 2.0.2
# Matplotlib == 3.9.4

# ------------------------------------------------------

# Revisão: Aula 002

"""
Aprendemos sobre:

- Conversão de imagem para grayscale utilizando a flag 0 ao ler a imagem: cv2.imread('caminho/imagem', 0)
- Como uma máquina lê uma imagem: matriz de pixels, com cada pixel tendo cores em RGB
- Acessar as dimensões (largura x altura) e quantidade de canais de cores de uma imagem usando .shape()
- Acessar os pixels de uma imagem e os canais de cores separadamente usando indexação e loop for
- Modificar os canais de cores de uma imagem, também com loop for
- Extrair uma região de interesse da imagem usando indexação
- Adicionar região de inteteresse por cima da imagem original em algum pixel

"""

# ------------------------------------------------------

# 001 - Criando bordas em imagens

""" 
Por que criar bordas em imagens?

- Trabalhar em imagens com tamanhos diferentes, mas que precisam ter o mesmo tamanho

- Uma solução para isso é redimensionar, porém você pode perder o dado original

- Em pesquisas de base de dados, você precisa do dado original, que tá na base, perder esse dado iria atrapalhar e possivelmente enviesar a análise

- Aplicando uma mesma borda em todas as imagens, com tamanhos diferentes, é uma solução mais viável, pois causa uma menor perda dos dados originais

"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def show_image_grid(img, title):
    fig, axis = plt.subplots()
    '''
    Aqui, definimos que nosso plot terá subplots, ou seja, sub-áreas onde poderemos fazer algum desenho.

    Quando temos apenas 1 subplot, já é lido automaticamente como subplot de 1 linha e 1 coluna.

    fig = A figue, a janela inteira. Podemos usar essa fig para controlar o tamanho da tela, layout, espaçamento e etc. Lembrando: fig != plot. Plot é basicamente a ação de desenhar algo em uma figure. A figure é a janela onde vai ser feito o desenho.

    axis = de forma simples, é cada subplot que será feito. se nós temos 6 axis, então temos 6 subplots. Cada subplot será em um axis próprio. É sempre feito um desenho por axis.

    Quem faz o desenho é o axis, então quando fazemos plt.plot, por baixo dos panos, o que acontece realmente é um axis.plot, pois somente o axis a capacidade de desenhar!
    '''
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def showMultipleImageGrid(imgs_array, titles_array, x, y):
    if(x < 1 or y < 1):
        print('ERRO: X e Y não podem ser menor ou igual a zero. Não é possível fazer a plotagem com zero colunas ou zero linhas!')
        return
    elif(x == 1 and y == 1):
        show_image_grid(imgs_array, titles_array)
    elif(x == 1):
        fig, axis = plt.subplots(y)
        fig.suptitle(titles_array)
        y_id = 0
        for img in imgs_array:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[y_id].imshow(imgMPLIB)

            y_id += 1

    elif(y == 1):
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titles_array)
        x_id = 0
        for img in imgs_array:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[x_id].imshow(imgMPLIB)

            x_id += 1
    else: 
        fig, axis = plt.subplots(y, x)
        imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x_id, y_id, title_id = 0, 0, 0
        for img in imgs_array:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[y_id, x_id].set_title(titles_array[title_id])
            axis[y_id, x_id].imshow(imgMPLIB)
            if (len(titles_array[title_id]) == 0):
                axis[y_id, x_id].axis('off')

            title_id += 1
            x_id += 1
            if x_id == x:
                x_id = 0
                y_id += 1
    
    plt.show()


def plot_two_image_horizontal():
    img_original = cv2.imread('imagens\cat.png')
    img_replicate = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REPLICATE)

    # cv2.copyMakeBorder cria uma borda, do tamanho que você quiser, na imagem

    # os números 100 é quantidade de pixels da borda de cada lado (top, bottom, left, right)

    # cv2.BORDER_REPLICATE replica a cor do último pixel da imagem para ser a mesma cor das bordas. Em tese não é a cor, mas sim o pixel em si que é replicado

    

    # criando grid com 2 imagens, a segunda com borda replicada
    imgs_array = [img_original, img_replicate]
    title = 'Imagem original e Imagem com borda replicada'
    showMultipleImageGrid(imgs_array, title, 2, 1)

def main():
    img = cv2.imread('imagens\cat.png')

    # Exibindo apenas uma imagem
    # showImageGrid(img, "Gatinho")

    # Exibindo duas imagens horizontalmente
    plot_two_image_horizontal()


main()