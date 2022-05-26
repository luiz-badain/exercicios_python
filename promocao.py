#3-Faça um programa em Python que leia dois números reais, um será o valor de um produto e outro o valor de desconto que esse produto está recebendo. Imprima quantos reais o produto custa na promoção.

valor=float(input('Coloque o valor do produto:'));
desconto=float(input('Coloque o valor do desconta:'));

print('O valor da promoção é de:',valor-desconto)