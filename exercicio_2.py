print('------------------------------------------------------------------------------------')
print('|          Bem vindo(a) à soverteria Genérica!            |')
print('|----------------------------------------------------------------------------------|')
print('| N° de bolas |  Sabor tradicional (TR) | Sabor premium (PR)  | Sabor especial (ES)|')
print('|      1      |        R$ 6,00          |       R$ 7,00       |      R$ 8,00       |')
print('|      2      |        R$ 11,00         |       R$ 13,00      |      R$ 15,00      |')
print('|      3      |        R$ 15,00         |       R$ 18,00      |      R$ 21,00      |')
print('------------------------------------------------------------------------------------')

sabor = ('')
numb = preco = total = 0

while True: #Enquanto for verdadeiro
  sabor = str(input('Entre com o sabor desejado (TR/PR/ES): '))
  sabor = sabor.upper() #função para deixar a string digitada em letras maiusculas
  if sabor != 'TR' and sabor != 'PR' and sabor != 'ES':
      print('Sabor inválido. Tente novamente.') # mostre na tela o erro
      print('') # print vazio para separar as frases/funçao apenas estetica
      continue # volta ao inicio e refaz o pedido

  else:
    numb = int(input('Entre com o número de bolas de sorvete desejado (1/2/3): ')) # entrada para o numero de bolas
    if numb != 1 and numb != 2 and numb != 3: # se a entrada for diferente dos números disponíveis
      print('Número de bolas de sorvete inválido. Tente novamente.') # exibe essa mensagem
      print('') # print vazio para separar as frases/funçao apenas estetica
      continue
    elif numb == 1 and sabor == 'TR': # se for uma bola e sabor tradicional
      preco =  6
    elif numb == 1 and sabor == 'PR': # para 1 bola e sabor premium
      preco =  7
    elif numb == 1 and sabor == 'ES': # 1 bola e sabor especial
      preco =  8

    #valores para 2 bolas
    elif numb == 2 and sabor == 'TR':
      preco =  11
    elif numb == 2 and sabor == 'PR':
      preco =  13
    elif numb == 2 and sabor == 'ES':
      preco =  15

    #valores para 3 bolas
    elif numb == 3 and sabor == 'TR':
      preco =  15
    elif numb == 3 and sabor == 'PR':
      preco =  18
    elif numb == 3 and sabor == 'ES':
      preco =  21
  print('') # print vazio para separar as frases/funçao apenas estetica

  # Condições para renomear os sabores de sorvete
  if sabor == 'TR':
    sabor = 'tradicional'
  elif sabor == 'PR':
    sabor = 'premium'
  else:
    sabor = 'especial'

  total += preco # Soma todos os preços se tiver mais de pedido
  # Print ao finalizar um pedido
  print(f'Você pediu um sorvete {sabor} de {numb} bola(s). Valor total do pedido: R$ {preco:.2f}')

  # Saber se quer pedir mais
  print('') # print vazio para separar as frases/funçao apenas estetica
  continuar = str(input('Deseja pedir novamente? (S/Digite outra coisa)'))
  continuar = continuar.upper()
  if continuar == 'S': # Refaz o pedido se desejar continuar
    continue
  else:
    print('')
    print(f'Valor total a ser pago: R$ {total:.2f}') # Mostrar o valor mesmo em caso de nao responder com 'N'
    break






