import math as mt
import string

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# soma = numero1 + numero2
# print(f'A soma dos números é {soma}')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero1 = int(input("Digite um número: "))
# resto = numero1 % 5
# print(f'O resto da divisão por 5 é {resto}')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# produto = numero1 * numero2
# print(f'O produto dos números é {produto}')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# divisão = numero1 // numero2
# print(f'A divisão inteira dos números é {divisão}')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero1 = int(input("Digite um número: "))
# quadrado = numero1 ** 2
# print(f'O quadrado do número é {quadrado}')


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))
# soma = numero1 + numero2
# print(f'A soma dos números é {soma}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))
# media = (numero1 + numero2) / 2  # A divisão converte para float automaticamente, se necessário
# print(f'A media dos números é {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))
# potencia = numero1 ** numero2
# print(f'O número {numero1} elevado a {numero2} é: {potencia}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# numero1 = float(input("Digite um número: "))
# farenheit = (numero1 * 1.8) + 32
# print(f'A temperatura {numero1}ºC equivale a {farenheit:.2f}F')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# numero1 = float(input("Digite o raio da circunferência: "))
# area = 2 * mt.pi * numero1 ** 2
# print(f'A área do círculo é: {area:.2f}')


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = input("Digite um texto: ")
# maiusculo = texto.upper()
# print(f'Esse é o seu texto maiúsculo: {maiusculo}')

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = input('Digite seu nome completo: ')
# nome_capitalizado = string.capwords(nome)
# # nome_capitalizado = nome.title()
# print(f'O nome com iniciais maiúsculas é: {nome_capitalizado}')

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input('Digite uma frase: ')
# frase_trimmada = frase.strip()
# print(f'Frase sem espaços no começo e no final: {frase_trimmada}')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato dd/mm/aaaa: ")
# dia = data.split('/')[0]
# mes = data.split('/')[1]
# ano = data.split('/')[2]
# print(f'Esses são o dia: {dia}, mês: {mes} e ano: {ano}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# palavra1 = input("Digite uma palavra: ")
# palavra2 = input("Digite outra palavra: ")
# frase  = palavra1 + ' ' + palavra2
# print(f'Aqui está sua frase: {frase}')

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# valor1 = input("Digite um valor booleano: ")
# valor2 = input("Digite outro valor booleano: ")
# resultado = valor1 and valor2
# print(resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# valor1 = input("Digite um valor booleano: ")
# valor2 = input("Digite outro valor booleano: ")
# resultado = valor1 or valor2
# print(resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor1 = input("Digite um valor booleano: ").lower().strip() == 'true' 
# Quando precisar de um input booleano, sempre comparar o texto do usuário com o valor que se quer.
# Se eu colocar só bool(input("Digite...")) o python irá verificar se existe uma string no input. Se sim, irá sempre retornar True, independente do que foi escrito.
# Precisamos comparar a string com algo para aí sim termos um valor True ou False.
print(not valor1)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.



# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.




# #### try-except e if

# 21: Conversor de Temperatura



# 22: Verificador de Palíndromo



# 23: Calculadora Simples



# 24: Classificador de Números



# 25: Conversão de Tipo com Validação



