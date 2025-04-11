print('*-- Calculo do IT --*')

#entrada de dados
salario = float(input('Salário: '))

#processamento
if salario < 0:
    print('Salário Negativo!')
elif salario <=1903.98:
    print('Isento')
elif salario >= 1903.99 and salario <= 2826.65:
    ir = salario * 0.075
elif salario >= 2826.66 and salario <= 3751.06:
    ir = salario * 0.15
elif salario >= 3751.07 and salario <= 4664.68:
    ir = salario * 0.225
elif salario >= 4664.69:
    ir = salario * 0.275

print(f'Salário: {salario:.2f} \nImposto: {ir} \nLiquido: {salario_ir}')