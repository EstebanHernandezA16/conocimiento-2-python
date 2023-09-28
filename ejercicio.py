
#Calculadora
#tupla/lista/diccionario

continuar = True

operaciones = ("1.Suma","\n 2.Resta" "\n 3.Multiplicacion", "\n 4.Division"  ,"5.Ver historial")

historial = []

indice= 0

agregarRegistro = lambda registro: historial.append(registro)



def Sumar(n1,n2):
    global indice
    resultado = n1+n2
    indice+=1
    registro = {f"registro{indice}":{"operacion": "suma", "n1": n1, "n2": n2, "resultado": resultado}}
    agregarRegistro(registro)
    
    
def Restar(n1,n2):
    global indice
    resultado = n1-n2
    indice+=1
    registro = {f"registro{indice}":{"operacion": "resta", "n1": n1, "n2": n2, "resultado": resultado}}
    agregarRegistro(registro)
   
def Multiplicar(n1,n2):
    global indice
    resultado= n1*n2
    indice+=1
    registro = {f"registro{indice}":{"operacion": "multiplicacion", "n1": n1, "n2": n2, "resultado": resultado}}
    agregarRegistro(registro)
   
def Division(n1,n2):
    global indice
    resultado = n1/n2
    indice+=1
    registro = {f"registro{indice}":{"operacion": "division", "n1": n1, "n2": n2, "resultado": resultado}}
    agregarRegistro(registro)
    
def VerHistorial(valorABuscar):
    if valorABuscar == 0:
        print(historial)
    elif valorABuscar<len(historial):
        print(historial[valorABuscar])
    else:
        print(f"El registro {valorABuscar} no existe en la lista")    

 



while continuar==True:
    respuesta = input(f"Ingrese la operacion que quiere realizar: {operaciones}: ")
    if respuesta!='5':
        n1 = float(input('Ingresa el primer numero: '))
        n2 = float(input('Ingresar el segundo numero: '))
    if respuesta=='1':
        Sumar(n1,n2)
    if respuesta=='2':
        Restar(n1,n2)
    if respuesta=='3':
        Multiplicar(n1,n2)
    if respuesta=='4':
        Division(n1,n2)
    if respuesta=='5':
        if indice!=0:
            valorABuscar = int(input('Ingrese el numero del registro que quiere buscar (ingrese 0 para ver todos los registros): '))
            VerHistorial(valorABuscar)
            
        else:
            print('Ahora mismo no hay ningún dato en el historial')


    reinciarCiclo= input('¿Desea realizar otra operacion? S/N ')
    if reinciarCiclo.lower()=="s":
        respuesta=True
    else:
        respuesta=False    


print("Cerrando el programa")