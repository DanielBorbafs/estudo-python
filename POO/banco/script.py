from conta import ContaBancaria

minha_conta = ContaBancaria('Daniel', 0)
minha_conta.depositar(1500)
minha_conta.mostrar_saldo()

conta_secundaria = ContaBancaria('Melissa', 100)
conta_secundaria.depositar(1300)
conta_secundaria.mostrar_saldo()

minha_conta.transferir(150,conta_secundaria)
print(f'Saldo Melissa R$ {conta_secundaria.saldo}')