from queue import Queue         #importamos el modulo para poder trabajar con colas por la forma estructurada de ingresar los datos

datos_entrada=input("Ingrese los numeros de entrada separados por una coma: ")
borrador=datos_entrada.split(",")
entrada=[]

for i in borrador:
    if (i != ''):
        entrada.append(i)


num_entrada = len(entrada)     #numero de datos(puede servir para el numero de columnas)
filas = int(input("Ingrese el numero de filas con las que desea trabajar: "))
print("\n")



def paginaFallas(entrada, num_entrada, filas):
    print("\n","paginas")
    s = set()   #creamos un nuevo conjunto sin elementos
    queue = Queue()  #creamos la variable para el uso de la cola

    pagina_fallas = 0
    for i in range(num_entrada):  #ciclo para avanzar por los datos ingresados

        # si el conjunto tiene menos elementos que las filas ingresadas,el conjunto puede contener más elementos
        if len(s) < filas:

            # Si el elemento entrante no está presente, se añade al conjunto
            if entrada[i] not in s:
                s.add(entrada[i])

                # incrementar el fallo de la pagina
                pagina_fallas += 1

                # Agregamos elementos a la cola  
                queue.put(entrada[i])

        # Si el conjunto está lleno, debeoms reemplazar la pagina de lo que entra primero, es decir, eliminar el primer elemento
        # del conjunto y la cola para luego insertar la página entrante
        else:

            # si el elemento entrante no esta presente
            if entrada[i] not in s:
                # eliminar la primera pagina de la cola
                val = queue.queue[0]

                queue.get()

                # eliminar del conjunto
                s.remove(val)

                # insertar la pagina de entrada 
                s.add(entrada[i])

                # Agregamos elementos a la cola
                queue.put(entrada[i])

                # incrementar los fallos de pagina 
                pagina_fallas += 1

        
        for q_item in queue.queue:
            print("|",q_item,"|",end="\t")
            
        print()
    return pagina_fallas

for i in range(num_entrada):
    print("|",entrada[i],"|",end="\t")

pagina_fallas = paginaFallas(entrada, num_entrada, filas)
print("\nFallos de pagina: ", pagina_fallas)

#Bibliografia
"""
https://www.youtube.com/watch?v=z6RTx0YXa-A&list=LL&index=1&t=51s
https://j2logo.com/python/tutorial/tipo-set-python/
https://pythontic.com/queue-module/queue-class/put 
https://www.geeksforgeeks.org/queue-in-python/#:~:text=get()%20%E2%80%93%20Remove%20and%20return,an%20item%20into%20the%20queue.

"""