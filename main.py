from punto3 import Cliente
from punto3 import Cuenta

banco=Cliente('nombre','apellido','cedula','ciudad')
banco.nombre="luis"
banco.apellido="suarez"
banco.cedula=1035452897
banco.ciudad="santa marta"

print(banco.nombre)
print(banco.apellido)
print(banco.cedula)
print(banco.ciudad)

cuenta=Cuenta(123456789,0)


print('1.para consultar saldo de cuenta')
print('2.para  agregar  dinero')
print('3.para  retirar  dinero')
print('0. fin')

deseo=int(input('Digite una de las opciones del Menu:'))


if(deseo==1):
    cuenta.consultarSaldo()    

elif(deseo==2):
    valor=int(input("cuanto agregamos: "))
    cuenta.agregarsaldo(valor)

elif(deseo==3):
     valor=int(input("cuanto retiramos: "))
     cuenta.retirarSaldo(valor)

else:
    print("digite una opcion valida")
          



 

        
    
    
    
