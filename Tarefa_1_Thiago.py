import sys
import cv2 as cv
import numpy as np
import os

def main(argv):

    #Converte a imagem para grayscale fazendo a média entre os valores RGB. 
    def convertToGrayScale(img):
        temp = np.copy(img)
        for i in range(temp.shape[0]):
            for j in range(temp.shape[1]):
                temp[i][j] = np.mean(temp[i][j])
        return temp
    
    #Função auxiliar para colocar duas imagens na mesma resolução para poder fazer a subtração.
    #O rescale das imagens foram feito usando a função resize do opencv.
    #A resolução é escolhida usando o menor valor de altura e de largura entre as duas imagens de entrada.
    def convertToSameResolution(img1, img2):
        temp1 = np.copy(img1)
        temp2 = np.copy(img2)
        heigth = np.min([temp1.shape[0], temp2.shape[0]])
        width = np.min([temp1.shape[1], temp2.shape[1]])
        temp1 = cv.resize(temp1, (width, heigth))
        temp2 = cv.resize(temp2, (width, heigth))
        return (temp1, temp2)
    
    #Subtração pixel a pixel de duas imagens de mesma resolução.
    def subtractImage(img1, img2):
        temp1 = np.copy(img1)
        temp2 = np.copy(img2)
        for i in range(temp1.shape[0]):
            for j in range(temp1.shape[1]):
                temp1[i][j] = temp2[i][j] - temp1[i][j]
        return temp1

    #Leitura dos arquivos na pasta imagens - Mudar o path de acordo com a localização da imagen utilizada.
    src1 = argv[0] if len(argv) > 0 else '/Users/thiago/Documents/Pós Graduação/ACI/codes/ACI - Tarefa 1/images/backtothefuture.jpeg'
    src2 = argv[0] if len(argv) > 0 else '/Users/thiago/Documents/Pós Graduação/ACI/codes/ACI - Tarefa 1/images/mr-robot.png'
    
    img1 = cv.imread(cv.samples.findFile(src1))
    img2 = cv.imread(cv.samples.findFile(src2))
    gray1 = convertToGrayScale(img1)
    gray2 = convertToGrayScale(img2)
    res1, res2 = convertToSameResolution(img1, img2)
    sub = subtractImage(res1, res2)

    cv.imshow("Imagem original 1", img1)
    cv.imshow("Imagem original 2", img2)
    cv.imshow('Grayscale 1', gray1)
    cv.imshow('Grayscale 2', gray2)
    cv.imshow('Rescale 1', res1)
    cv.imshow('Rescale 2', res2)
    cv.imshow('Subtract images', sub)
    
    c = cv.waitKey(0)
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])


