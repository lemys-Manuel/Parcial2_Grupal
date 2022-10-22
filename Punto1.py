
def compararTiempo(listaCiclsitas):
        TiempoMeneor=100
        for ciclistas in listaCiclsitas:

            print(TiempoMeneor)
            if ciclista['Tiempo']<TiempoMeneor:

              TiempoMeneor=ciclistas['Tiempo']
              print(TiempoMeneor)
        print(f'el tiempo menor fue: {TiempoMeneor}')  

print("***Menu***")
print("1. Agregar ciclista")
print("2. Ver Tiempo")


opcion=1

ciclistas=[]

while(opcion!=0):
     ciclista={}
     opcion = int(input("Digite una opcion: "))
     if(opcion == 1):
            ciclista ['Nombre'] = input("Digite el Nombre: ")
            ciclista ['Edad']=int(input("Digite la edad: "))
            ciclista ['Pais']= input("Digite el pais: ")
            ciclista ['Equipo']= input("Digite el equipo: ")
            ciclista ['Tiempo']=int(input("Digite Tiempo: ")) 
            ciclistas.append(ciclista)  

            compararTiempo(ciclistas) 
# ciclista()         
     





    
    

                     
          
        
        
         

        
                    
           
            
   
       





    
