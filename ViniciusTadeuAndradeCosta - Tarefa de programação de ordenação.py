# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:45:40 2020

@author: vinit
"""

def mergesort(vetor): #definçao do metodo Merge Sort e passando o vetor A como partemento para a ordenação seja realizada
  
    if len(vetor)>1: #condiçao se o tamanho do vetor é maior que 1
        m = len(vetor)//2 # divsao de vetor A ao meio 
        esquerda = vetor[:m] # vetor esquerda recebera a parte da esquerda do vetor A
        direita = vetor[m:] # vetor direita recebera a parte da direita do vetor A
        esquerda = mergesort(esquerda) # chamada recursiva do metodo Merge Sort com a parte o vetor esquerda
        direita = mergesort(direita) # chamada recursiva do metodo Merge Sort com a parte o vetor direita
  
        vetor =[] # criação de um vetor vazia para receber a ordenção
  
        while (len(esquerda)>0 and len(direita)>0): # laço que se repetira enquando os vetores esquerda e direita tiveram tamano maior que 0
            if esquerda[0]<direita[0]: # condiçao se a primeira posição do vetor esquerda for menor que a primeira posição do vetor esquerda
                vetor.append(esquerda[0]) # caso satizfeita o vetor recebera o valor da primeira posiçao do vetor esquerda
                esquerda.pop(0) # remoçao do valor da primeira posição do vetor esquerda
            else: #senão
                vetor.append(direita[0]) #caso a condiçao não seja satizfeita o vetor recebera o valor da primeira posição do veotr direita
                direita.pop(0) # remoçao do valor da primeira posição do vetor direita
  
        for i in esquerda: # for que rodará a partir do tamanho do vetor esquerda
            vetor.append(i) # adiciona o valor de i em vetor
        for i in direita: # for que rodará a partir do tamanho do vetor direita
            vetor.append(i) # adiciona o valor de i em vetor
                  
    return vetor #retorno do vetor ordenado
  
def main():
    A = [9 , 10 , -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0] # vetor proposto no problema
    print("\nDado um vetor A: ",A) # mostrar o vetor proposto para verificar que o mesmo esta desordenado
    
    vetorOrdenado = mergesort(A) #chamado do metodo Merge Sort com o vetor A e sentando em vetorOrdenado
      
    print("\nA ordenação usando o Merge Sort terá a segunite saída: ") # mostrar o vetor ja ordenado
    print(vetorOrdenado) 

main()