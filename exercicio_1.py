print("Bem vindo(a) à Loja Genérica")
print("_" * 60)
valor_unid = float(input('Entre com o valor da unidade do produto: ')) # Valor unitário do produto
qtd = int(input('Entre com a quantidade de protudos para a compra: '))  # Quantidade de produto
total = valor_unid * qtd

# Aplicando (ou não) desconto
if (qtd >= 2000):
  total_desc = total * 0.85   # Aplicando o desconto de 15%
  print('Desconto de 15% aplicado! O valor da compra passou de R$ {:.2f} para R${:.2f} com o desconto.' .format(total, total_desc)) # Comparando os dois valores, com e sem desconto, na mesma sentença
elif (qtd >= 1000) and (qtd < 2000):
  total_desc = total * 0.90   # Aplicando desconto de 10%
  print('Desconto de 10% aplicado! O valor da compra passou de R$ {:.2f} para R${:.2f} com o desconto.' .format(total, total_desc))
elif (qtd >= 200) and (qtd < 1000):
  total_desc = total * 0.95   # Aplicando desconto de 5%
  print('Desconto de 5% aplicado! O valor da compra passou de R$ {:.2f} (sem desconto) para R${:.2f} com o desconto.' .format(total, total_desc)) # :.2f para limitar a quantidade de números p/ dois pós vírgula
else:
  print('Sua compra ficou no valor de R$ {:.2f}' .format(total)) # Mensagem sem desconto