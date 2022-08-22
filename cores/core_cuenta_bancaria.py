class CuentaBancaria:
    nombre_banco = "Banco de Credito Nacional"
    def __init__(self, tasa_interes = 0.01, balance = 0):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, monto):
        self.balance = self.balance + monto
        return self
    
    def retiro(self, monto):
        if monto > self.balance:
            print("Fondos insuficientes: cobrando una tarifa de $5")
        else:
            self.balance -= monto
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance} \n Interes: {self.tasa_interes}")
        return self

    def generar_interes(self):
        nuevo_interes = self.balance * self.tasa_interes
        self.balance = self.balance + nuevo_interes
        return self

print("Informacion Cuenta 1")
cuenta1 = CuentaBancaria(0.01, 0)
cuenta1.deposito(100).deposito(100).deposito(100).retiro(400).generar_interes().mostrar_info_cuenta()
print("\n")

print("Informacion Cuenta2")
cuenta2 = CuentaBancaria(0.01, 0)
cuenta2.deposito(500).deposito(500).retiro(100).retiro(100).retiro(100).retiro(100).generar_interes().mostrar_info_cuenta()