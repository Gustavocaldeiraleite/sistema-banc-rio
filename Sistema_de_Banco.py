from datetime import datetime
import random
contas = []
clientes = []
pergunta = None
cliente_logado = None
class Cliente:
    def __init__(self, nome: str, endereco: object, cpf: int, numero_da_conta: object) -> object:
        self.nome =nome
        self.endereco =endereco
        self.cpf =cpf
        self.saldo = 0
        self.numero_saques = 0
        self.depositos = []
        self.saques = []
        self.agencia = '0001'
        self.numero_da_conta =  numero_da_conta

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print('deposito feito')
        else:
            print('deposito invalido')
    def sacar(self):
        if self.numero_saques < 3:
            valor = float(input('Digite o valor'))
            if valor < self.saldo and valor > 0:
                self.saldo -= valor
                self.numero_saques += 1
                self.saques.append(valor)
                print('saque feito')
            elif self.numero_saques == 3:
                print('Voce atingiu o limite de saque diario')
            elif valor < 0:
                print('Digite um valor positivo')
            elif self.saldo < valor:
                print('Saldo insulficiente')
            else:
                print('saque invalido')
        else:
            print('Voce atingiu o limite de saque diario')

    def extrato(self):
        data = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        print('='*20)
        print(f'''Nome: {self.nome}
Agencia: {self.agencia} Numero da conta: {self.numero_da_conta}
Saldo: {self.saldo}
Saques realizados:''')
        for c in self.saques:
            print(f'R${c}')
        print(f'Total: {self.numero_saques}')
        print('Depositos realizados:')
        for c in self.depositos:
            print(f'R${c}')
        print(f'Extrato realizado às: {data}')
        

    def conta_nova(self):
        print(f'sua agencia: {self.agencia} e numero de conta {self.numero_da_conta}')

def login():
    numero_da_conta = input('digite seu o numero da sua conta: ')
    for cliente in clientes:
        if cliente.numero_da_conta == numero_da_conta:
            return cliente
    print('Cliente nao encontrado. Tente novamente')
    return None

while True:
    if '1' == pergunta:
        cliente_logado = login()
        if cliente_logado is not None:
            print(f'''Acessando a conta de: {cliente_logado.nome}
Numero da conta: {cliente_logado.numero_da_conta}
Agencia: {cliente_logado.agencia} ''')
    elif '2' == pergunta:
        if cliente_logado is not None:   
            cliente_logado.sacar()
        else: 
            print('faca login primeiro')
    elif '3' == pergunta:
        if cliente_logado is not None:   
            deposito = float(input('Digite o valor'))
            cliente_logado.depositar(deposito)
        else:
            print('faca login primeiro')
    elif '4' == pergunta:
        if cliente_logado is not None:   
            cliente_logado.extrato()
        else:
            print('faca login primeiro')
    elif '5' == pergunta:
        print('=<>'*25)
        nome = input('digite seu nome')
        endereco = 'vazio'
        cpf = int(input('Cpf'))
        cpf = str(cpf)
        if len(cpf) != 11:
            print('cpf invalido')
            break
 
        numero_da_conta = random.randrange(10000, 100000)
        while numero_da_conta in contas:
            numero_da_conta = random.randrange(10000, 100000)
        contas.append(numero_da_conta)
        novo_cliente = Cliente(nome, endereco, cpf, numero_da_conta)
        clientes.append(novo_cliente)
        novo_cliente.conta_nova()
    elif '6' == pergunta:
        print('Obrigado por usar o sistema, tenho um bom dia')
        break
    elif '7' == pergunta:
        print('='*20)
        for c in clientes:
            print(f'''Nome: {c.nome} Agencia: {c.agencia} Numero da conta: {c.numero_da_conta}
Saldo: {c.saldo} CPF: {c.cpf} Endereco: {c.endereco}''')
            print('='*20)


    else:
        print('digite um valor valido')
    pergunta = input('''Ola, escolha a funcao que o agrada
 [1]Entrar em conta existente
 [2]Sacar
 [3]Depositar
 [4]Extrato
 [5]Nova conta
 [6]Sair
 [7]Listar contas
''')
    