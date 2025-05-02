valorMercadoria = float (input("digite o valor da mercadoria: "))
descontoPercentual = float (input(" digite o percentual de desconto: "))
pagamentoTotal = valorMercadoria - descontoPercentual/ 100 * valorMercadoria
print ("total a pagar com o desconto escolhido é: ", pagamentoTotal)
input()
