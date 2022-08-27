
"""
Programa para restaurantes

"""

def main ():
    
    print ("Bienvenidos")
    
    print ("Menú")
 #Colocar platillos y precios
  
    print ("Desplegar menú")
    print ("1. Comida $300")
    print ("2. Comida $200")
    print ("3. Comida $100")
    
    cuentaTotal=0
    
    x=str(input("¿Desea agregar un platillo? (si/no): "))
    
    while x=="si":
        num=int(input("Introduce un número de la comida: "))
        if num==1:
            cuentaTotal=cuentaTotal+300
        elif num==2:
            cuentaTotal=cuentaTotal+200
        elif num==3:
            cuentaTotal=cuentaTotal+100
            
        x=str(input("¿Desea agregar un platillo? (si/no): "))
    
    print ("Su cuenta total es de: $", cuentaTotal)
      
    
    

main()