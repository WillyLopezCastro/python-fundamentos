from core_cuenta_bancaria import CuentaBancaria

class Usuario:
    def __init__(self):
        self.cuenta = CuentaBancaria()

    def deposito(self, monto):
        self.cuenta.deposito(monto)
        return self

    def retiro(self, monto):
        self.cuenta.retiro(monto)
        return self

    def mostrar_info_cuenta(self):
        self.cuenta.mostrar_info_cuenta()
        return self

juan = Usuario()
juan.deposito(100).retiro(50)
print("Informacion Juan")
juan.cuenta.mostrar_info_cuenta()