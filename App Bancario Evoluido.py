import textwrap
def menu():
    menu = """\n
----------- MENU ----------
[1] \tDeposito
[2] \tSacar 
[3] \tExtrato 
[4] \tNova conta 
[5] \tNovo usuário 
[6] \tLista de contas
[7] \tAcessar Conta 
[0] \tSair 
=> """
    return input(textwrap.dedent(menu))

def acessar_conta(contas):
    agencia = input('Informe a agência:')
    numero_conta = input('Informe o número da conta:')
    
    for conta in contas:
        if conta['agencia'] == agencia and conta['numero_conta'] == numero_conta:
            return conta

    print('Conta não encontrada.')
    return None

def depositar(saldo, valor, extrato, /):
 if valor > 0:
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print('\n Depósito realizado com sucesso!!')
 else:
    print('\n Operação Falhou!! Valor informado é inválido.')

 return saldo, extrato       

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
   excedeu_saldo = valor > saldo
   excedeu_limite = valor > limite
   excedeu_saques = numero_saques >= limite_saques

   if excedeu_saldo:
      print('Operação falhou! Você não tem saldo suficiente.')

   elif excedeu_limite:
      print('Operação falhou" O valor do saque excede o limite.')

   elif excedeu_saques:
      print('Operação falhou" Número máximo de saques excedido.')

   elif valor > 0:
      saldo -= valor
      extrato += f'Saque:\tR$ {valor:.2f}\n'
      numero_saques += 1
      print('\n Saque realizado com sucesso!')
   else:
      print('Operação falhou" O Valor informado é inválido.')
   return saldo, extrato      
                  
def exibir_extrato(saldo, /, *, extrato):
   print('\n---------- EXTRATO ----------')
   print(' Não foram realizadas movimentações.'if not extrato else extrato )
   print(f'\nSaldo:\t\tR$ {saldo:.2f}')
   print('----------------------------')

def criar_usuario(usuarios):
   cpf = input('Informe o CPF (somente números):')
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print(' Já existe um usuário com esse CPF!')
      return usuarios
   
   nome = input('Informe seu nome completo:')
   data_nascimento = input('Informe a data de nascimento (data-mês-ano):')
   endereco = input('Informe o endereço (logradouro, nro - bairro - cidade\sigla estado):')
   
   usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
   print('Usuário criado com sucesso!')
   return usuarios

def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']== cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

def criar_conta(agencia, numero_conta, usuarios, contas):
   cpf = input('informe o CPF do usuário:')
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      nova_conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario,}
      contas.append(nova_conta)
      print('\n Conta criada com sucesso!')
      return nova_conta
      #return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario,}
   else:
      print(' Usuário não encontrado, fluxo de criação de conta encerrado!')
      return None

def listar_contas(contas):
   print("=" * 100)
   for conta in contas:
      linha = f'''\
        Agência:\t{conta['agencia']}
        C\C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    '''
      print(textwrap.dedent(linha))
   print("=" * 100)

def main():
   LIMITE_SAQUES = 3
   AGENCIA = '0001'

   saldo = 0
   limite = 1000
   extrato = ""
   numero_saques = 0
   usuarios = []
   contas = []

   while True:
      opcao = menu()
      if opcao == '1':
         valor = float(input('Informe o valor do depósito:'))
         saldo, extrato = depositar(saldo, valor, extrato)
      
      elif opcao == '2':
         valor = float(input('Informe o valor do saque:'))
         saldo, extrato = sacar (
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,   
         )
      elif opcao == '3':
         exibir_extrato(saldo, extrato=extrato)
      elif opcao == '4':
         criar_usuario(usuarios)
      elif opcao == '5':
         numero_conta = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta,usuarios, contas)

         if conta:
            contas.append(conta)            
      
      elif opcao == '6':
         listar_contas(contas)


      elif opcao == '7':
         conta = acessar_conta(contas)
         if conta:
            print(f"Bem-vindo(a) {conta['usuario']['nome']}!")
      
      elif opcao == '0':
         break
      else:
         print('Operação inválida, por favor selecione novamente a operação desejada')

main()     