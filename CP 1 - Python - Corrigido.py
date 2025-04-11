# Andrei de Paiva Gibbini - RM 563061
''''''

print('* -- Exercício 1 - CP - Calcular Comissão --*')

#Entrada de Dados
nome = (input('Vendedor: '))
salario_fixo = float(input('Salário: '))
tv_seg_qua = float(input('Vendas (Seg-Qua): '))
tv_qui_sex = float(input('Vendas (Qui-Sex): '))
tv_sab_dom = float(input('Vendas (Sab-Dom): '))

#Processamento
comissao_seg_qua = tv_seg_qua *0.2
comissao_qui_sex = tv_qui_sex *0.15
comissao_sab_dom = tv_sab_dom *0.1 #(10/100)

total_comissao = comissao_seg_qua + comissao_qui_sex + comissao_sab_dom

total_receber = salario_fixo + total_comissao

#Saída de dados
print(f'Vendedor: {nome}')
print(f'Salário Fixo: {salario_fixo:.2f}')
print(f'Vendedor: {total_comissao:.2f}')
print(f'Vendedor: {total_receber:.2f}')