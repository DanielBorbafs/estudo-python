import unittest
from conta import ContaBancaria

class TestContaBancaria(unittest.TestCase):

    def test_deposito_valido(self):
        conta = ContaBancaria("Daniel", 100)
        resultado = conta.depositar(50)
        self.assertTrue(resultado)
        self.assertEqual(conta.saldo, 150)

    def test_deposito_negativo(self):
        conta = ContaBancaria("Daniel", 100)
        resultado = conta.depositar(-10)
        self.assertFalse(resultado)
        self.assertEqual(conta.saldo, 100)

    def test_deposito_invalido_string(self):
        conta = ContaBancaria("Daniel", 100)
        resultado = conta.depositar("abc")
        self.assertFalse(resultado)
        self.assertEqual(conta.saldo, 100)

    def test_deposito_com_string_numero(self):
        conta = ContaBancaria("Daniel", 100)
        resultado = conta.depositar("50.75")
        self.assertTrue(resultado)
        self.assertAlmostEqual(conta.saldo, 150.75)




class TestTransferencia(unittest.TestCase):
    def test_transferencia_valida(self):
        conta_origem = ContaBancaria("Daniel", 500)
        conta_destino = ContaBancaria("Lucas", 100)
        resultado = conta_origem.transferir(200, conta_destino)
        self.assertTrue(resultado)
        self.assertEqual(conta_origem.saldo, 300)
        self.assertEqual(conta_destino.saldo, 300)




if __name__ == '__main__':
    unittest.main()