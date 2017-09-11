# -*- coding: utf-8 -*-
"""
         
Created on Mon Sep 11 17:37:12 2017

@author: Victor M. Israel
"""
import copy
 
kill = False #ao achar uma combinação head-tail, o programa irá parar de gerar permutações novas
contador = 0
head_tail_counter = 0 #controlará quantas strings que se encaixam na definição de head_tail foram encontradas

def entrada_usuario():
    qtdade_palavras = (int(input("entre com a quantidade de palavras desejadas: ")))
    while(qtdade_palavras < 2 or qtdade_palavras > 100):
        print("A quantidade de palavras deve ser de pelo menos dois e de no máximo 100, digite uma quantidade adequada.")
        qtdade_palavras = (int(input("entre com a quantidade de palavras desejadas: ")))
    return qtdade_palavras        
def printa_permutacao():# verificará se alguma permutação gerada é head tail, se for, a combinação será adicionada  a lista "head_tail"
     #print( "permutacao",contador,": ")
     global head_tail_counter
     for i in range(len(permutacao)):
        #print(permutacao[i], " indice ", i, " headtailcounter ", head_tail_counter)
        if i + 1 == len(permutacao):
            pass
        elif permutacao[i][-1] == permutacao[i + 1][0]:
            head_tail_counter += 1
        if head_tail_counter == len(permutacao)-1:
            head_tail_counter = 0
            global kill
            kill = True
            for i in range(len(permutacao)):
                head_tail.append(permutacao[i])
     if(head_tail_counter != len(permutacao)-1):
         head_tail_counter = 0
    # print()    
def printar_permutacoes_head_tail():
    print("HEAD TAIL:")
    for el in head_tail:
        print(el)         
def permuta_inicial(vet): #iniciará a pilha de recursão   
    permutar(vet, 0)
def permutar(vet, n):# irá gerar todas as permutacoes das palavras fornecidas pelo usuário
    global kill
    if(kill is True):
        return
    if n == len(vet):
        global contador
        contador += 1
        printa_permutacao()
    else:
        for i in range(len(vet)):
            repetido = False
            for j in range(0,n):
                if permutacao[j] == vet[i]:
                    repetido = True   
            if  not repetido:
                permutacao[n] = vet[i]
                permutar(vet, n+1)
                
qtdade_palavras = entrada_usuario()
lista_palavras = []
head_tail = []

for x in range(qtdade_palavras):
    print("digite a palavra",x+1,":" )
    x = input("").strip().lower() #irá remover qualquer espaço em branco entre o começo e o final de uma palavra e botará todos os caracteres para minúsculo
    lista_palavras.append(x)
    
permutacao = copy.deepcopy(lista_palavras) #copia o CONTEÚDO do vetor de palavras
permuta_inicial(lista_palavras)
printar_permutacoes_head_tail()
