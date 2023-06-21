class Usuario:
    nombre_banco = "Banco de Chile"

    def __init__(self, nombre, correo, balance_cuenta1, balance_cuenta2):
        self.nombre = nombre
        self.correo = correo
        self.cuenta1 = CuentaBancaria(tasa_interés=0.02, balance=balance_cuenta1)
        self.cuenta2 = CuentaBancaria(tasa_interés=0.04, balance=balance_cuenta2)

    def hacer_retiro(self, monto, cuenta):
        if cuenta == 1:
            if monto <= self.cuenta1.balance:
                self.cuenta1.balance -= monto
                print(f"Se hizo un retiro de ${monto} en la cuenta 1. Nuevo balance: ${self.cuenta1.balance}")
            else:
                print("Saldo insuficiente para realizar la acción")
        elif cuenta == 2:
            if monto <= self.cuenta2.balance:
                self.cuenta2.balance -= monto
                print(f"Se hizo un retiro de ${monto} en la cuenta 2. Nuevo balance: ${self.cuenta2.balance}")
            else:
                print("Saldo insuficiente para realizar la acción")
        else:
            print("Cuenta inválida")
        return self

    def hacer_deposito(self, monto, cuenta):
        if cuenta == 1:
            if monto > 0:
                self.cuenta1.balance += monto
                print(f"Se hizo un depósito de ${monto} en la cuenta 1. Nuevo balance: ${self.cuenta1.balance}")
            else:
                print("El monto depositado debe ser mayor a $0")
        elif cuenta == 2:
            if monto > 0:
                self.cuenta2.balance += monto
                print(f"Se hizo un depósito de ${monto} en la cuenta 2. Nuevo balance: ${self.cuenta2.balance}")
            else:
                print("El monto depositado debe ser mayor a $0")
        else:
            print("Cuenta inválida")
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}")
        print(f"Su balance en la Cuenta 1 es de ${self.cuenta1.balance}")
        print(f"Su balance en la Cuenta 2 es de ${self.cuenta2.balance}")
        return self

class CuentaBancaria:
    def __init__(self, tasa_interés, balance):
        self.tasa_interés = tasa_interés
        self.balance = balance


# Instancia de clase 
persona1 = Usuario("Guido van Rossum", "guido@python.com", balance_cuenta1=1000, balance_cuenta2=2000)

# Llamadas a métodos
persona1.hacer_deposito(monto=100, cuenta=1).hacer_deposito(monto=200, cuenta=2).hacer_retiro(monto=300, cuenta=1).mostrar_balance_usuario()
