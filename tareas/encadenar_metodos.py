class Usuario:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.email = correo
        self.balance_cuenta = 0

    def hacer_deposito(self, monto): 
        self.balance_cuenta += monto
        return self

    def hacer_retiro(self, monto):
        self.balance_cuenta -= monto
        return self
    
    def mostrar_balance(self):
        print("Usuario: ", self.nombre, "Balance: ", self.balance_cuenta)
        return self

    def transferir_dinero(self, otro_usuario, monto):
        self.hacer_retiro(monto)
        otro_usuario.hacer_deposito(monto)
        return self


guido = Usuario("Guido Van Rossum", "guidoVR@gmail.com")
guido.hacer_deposito(100).hacer_deposito(100).hacer_deposito(100).hacer_retiro(150).mostrar_balance()

monty = Usuario("Monty Perez", "montyP@gmail.com")
monty.hacer_deposito(100).hacer_deposito(100).hacer_retiro(50).mostrar_balance()

juan = Usuario("Juan Alvarado", "juan@gmail.com")
juan.hacer_deposito(500).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance()

guido.transferir_dinero(juan, 50)
guido.mostrar_balance()
juan.mostrar_balance()