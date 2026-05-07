
class Cliente:

    def __init__(self,nome, cpf):
        self.nome = nome
        self.cpf = cpf
          
    

class Conta(Cliente):
    def __init__(self, saldo):
        self.__saldo = saldo
        self.__saldo = 0


    def get_saldo(self):
        return self.__saldo
    
    
    def depositar(self, valor):

        try:
            if valor > 0:
                self.__saldo += valor
            
            else:
                print("ERRO: valor invalido!")
        except ValueError:
            print("ERRO: digite um número inteiro valido!")
    

    def sacar(self, saque):    
        try:
            if saque <= self.__saldo and saque > 0 :
                self.__saldo -= saque
            
            else:
                print("ERRO: valor invalido!")
        except ValueError:
            print("ERRO: digite um número inteiro valido!")
        
    def transferir(self, valor, conta_destino):
        if self.__saldo > 0:
            self.__saldo -= self.depositar()
            

class ContaCorrente(Conta):
    
    def __init__(self, saldo):
        super().__init__(saldo)


    def sacar(self, saque):
        self.saque = saque
        self.saque += 1

class ContaPoupanca(Conta):
    def render_juros(self):
        self.__saldo = self.__saldo * 1.01
    

        