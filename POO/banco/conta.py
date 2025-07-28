class ContaBancaria():
    def __init__(self, titular, saldo=0):
        """Inicia com um titular em branco e um saldo zerado"""
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """Tenta adicionar valor ao saldo e trata erros de entrada inválida"""
        try:
            valor = float(valor)
            if valor > 0:
                self.saldo += valor
                print(f'Deposito de R$ {valor:.2f} realizado com sucesso!')
                return True
            else:
                print('Valor invalido: deve ser maior que zero.')
                return False
        except ValueError:
            print('Erro: o valor informado não é um numero válido.')
            return False
        except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')
            return False

    def transferir(self, valor, conta_destino):
        try:
            valor = float(valor)
            if valor <= 0:
                print('Valor inválido para transferencia')
                return False
            if valor > self.saldo:
                print('Saldo insuficiente para transferencia')
                return False
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f'Transferencia de R$ {valor:.2f} realizada para {conta_destino.titular}')
            return True
        except Exception as e:
            print(f'Erro na transferencia: {e}')
            return False

    def mostrar_saldo(self):
        print(f'Saldo atual de {self.titular}: R$ {self.saldo:.2f}')

