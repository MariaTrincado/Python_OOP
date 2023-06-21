class Usuario:
    nombre_banco = "Banco de Chile"

    def __init__(self, nombre, correo, balance=0):
        # Atributos de instancia
        self.nombre = nombre
        self.correo = correo
        self.balance = balance

    def hacer_retiro(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            print(f"Se realizó un retiro de ${monto}. Nuevo balance: ${self.balance}")
        else:
            print("Saldo insuficiente para hacer el retiro")
        return self


    def hacer_deposito(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se realizó un depósito de ${monto}. Nuevo balance: ${self.balance}")
        else:
            print("El monto depositado debe ser mayor a $0")
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, su balance es de ${self.balance}")
        return self
    
    def hacer_transferencia(self, otro_usuario, monto):
        if monto <= self.balance:
            self.balance -= monto
            otro_usuario.balance += monto
        else:
            print("Saldo insuficiente para realizar el depósito")
        return self


# Instancias de clase
persona1 = Usuario("Guido van Rossum", "guido@python.com", balance = 1000)
persona2 = Usuario("Monty Mekano", "monty@python.com", balance = 2000)
persona3 = Usuario("Cristina Tank", "cristina@python.com",  balance = 500)

# Llamadas a métodos
persona1.hacer_deposito(monto=100).hacer_deposito(monto=60).hacer_deposito(monto=40).hacer_retiro(monto=300).mostrar_balance_usuario()

persona2.hacer_deposito(monto=100).hacer_deposito(monto=80).hacer_retiro(monto=500).hacer_retiro(monto=130).mostrar_balance_usuario()

persona3.hacer_deposito(monto=100).hacer_retiro(monto=60).hacer_retiro(monto=140).hacer_retiro(monto=400).mostrar_balance_usuario()

persona1.hacer_transferencia(otro_usuario=persona3, monto=50).mostrar_balance_usuario()

persona3.mostrar_balance_usuario()
