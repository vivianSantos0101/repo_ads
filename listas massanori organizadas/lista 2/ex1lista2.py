a = int(input("digite o lado a: "))
b = int(input("digite o lado b: "))
c = int(input("digite o lado c: "))

if(a == b == c):
   print(" seu triangulo é equilatero")
elif(a == b != c or b == c != a or c == a != b):
   print("seu triangulo é isósceles")
elif(a != b != c):
   print (" seu triangulo é escaleno")
   