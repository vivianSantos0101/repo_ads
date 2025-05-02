import random
vetor1=[]
vetor2=[]
vetor3=[]
for elemento in range(10):
   numeroR= random.randint(1,100)
   numeroX= random.randint(1,100)
   vetor1.append(numeroR)
   vetor2.append(numeroX)
   vetor3.append(numeroR)
   vetor3.append(numeroX)
print(vetor1)
print(vetor2)
print(vetor3)