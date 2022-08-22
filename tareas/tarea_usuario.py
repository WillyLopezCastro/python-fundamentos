class Usuario:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.email = correo
        self.balance_cuenta = 0

    def hacer_deposito(self, monto): 
        self.balance_cuenta += monto

    def hacer_retiro(self, monto):
        self.balance_cuenta -= monto
    
    def mostrar_balance(self):
        print("Usuario: ", self.nombre, "Balance: ", self.balance_cuenta)

    def transferir_dinero(self, otro_usuario, monto):
        self.hacer_retiro(monto)
        otro_usuario.hacer_deposito(monto)


guido = Usuario("Guido Van Rossum", "guidoVR@gmail.com")
guido.hacer_deposito(100)
guido.hacer_deposito(100)
guido.hacer_deposito(100)
guido.hacer_retiro(150)
guido.mostrar_balance()

monty = Usuario("Monty Perez", "montyP@gmail.com")
monty.hacer_deposito(100)
monty.hacer_deposito(100)
monty.hacer_retiro(50)
monty.mostrar_balance()

juan = Usuario("Juan Alvarado", "juan@gmail.com")
juan.hacer_deposito(500)
juan.hacer_retiro(100)
juan.hacer_retiro(100)
juan.hacer_retiro(100)
juan.mostrar_balance()


guido.transferir_dinero(juan, 50)

guido.mostrar_balance()
juan.mostrar_balance()