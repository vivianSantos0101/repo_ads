'''Sorteie 20 inteiros entre 1 e 100 numa lista. 
Armazene os números pares na lista PAR e os 
números ímpares na lista IMPAR. Imprima as três listas. '''
import random
par = []
impar = []
def exercicio2 ():
    listaRandom = random.sample(range(100),20)
    for resultado in listaRandom:
      if resultado%2 == 0: 
        par.append(resultado)
      else:
        impar.append(resultado)
    print(listaRandom,par,impar)
exercicio2 ()
        