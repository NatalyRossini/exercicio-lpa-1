#QUESTÃO 1 de 4 (AULA 3)


print('Bem-vindo a Loja da Nataly Rossini')
valor_produto = float(input(' Entre com o valor do produto: ')) #Esta variável recebe o valor do produto.
quantidade = int(input(' Entre com valor do quantidade: ')) #Esta variável recebe a quantidade do produto.


valor_do_frete = 0 #Variável que recebe o valor do frete dependendo da quantidade de embalagens.
if 0 <= quantidade <11:
  valor_do_frete = 30
elif 11 <= quantidade < 101:
  valor_do_frete = 60
elif 101 <= quantidade <1001:
  valor_do_frete = 120
else:
  valor_do_frete = 240


valor_sem_frete = float(valor_produto * quantidade) #Variável responsável por receber o valor sem frete do produto x quantidade
valor_total = float(valor_sem_frete + valor_do_frete) #Variável responsável por receber o valor total, com frete incluso.
print('O valor sem frete foi: R$ {:.2f}'.format(valor_sem_frete)) #Imprime valor parcial, ou seja, sem acrescentar o frete.
print('O valor com frete foi: R$ {:.2f} (frete de: R${:.2f}) '.format(valor_total, valor_do_frete)) #Imprime valor total, já com o frete.