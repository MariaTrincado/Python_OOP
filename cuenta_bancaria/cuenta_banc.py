class CuentaBancaria:
    # atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []

    def __init__(self, tasa_int=0.01 ,balance=0):
        #atributos de instancia
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    
    def hacer_deposito(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se realizó un depósito de ${monto}. Nuevo balance: ${self.balance}")
        else:
            print("El monto depositado debe ser mayor a $0")
        return self

    
    def hacer_retiro(self, monto):   #restarle -$5 como tarifa por retiro
        if monto <= self.balance:
            self.balance -= monto
            self.balance -= 5
            print(f"Se realizó un retiro de ${monto}. Nuevo balance: ${self.balance}")
        else:
            print("Saldo insuficiente para hacer el retiro")
        return self

    def mostrar_info_cuenta(self):
        print(f"Su balance es de ${self.balance}")
        return self

#aumenta el balance de la cuenta por el balance actual * la tasa de interés (siempre que el balance sea positivo) 
    def generar_interes(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_int
            self.balance += interes_generado
            print(f"Se generó un interés de ${interes_generado} en la cuenta con balance ${self.balance}")
            return self

#BONUS NINJA: utiliza un método de clase para imprimir todas las instancias de la información de una cuenta bancaria
    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            cuenta.mostrar_info_cuenta()

# Instancias de clase (crea cuentas)
cuenta1 = CuentaBancaria(balance = 1000)
cuenta2 = CuentaBancaria(balance = 2000)

# Llamadas a métodos
cuenta1.hacer_deposito(monto=100).hacer_deposito(monto=60).hacer_deposito(monto=40).hacer_retiro(monto=300).mostrar_info_cuenta() #895
cuenta2.hacer_deposito(monto=500).hacer_deposito(monto=75).hacer_retiro(monto=500).hacer_retiro(monto=130).hacer_retiro(monto=100).hacer_retiro(monto=180).mostrar_info_cuenta() #1645

