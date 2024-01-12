def cachorro_peso(): #função que recebe o peso
  while True:
    try:
      pesoCachorro = int(input('Entre com o peso do cachorro: ')) # input recebe peso em kg
      if pesoCachorro > 0 and pesoCachorro < 3: #se o peso for menor que 3 e maior que 0
          base = 40
          return base
      elif pesoCachorro >= 3 and pesoCachorro < 10: #peso maior ou igual a 3 e menor que 10
          base = 50
          return base
      elif pesoCachorro >= 10 and pesoCachorro < 30: #peso maior ou igual a 10 e menor que 30
          base = 60
          return base
      elif pesoCachorro >= 30 and pesoCachorro < 50:  #eso maior ou igual a 30 e menor que 50
          base = 70
          return base
      else: #else para cachorros grandes
        print('Não aceitamos cachorros tão grandes.\n Por favor entre com o peso do cachorro novamente.')
    except ValueError: #tratamento de erros
      print('Você digitou um valor não numérico.\nPor favor entre com o peso do cachorro novamente.')




def cachorro_pelo(): #função que recebe o tipo de pelo do animal
  while True:
    print('Entre com o pelo do cachorro\n c - Pelo Curto\n m - Pelo Médio \n l - Pelo Longo')
    peloCachorro = input('>>') #input que recebe a entrada
    try:
      if peloCachorro == 'c' or peloCachorro == 'C': # pro caso do usuario digitar com letra maiuscula
        multiplicador = 1 #multiplicador especifico
        return multiplicador
      elif peloCachorro == 'm' or peloCachorro =='M':  # pro caso do usuario digitar com letra maiuscula
        multiplicador = 1.5  #multiplicador especifico
        return multiplicador
      elif peloCachorro == 'l' or peloCachorro =='L':  # pro caso do usuario digitar com letra maiuscula
        multiplicador = 2  #multiplicador especifico
        return multiplicador
      else:  # para qualquer entrada diferente das especificadas como opcionais
        print('Você digitou uma classificação inválida.\n Tente novamente')
    except ValueError: # para entradas diferentes de string
      print('Você digitou um valor inválido.\nPor favor entre com tipo de pelo do cachorro novamente.')

def cachorro_extra(): #função que recebe serviços adicionais
  extra = 0
  while True: # print abaixo que dá os opcionais
      extras = input('Deseja adicionar mais algum servico?\n' +
            '1 - Corte de Unhas - R$ 10,00\n' +
            '2 - Escovar Dentes - R$ 12,00\n' +
            '3 - Limpeza de Orelhas - R$ 15,00\n'+
            '0 - Não desejo mais nada\n' +
            '>>')
      if extras == '0':
        return extra #retorna tudo que foi somado
      elif extras == '1':
        extra += 10  #soma o valor do serviço extra
        continue # volta para o inicio do laço
      elif extras == '2':
        extra += 12 #soma o valor do serviço extra
        continue # volta para o inicio do laço
      elif extras == '3':
        extra += 15 #soma o valor do serviço extra
        continue # volta para o inicio do laço

print('Bem vindo(a) ao Petshop')
peso = cachorro_peso() #atribuindo a variavel peso à função
pelo = cachorro_pelo() #atribuindo a variavel pelo à função
extra = cachorro_extra() #atribuindo a variavel extra à função
total = peso * pelo + extra # calculo do total
print(f'O total ficou: R${total:.2f} (Peso: {peso} * pelo: {pelo} + extra(s): {extra})')

