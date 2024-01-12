lista_colaboradores = [] #lista vazia de colaboradores
id_global = 0 #variável inicial de id definida como 0

#--------------------------------------------------------
def cadastrar_colaborador(id): #função de cadastro de colaboradores
  print('*' * 75)
  print('------------------MENU CADASTRAR COLABORADOR---------------------')
  nome = input('Por favor entre com o nome: ') #inserção dos dados
  setor = input('Por favor entre com o setor: ')
  pagamento = input('Por favor entre com o  (R$): ')

  colaborador = { #dicionário para inserir os colaboradores
      'id': id_global,
      'nome': nome,
      'setor': setor,
      'pagamento': pagamento
      }
  lista_colaboradores.append(colaborador.copy()) #adicionando o dicionário na lista

#--------------------------------------------------------

#função de consulta de colaborador
def consultar_colaborador():
  print('*' * 75)
  while True:
    print('------------------MENU CONSULTAR COLABORADOR---------------------------')
    print('Escolha a opção desejada:\n1- Consultar Todos\n 2- Consultar por Id\n 3- Consultar por Setor \n 4- Retornar ao menu')
    consulta = input('>>') #variável para receber a resposta

  #condições para cada RESPOSTA recebica
    if consulta == '1': #varrer todos os conjuntos chave e valor do dicionário de colaboradores
      print('--------------------------')
      for colaboradores in lista_colaboradores: #for que mostra toda a lista/dicionário de colaboradores
        print('--------------------------')
        for key, value in colaboradores.items(): #for para mostrar todos os colaboradores com chave e valores
          print(f'{key}: {value}')
      print('--------------------------')
    elif consulta == '2': #consulta por id de colaborador
      print('--------------------------')
      valor_desejado = input('Digite o id do colaborador: ') #recebe o id
      for colaboradores in lista_colaboradores:
        if colaboradores['id'] == int(valor_desejado): #se o id do colaborador for igual ao id recebido do usuário, vai mostrar a informação
           print('--------------------------')
           for key, value in colaboradores.items(): #for para mostrar todos os colaboradores com chave e valores
            print(f'{key}: {value}')


    elif consulta == '3': #condição semelhante à anterior, mudando apenas a resposta recebida
      print('--------------------------')
      valor_desejado = input('Digite o setor do(s) colaborador(es): ') #no caso, se refere ao setor
      for colaboradores in lista_colaboradores:
        if colaboradores['setor'] == (valor_desejado):
           for key, value in colaboradores.items():
            print(f'{key}: {value}')
        print('--------------------------')
    elif consulta == '4':
      return #sai da função
    else:
      print('Opção inválida.')
      continue

#--------------------------------------------------------

#função de remoção de colaborador
def remover_colaborador():
  print('*' * 75)
  print('---------------MENU REMOVER COLABORADOR---------------------')
  valor_desejado = int(input('Digite o id do colaborador a ser removido: ')) #variável para receber o id a ser removido
  for colaboradores in lista_colaboradores: #basicamente a mesma coisa das funções anteriores
    print('--------------------------')
    if colaboradores['id'] == valor_desejado:
      lista_colaboradores.remove(colaboradores) #parte diferente: utiliza a função de remover
      print('Colaborador Removido.')
      print('--------------------------')

#--------------------------------------------------------

#PROGRAMA PRINCIPAL
  print('Bem-vindo(a) ao Controle de Colaboradores')
while True:
  print('*' * 75)
  print('--------------------------MENU PRINCIPAL-----------------------------------')
  print('Escolha a opção desejada:\n1- Cadastrar Colaborador\n2- Consultar Colaborador(es)\n3- Remover Colaborador\n4- Sair')
  menu = input('>>')

  #condições para redirecionar cada caso para as funções
  if menu == '1':
    id_global +=1
    cadastrar_colaborador(id_global)
  elif menu == '2':
    consultar_colaborador() #chama a função de consultar
  elif menu =='3':
    remover_colaborador() #chama a função de remover
  elif menu == '4':
    break #encerra o programa
  else:
    print('Opção inválida.')
    continue #volta para o início do laço