
import random
""" Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min. """
from random import sample
def exercicio1():
    listaRandom = sample(range(100),10)
    maior = 0
    menor = 101
    for valor in listaRandom:
        if valor>maior:
            maior = valor
        if valor<menor:
            menor = valor 
    print(listaRandom)
    print(maior, menor)
exercicio1()