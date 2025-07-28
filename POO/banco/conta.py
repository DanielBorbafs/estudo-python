class ContaBancaria():
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
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


class ContaPoupanca(ContaBancaria):
    def __init__(self, juros, saldo, titular):
        self.juros = juros
        super().__init__(titular, saldo)

    def calcula_juros(self, tempo):
        return self.saldo + (self.saldo * self.juros * tempo)


conta01 = ContaPoupanca(juros=0.1, saldo=1500, titular="Melissa")
conta01.mostrar_saldo()


rendimento = conta01.calcula_juros(6)
print(f'Saldo após 6 meses: R$ {rendimento:.2f}')
