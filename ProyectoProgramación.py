#Autores: Eduardo Salazar Vindas, Andres Fabricio Araya Hernandez, Sharon Avila, Joseph Alvarado, Grupo 6 - 2do Avance de Proyecto, Segunda Entrega 23/03/2023
from datetime import datetime #Importa la librería datetime

tareas_Registros = [] #Arreglo a utilizar para almacenar los registros de las tareas

def carga_Registros(): #Funcion para cargar los registros en archivo plano (txt) y ponerlas en un array bidimensional
    try:
        with open('Datos_Guardado.txt','r') as file: # Abre y cierra automáticamente el archivo tomandolo como nombre file (variable)
            registros = file.readlines() #Guarda los datos del txt en arreglo (unidimensional sin formato)

            for registro in registros: #Se refiere a cada dato que haya en el arreglo
                campos = registro.strip().split(',') #Formatea cada registro o tarea, para eliminar los \n y separar los campos en array provisional
                campos[0],campos[1],campos[2],campos[3],campos[4] = campos[0].strip(), campos[1].strip(), campos[2].strip(), float(campos[3].strip()), campos[4].strip() #Da los formatos finales a cada campo del array provisional (**Nota: El campo[3] = costo, pasa a ser float), eliminando espacios en blanco
                
                tareas_Registros.append(campos) #Agrega cada registro formateado al array central
    except:
        return
        
def agregar_Tarea():
    try: #Manejo de errores
        fecha_Nuevo = input('\nDigite la fecha (dd/mm/aaaa): ') #Ingresa la fecha nueva en el formato establecido    
        formato_Fecha = datetime.strptime(fecha_Nuevo, '%d/%m/%Y') #Se especifica el formato de fecha
        titulo_Nuevo = input('\nDígite un título: ') #Se ingresa el titulo elegido
        
        if titulo_Nuevo != "":
            descripcion_Nuevo = input('\nDigite una descripción: ') #Solicita una descripcion para la tarea
            if descripcion_Nuevo != "":

                try:
                    costo_Nuevo = float(input('\nDigite un costo: $')) #Se ingresa un costo de la tarea
                    estado_Nuevo = 'Pendiente'

                    tareas_Registros.append([fecha_Nuevo, titulo_Nuevo, descripcion_Nuevo, costo_Nuevo, estado_Nuevo]) #Guarda cada tarea que el usuario desee agregar
                    print(f'\nSe a creado un nuevo registro con título: {titulo_Nuevo}') #Se imprime el titulo 

                except:
                    print('\nError: Debe ingresar un costo válido, no se admiten letras') #Valida que el costo sea valido (formato decimal)
            else:
                print("\nError: La descripción no puede ser un espacio vacio") #Valida espacios en blanco
            
        else:
            print("\nError: El titulo no puede ser un espacio vacio") #Valida espacios en blanco

    except:
        print('\nError: Debe ingresar una fecha en el formato indicado. dd/mm/aaaa') #Valida que el formato de fecha sea el indicado (formato datetime)

def mostrar_Tareas(tareas):
    if (len(tareas) == 0):  #Valida que existan tareas para mostrar
        print('\nError: No hay registros para mostrar')  #Imprime que no hay registros

    else:
        print(f'\n{'Daily Planner - Actividades':^110}') #Imprime el titulo
        print(f'{'-'*110:^110}') #Centra el titulo

        for actividad in tareas: #Inicia el bucle 
            print(f'ID: {tareas.index(actividad) + 1}, Fecha: {actividad[0]}, Titulo: {actividad[1]}, Descripcion: {actividad[2]}, Costo: ${actividad[3]}, Estado: {actividad[4]}') #Muestra todas las tareas que el usuario haya registrado

def editar_Tarea(index, tareas): #Proceso para editar tareas ya ingresada

        tarea_Editar = tareas[index] #Tareas existentes

        while True: #Con este while, entramos al menu de edicion de tareas
            print(f'\nID: {tareas.index(tareas[index]) + 1}, Fecha: {tarea_Editar[0]}, Titulo: {tarea_Editar[1]}, Descripcion: {tarea_Editar[2]}, Costo: ${tarea_Editar[3]}, Estado: {tarea_Editar[4]}') #Este print nos muestra las tareas ingresadas

            opcion_Editar = str(input("\n---------- Menu Editar Tarea ---------\n\nA) Fecha\nB) Titulo\nC) Descripcion\nD) Costo\nE) Salir\n\nSeleccione una opcion (A-E): ")).lower() #Menu de seleccion para editar tareas

            sub_Indice = 0 #Posición a editar, por default será 0 (fecha)
                
            if opcion_Editar == "a": #Entra a la opcion editar fecha
                try:
                    fecha_edicion = input('\nDigite la fecha a editar (dd/mm/aaaa): ') #Opcion para selecionar la fecha a editar
                    formato_fecha_Edicion = datetime.strptime(fecha_edicion, '%d/%m/%Y') #Opcion para seleccionar el formato
                    tarea_Editar[sub_Indice] = fecha_edicion #Toma la posicion de la fecha ingresada
                    print("\nLa fecha fue correctamente editada.") #Imprime ejecucion fue editada
                    
                except: #Si el usuario ingresa un formato de fecha incorrecto, muestra el siguiente error
                    print("\nError: Opcion incorrecta, favor seleccionar fecha en formato correcto (dd/mm/aaaa).") 


            elif opcion_Editar == "b": #Entra a la opcion editar el titulo
                sub_Indice = 1 #Posición a editar (titulo)
                
                titulo_Edicion = input("\nDigite el titulo a editar: ") #opcion para seleccionar el titulo a editar
                tarea_Editar[sub_Indice] = titulo_Edicion #Toma la posicion del titulo ingresado
                print("\nEl titulo fue correctamente editado.") #Muestra en pantalla que al edicion se ejecuto correctamente
                
                

            elif opcion_Editar == "c": #Opcion para editar la descripcion 
                sub_Indice = 2  #Posición a editar (descripcion)
                descripcion_edicion = input("\nDigite el titulo a editar: ") 
                tarea_Editar[sub_Indice] = descripcion_edicion
                print("\nLa descripcion fue correctamente editada.") #Muestra en pantalla que al edicion se ejecuto correctamente

            elif opcion_Editar == "d": #Opcion para editar el costo
                sub_Indice = 3 #Posición a editar costo)
                try:
                    costo_edicion = float(input("\nDigite el costo a editar: $"))  #Solicita el costo a editar
                    tarea_Editar[sub_Indice] = costo_edicion 
                    print("\nEl costo fue editado correctamente")  #Indica que se edito el texto

                except:
                    print("\nError: El costo debe ser un numero, no se aceptan letras")  #Valida que el valor sea un numero     

            elif opcion_Editar == "e": #Opciom para salir del menu de edicion
                print("\nSalir de Edicion")
                break #Rompe el ciclo para salir del menu

            else:#En caso de opción Incorrecta
                print("\nOpción Incorrecta, intente de nuevo. \nIngrese una opción de la A a la E.")
                
            #Salida Ciclo While 

def eliminar_tarea(tareas): #funcion de eliminar tareas
    if(len(tareas)) == 0: # valida que existan tareas
        print("\nError: No hay tareas para eliminar")
    
    else:
        try:
            index = int(input('Seleccione el ID del Registro a Eliminar: ')) - 1 #Solicita al usuario el numero de ID de la tarea a eliminar
            if 0 <= index < len(tareas):
                print(f'\nSe ha eliminado la tarea con título: {tareas[index][1]}')  #Indica cual tarea fue eliminada
                del tareas[index] #Elimina la tarea seleccionada
            else:
                print('\nError: La tarea seleccionada no existe')

        except:
            print('\nError: Opcion incorrecta, debe de usar el numero de ID')  #Error por numero de ID incorrecto
        
    
def marcar_tarea(tareas):
    if(len(tareas)) == 0:  #Valida que existan tareas para marcar
        print("\nError: No hay tareas para marcar")
        
    else:
        try:
            elegir_tarea = int(input("\nDigite cual tarea desea marcar: ")) - 1 #Solicita al usuario la tarea que desea marcar

            tarea_marcar = tareas[elegir_tarea]  #Selecciona la tarea
            
            tarea_marcar[4] = 'Completa' #Marca la tarea completa

            print(f"\nLa tarea con título {tarea_marcar[1]} se marcó como Completa")  #Imprime que la tarea fue marcada correctamente

        except:
            print("\nError: Se debe ingresar el numero de tarea, no se aceptan letras") #Error por ingresar letras como valor
            
def convertir_a_fecha(fecha_str): #Convierte una string a formato Fecha, eso se usa en el ordenamiento de actividades por fecha
    return datetime.strptime(fecha_str, '%d/%m/%Y')

def estadisticas_Simples(tareas):
    #Variables para contadores
    num_tareas = 0 #Inicializa el valor total de tareas tanto pendientes como completas
    tareas_pendientes = 0 #Inicializa el valor de las tareas pendientes
    tareas_completadas = 0 #Inicializa el valor de las tareas completas

    #Varibles para costos
    costo_Total  = 0 #Inicializa el costo total de las categorías de tareas
    costo_tareas_completadas = 0 #Inicializa el costo de las tareas completas
    costo_tareas_pendientes = 0 #Inicializa el costo de las tareas pendientes 

    if len(tareas) == 0:
         print("\nError: No hay tareas para mostrar estádisticas") #Valida que existan tareas para mostrar
         
    else:
        num_tareas = len(tareas) #Verifica el numero de tareas
        
        for tarea in tareas:  #Ciclo segun el numero de tareas

            costo_Total += tarea[3] #Suma el costo de todas las tareas
            
            if tarea[4] == "Pendiente":
                tareas_pendientes +=1  #Suma las tareas pendientes
                costo_tareas_pendientes += tarea[3]  #Suma el costo de las tareas pendientes
            else:
                tareas_completadas +=1  #Suma las tareas completadas
                costo_tareas_completadas += tarea[3]  #Suma el cossto de las tareas completadas
        
        print(f'\n---------- Estadísticas Simples ----------\n') #Titulo de estadisticas
        print(f'Cantidad de Tareas = {num_tareas}\nCantidad de Tareas Pendientes = {tareas_pendientes}\nCantidad de Tareas Completas = {tareas_completadas}\n') #Imprime la cantidad de tareas pendientes y completadas
        print(f'Costo Total = ${costo_Total}\nCosto de Tareas Pendientes = ${costo_tareas_pendientes}\nCosto de Tareas Completas = ${costo_tareas_completadas}') #Imprime el costo de las tareas pendientes y completadas

        print(f'\n{'Daily Planner - Actividades Ordenadas':^110}') #Imprime el titulo
        print(f'{'-'*110:^110}') #Centra el titulo

        tareas_Ordenadas = sorted(tareas, key=lambda x: convertir_a_fecha(x[0])) #Nueva lista ordenada, creando función anónima, para convertir el valor en pos(0) a fecha y ordenarlo correctamente
        
        for actividad in tareas_Ordenadas: #Imprime la lista de actividades ordenadas
            print(f'ID: {tareas.index(actividad) + 1}, Fecha: {actividad[0]}, Titulo: {actividad[1]}, Descripcion: {actividad[2]}, Costo: ${actividad[3]}, Estado: {actividad[4]}') #Muestra todas las tareas que el usuario haya registrado

def guardar_Datos(tareas): #Guardar los nuevos ingresos de datos y los existentes 

    with open('Datos_Guardado.txt', 'w') as file: #Abre el documento en formato txt, con w sobre-escribe el documento
            
        for registro in tareas: #Ciclo for para ingresar al registro 
                
            regitro_Formato = ", ".join(str(campo) for campo in registro) #Formaro con coma espacion por cada linea
            file.write(regitro_Formato + "\n") #Formato para rescribir en el documento y con \n pasa de linea a cada actividad

def main():
    carga_Registros()
    print("¡Bienvenido!")#Saludo Inicial al Usuario

    while True: #Repite Indefinidamente el Menu Principal
    
        opcion = str(input("\n\n---------- Menu Principal ----------\n\nA) Ver Tareas\nB) Administrar Tareas\nC) Estadísticas\nD) Salir\n\nSeleccione una opción: ")).lower() #Opción para el Menu Principal

        if opcion == "a": #Opción de ver las tareas
            mostrar_Tareas(tareas_Registros)

        elif opcion == "b": #Opción de Administrar tareas

            while True: #Se repite indefinidamente el segundo menu (Menu administrativo)
                opcion_Menu2 = str(input("\n\n---------- Menu Administrativo ----------\n\nA) Agregar Tareas\nB) Editar Tareas\nC) Eliminar Tareas\nD) Marcar Tarea Completa\nE) Salir\n\nSeleccione una opción: ")).lower()
                
                if opcion_Menu2 == "a":  #opcion de agregar tareas
                    agregar_Tarea()

                elif opcion_Menu2 == "b": #opcion de editar tareas 
                    if(len(tareas_Registros)) == 0:

                        print("\nError: No hay tareas para editar")

                    else:
                        try:
                            indice = int(input("\nSeleccione el ID de la tarea que desea editar: ")) - 1  #Solicita al usuario el ID de la tarea a editar
                            if 0 <= indice < len(tareas_Registros): #Valida que la tarea seleccionada exista
                                editar_Tarea(indice,  tareas_Registros)
                            else:
                                print('\nError: La tarea seleccionada no existe')
                            
                        except:
                            print("\nError: Opcion incorrecta, debe de usar el numero de ID")  #Valida que el numero de ID sea correcto

                elif opcion_Menu2 == "c":  #opcion de eliminar tareas
                    eliminar_tarea(tareas_Registros)

                elif opcion_Menu2 == "d": #opcion de marcar tareas
                    marcar_tarea(tareas_Registros)
                    

                elif opcion_Menu2 == "e": #opcion de salir del menu administrativo
                    print("\nSalir del menu administrativo")
                    break

                else:#En caso de opción Incorrecta
                    print("\nError: Opción Incorrecta, intente de nuevo. \nIngrese una opción de la A a la E.")
                
            #Salida Ciclo While 2 (Menu Administrativo)
            
        elif  opcion == "c": #Opción Estadisticas Simple
            
            estadisticas_Simples(tareas_Registros) #Manda a llamar la función y como parámetro usa el arreglo bidimensional con los registros

        elif opcion == "d": #Opción Salir
            guardar_Datos(tareas_Registros)
            print("\n¡Hasta Luego!") #Se da la despedida al usuario al dar a la opción salir
            break
        
        else: #En caso de opción Incorrecta
            print("\nError: Opción incorrecta, intente de nuevo. \nIngrese una opción de la A a la D.") 

    #Salida del ciclo While Menu Principal

main()