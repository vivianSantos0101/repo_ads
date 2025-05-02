dia = int(input ("digite o dia : "))
hora = int(input ("digite a hora : "))
minuto = int(input ("digite o minuto : "))
segundos = int(input ("digite os segundos: "))

dia = dia * 86.400
hora = hora * 3.600
minuto = minuto * 0.6

print(f" o total de segundos é{dia + hora + minuto + segundos: .3f}")

