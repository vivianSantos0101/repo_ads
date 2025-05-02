import random 
v = random.sample(range(1,101),10)
maior = menor = v[0]
for x in v [1:]:
    if x > maior: maior = x
    if x < maior: menor = x
    print("v:", v)
    print(f'maior: {maior}')
    print(f'menor: {menor}')


