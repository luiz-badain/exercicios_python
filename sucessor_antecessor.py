#1-Faça um programa em Python que leia um número inteiro e imprima o seu sucessor e seu antecessor, na mesma linha.

numero = int(input('Coloque um número: '))
sucessor = numero + 1
antecessor = numero - 1
print('O sucessor de {} é {}, e o seu antecessor é {}'.format(numero,sucessor,antecessor))