class Cliente:
    def __init__(self,nombre,apellido,cedula,ciudad):
        
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.ciudad=ciudad
   
class Cuenta:
    def __init__(self,numerocuenta,saldo):
        self.numerocuenta=numerocuenta
        self.saldo=saldo

    def retirarSaldo(self,valor):
        self.saldo = self.saldo - valor
        print(f'el nuevo saldo es {self.saldo}')

    def agregarsaldo(self,valor):
        self.saldo = self.saldo + valor
        print(f'el nuevo saldo es {self.saldo}')

    def consultarSaldo(self):
        print(self.saldo)