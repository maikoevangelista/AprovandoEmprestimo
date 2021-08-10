casa = float(input('valor da casa: R$'))
salario = float(input('salario do comprador: R$'))
anos = int(input('quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {} anos,'.format(casa,anos ), end='')
print('a prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print ('empréstimo pode ser CONCEDIDO!')
else:
    print('empréstimo NEGADO!')