# -*- coding: utf-8 -*-
"""
Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
a = input ('Digite algo! ')
print ('O tipo primitivo desse valor é: ', type(a))
print ('Só tem espaço?', a.isspace())
print ('É um número?', a.isnumeric())
