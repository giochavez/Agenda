#   Hacer un programa que mantenga una agenda.
#   Contactos: Nombre, Teléfono, Correo, Número de cuenta.
#   Los datos se guardarán en un archivo.
#   Y se recuperarán de ahí al inciar el programa.
#   Será posible buscar por nombre o por número de cuenta
#   También se deberá buscar por todos los teléfonos que (...)
#   (...) comiencen en un número en específico. 
#   Al terminar los datos se volverán a guardar en el archivo 
#   "agenda.txt"
#   Si el archivo no existe, se creará.
#   Agregar, borrar o buscar un contacto.

def menu(opciones):
    while True:
        k = 1
        for op in opciones:
            print(f'({k}) {op}') #format
            k+=1
        try:
            print('Introduzca 0 para terminar el programa')
            op = input("Opción: ")
            op = int(op)
            print('')
        except ValueError:
            print('Entrada con formato inválido!! :o')
            continue
        if op>=0 and op<=len(opciones):
            return op
        print('Número fuera de rango')
    return

def cargar_agenda(nombre):
    agenda = dict()
    try:
        archivo = open('agenda.txt', 'rt')
        for linea in archivo:
            linea = linea[:-1] #descartamos el último caracter de la line (salto de linea)
            datos = linea.split('|')
            nombre, telefono, correo, cta = datos
            telefono = int(telefono)
            cta = int(cta)
            agenda[nombre] = [telefono, correo, cta]
        archivo.close()
    except FileNotFoundError:
        print("Agenda vacía.... :(")
    return agenda

def agregar_contacto(agenda):
    print("\tAgregar contacto:\n")
    nombre = input('Nombre: ')
    if nombre in agenda:
        print(f"{nombre} ya existe en la agenda")
        print(f"\tTeléfono: {agenda[nombre][0]}")
        print(f"\tCorreo: {agenda[nombre][1]}")
        print(f"\tNúmero de cuenta: {agenda[nombre][2]}")
        
    telefono = int(input('Teléfono: '))
    correo = input('Correo: ')
    cta = int(input('Número de cuenta: '))
    agenda[nombre] = [telefono, correo, cta]    #.append({'Nombre' : n, 'Teléfono': t, 'Correo': c, 
            #'Número de Cuenta' : nc})
    #print(n, " ha sido agregado correctamente.")
    return agenda

def salvar_agenda(nombre, ag):
    with open(nombre, "wt") as archivo:
        for n in ag:
            archivo.write(f'{n}|{ag[n][0]}|{ag[n][1]}|{ag[n][2]}\n')
    return

def buscar_4_name(agenda):    
        nombre = input("Ingresa el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"\n\tNombre: {nombre}")
            print(f"\tTeléfono: {agenda[nombre][0]}")
            print(f"\tCorreo: {agenda[nombre][1]}")
            print(f"\tNúmero de cuenta: {agenda[nombre][2]}\n")
            return
        else:
            print("Contacto no encontrado")
        return

def buscar_4_phone(agenda):    
        telefono = int(input("Ingresa el teléfono del contacto a buscar: "))
        for e in agenda:
            if agenda[e][0] == telefono:
                print(f"\n\tNombre: {e}")
                print(f"\tNúmero de cuenta: {agenda[e][2]}")
                print(f"\tCorreo: {agenda[e][1]}\n")
                return
        else:
            print("Contacto no encontrado")
        return

def buscar_4_nc(agenda):    
        cta = int(input("Ingresa el número de cuenta del contacto a buscar: "))
        for k in agenda:
            if agenda[k][2] == cta:
                print(f"\n\tNombre: {k}")
                print(f"\tTeléfono: {agenda[k][0]}")
                print(f"\tCorreo: {agenda[k][1]}\n")
                return
        else:
            print("Contacto no encontrado")
        return

def borrar(agenda):
    nombre = input("Ingresa el contacto a borrar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto borrado correctamente\n")
        return
    else:
        print("El contacto no existe")
    return

if __name__ == "__main__":
    opciones = ['Agregar un contacto','Buscar por nombre', 'Buscar por teléfono', 'Buscar por número de cuenta', 'Mostrar todos los contactos', 'Borrar Contacto']
    agenda = cargar_agenda('agenda.txt')

    while True:
        op = menu(opciones)
        if op == 1:
            agregar_contacto(agenda)
            pass
        elif op == 2:
            buscar_4_name(agenda)
            pass
        elif op == 3:
            buscar_4_phone(agenda)
            pass
        elif op == 4:
            buscar_4_nc(agenda)
            pass
        elif op == 5:
            print(agenda)
            print('')
            pass
        elif op == 6:
            borrar(agenda)
            print(agenda)
            pass
        else:
            print('CusBai!!')
            break
    salvar_agenda('agenda.txt', agenda)