menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 600
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []
valor = 0
while True:
  
 opcao = (input(menu))
 if opcao == 'd': 
     valor = int(input('Informe o valor do depósito:'))
     if valor >= 0: 
         saldo += valor 
         extrato += f'Depósito R$ {valor:.2f}\n' 
     
 elif opcao == 's':
     valor = float(input('Informe o valor do saque:'))
     erro_saldo = valor > saldo 
     erro_limite = valor > limite 
     erro_saques = numero_saques >= LIMITE_SAQUES 
     
     if erro_saldo: 
         print('Você não tem saldo suficiente.')
     if erro_limite: 
         print('O valor escolhido excede o limite disponivel')
     if erro_saques: 
         print('Limite de saques diarios alcançado.')
     
     if not erro_saldo and not erro_limite and not erro_saques:
         saldo -= valor
         extrato += f'saque: R$ {valor:.2f}\n'
         numero_saques += 1

 elif opcao == 'e': 
     print ('==========EXTRATO===========')
     print (f'\n Saldo: R$ {saldo:.2f}')
     print ('=========================')

 elif opcao == 'q': 
     break
     
 else: 
     print('Operação inválida, por favor selecione novamente a operação desejada.')
