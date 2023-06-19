import random
import tkinter as tk # Se importan dos librerias, una para elegir palabras random y la otra para mostrar imagenes 
from PIL import ImageTk, Image
prandom = "" # Hacemos un prandom que será la palabra que vamos a adivinar
def ahorcadomj(prandom, user): # Hacemos una función para cuando jueguen dos personas
    prandom=input("Pon la palabra que quieras que el otro jugador adivine: ") # La palabra se da por otro usuario
    definiciones = {}
    clave = prandom
    valor = input("Ingrese la definición en caso de que la quiera usar el otro: ")
    n = int(input("ingrese la cantidad de vidas del otro: "))
    definiciones[clave] = valor 
    letrasusadas = [] # Hacemos un arreglo con las letras que se han usados que se muestran a veces
    score = 10.0 # Se pone un score que tiene como maximo el 10.0
    x = ["_"] * len(prandom) # Hacemos una x que va a ser la palabra que vamos adivinando
    proh3=False # Hacemos unas banderas en falso para que luego se puedan cambiar
    proh4=False
    proh5=False
    proh6=False
    proh7=False
    proh8=False
    
    while n > 0: # Hacemos un menú que se muestra en bucle hasta que se acaben las vida "n" o cuando se adivine la palabra
        print("_-_-_-_ MENÚ _-_-_-_")
        print("1: Adivinar una letra")
        print("2: Adivinar la palabra directamente")
        print("3: ¿Hay tildes?")
        print("4: Poner vocales")
        print("5: Poner primera letra")
        print("6: Poner última letra")
        print("7: Poner letra aleatoria")
        print("8: ¿Cuál es la definición de la palabra?")
        print("9: Salir")
        opcion = input("Elige una opción: ") # Pedimos un valor para poder usar las opciones

        if opcion == "1": # Se hace la opción número 1
            letra = input(user + ", ingresa una letra : ").lower()  # Se pide una letra y se aplica el lower para que se procese todo en minusculas
            if letra in letrasusadas: # Se revisa si la letra ya se usó comparando con el arreglo con las usadas
                print(user + ", esa letra ya se usó.") 
            else:
                letrasusadas.append(letra) # Se agrega la letra al arreglo de las usadas
                if letra in prandom: # Se revisa si la letra está en la palabra secreta
                    for i in range(len(prandom)): # En el rango de de la palabra secreta
                        if prandom[i] == letra: # se ve si alguna letra en el rango i, es igual a la letra ingresada
                            x[i] = letra # Se iguala el valor de la letra con el lugar de la letra secreta
                    print(user + ", ¡Adivinaste una letra!") # Se muestra un mensaje dando felicitación por eso
                    print(user + ", La palabra de momento es: " + " ".join(x)) # Se muestra como va la palabra con el join(x)
                    if "_" not in x: # En caso de que ya no hayan más incognitas en la x, queriendo decir que ya se descifró 
                        print("Has adivinado la palabra, " + user + "y tu puntaje del 1.0-10.0 es " + str(score) )
                        return # Se muestra el mensaje junto con el score y se acaba el bucle
                else:
                    n -= 1 # En caso de no adivinar la palabra se resta un vida
                    score -= 0.2 # Se le baja al score
                    print("Faltan", n, "Vidas") # Se muestra la cantidad de vidas para tenerlo en cunta
                    if n == 0: # Se muestar una imagen de acuerdo con cada vida, haciendo un ahorcado
                        root = tk.Tk() # Se busca la imagen y se muestra
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss8.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Perdiste") # Se muestran los mensajes de acuerdo con la cantidad de vida
                        print("La palabra era:", prandom)
                    if n == 7:
                        root = tk.Tk()
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss1.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Faltan", n, "Vidas")
                    elif n == 6:
                        root = tk.Tk()
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss2.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Faltan", n, "Vidas")
                    elif n == 5:
                        root = tk.Tk()
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss3.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Faltan", n, "Vidas")
                    elif n == 4:
                        root = tk.Tk()
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss4.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Faltan", n, "Vidas")
                    elif n == 3:
                        root = tk.Tk()
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss5.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Faltan", n, "Vidas")
                    elif n == 2:
                        root = tk.Tk()
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss6.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Faltan", n, "Vidas")
                    elif n == 1:
                        root = tk.Tk()
                        imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss7.ico"))
                        boton = tk.Button(image=imagen, command=root.quit)
                        boton.pack()
                        root.mainloop()
                        print("Faltan", n, "Vidas")
        elif opcion == "2": # Se hace la opción número 2
            palabradefe = input(user + ", ingresa una palabra: ").lower() # Se pide una palabra para ver si se adivina directamente
            if palabradefe.lower() == prandom.lower():
                x = palabradefe # Si la palabra es igual se acaba el programa
                print(str(x))
                print("Has adivinado la palabra, " + user + "y tu puntaje del 1.0-10.0 es " + str(score) )
                return
            else:
                score -= 0.3 # En caso de no adivinar se hace una reducción de vidas y score
                n -= 1
                print("Sigue intentando bro") # Se hace lo mismo que en la opción 1
                if n == 0:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss8.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Perdiste")
                    print("La palabra era:", prandom)
                if n == 7:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss1.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Faltan", n, "Vidas")
                elif n == 6:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss2.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Faltan", n, "Vidas")
                elif n == 5:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss3.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Faltan", n, "Vidas")
                elif n == 4:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss4.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Faltan", n, "Vidas")
                elif n == 3:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss5.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Faltan", n, "Vidas")
                elif n == 2:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss6.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Faltan", n, "Vidas")
                elif n == 1:
                    root = tk.Tk()
                    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss7.ico"))
                    boton = tk.Button(image=imagen, command=root.quit)
                    boton.pack()
                    root.mainloop()
                    print("Faltan", n, "Vidas")

        elif opcion == "3": # Se hace la opción número 3
            if proh3: # Se revisa si la bandera es True para decir que ya se usó
                print("La opción 3 ya se usó")
            else:
                score -= 0.3 # Se baja al score por el uso del comodin y se cambia la bandera a True parano volver a usar la opción
                proh3 = True
                for i in prandom: # Se busca en la palabra a ver si tiene vocales con tilde
                    if i in "áéíóú":
                        sitildes = True # Se hace un bandera si existen tildes
                    else:
                        sitildes = False
                if sitildes:
                    print("La palabra contiene tildes") # si es verdadera se imprime que si hay tildes
                else:
                    print("La palabra no contiene tildes") # Lo contrario en caso de que no

        elif opcion == "4": # Se hace la opción número 4
            if proh4:   # Se revisa si la bandera es True para decir que ya se usó
                print("La opción 4 ya se usó")
            else:
                score -= 3.5 # Se baja al score por el uso del comodin 
                vocales = "aeiouáéíóú"
                for i in range(len(prandom)):
                    if prandom[i] in vocales: # Se revisa si la palabras secreta tiene vocales
                        x[i] = prandom[i] # Se ponen las vocales en la incognita
                        print(user + ", La palabra de momento es: " + " ".join(x)) # Se muestar la palabra
                        proh4 = True # se cambia la bandera a True parano volver a usar la opción
                        if "_" not in x: # En caso de que ya no hayan más incognitas en la x, queriendo decir que ya se descifró 
                            print("Has adivinado la palabra, " + user + "y tu puntaje del 1.0-10.0 es " + str(score) )
                            return
        elif opcion == "5": # Se hace la opción número 5
            if proh5: # Se revisa si la bandera es True para decir que ya se usó
                print("La opción 5 ya se usó")
            else:
                score -= 0.5 # Se baja al score por el uso del comodin
                x[0] = prandom[0] # Reemplaza la incognita con la letra en la posicion 0
                print(user + ", La palabra de momento es: " + " ".join(x))
                proh5 = True # se cambia la bandera a True parano volver a usar la opción
                if "_" not in x : # En caso de que ya no hayan más incognitas en la x, queriendo decir que ya se descifró 
                    print("Has adivinado la palabra, " + user + "y tu puntaje del 1.0-10.0 es " + str(score) )
                    return

        elif opcion == "6": # Se hace la opción número 6
            if proh6: # Se revisa si la bandera es True para decir que ya se usó
                print("La opción 6 ya se usó")
            else:
                score -= 0.5 # Se baja al score por el uso del comodin
                x[-1] = prandom[-1]  # Reemplaza la incognita con la letra en la posicion -1
                print(user + ", La palabra de momento es: " + " ".join(x))
                proh6 = True # se cambia la bandera a True parano volver a usar la opción
                if "_" not in x: # En caso de que ya no hayan más incognitas en la x, queriendo decir que ya se descifró 
                    print("Has adivinado la palabra, " + user + "y tu puntaje del 1.0-10.0 es " + str(score) )
                    return

        elif opcion == "7": # Se hace la opción número 7
            if proh7: # Se revisa si la bandera es True para decir que ya se usó
                print("La opción 7 ya se usó")
            else:
                score -= 0.5 # Se baja al score por el uso del comodin
                j = random.randint(0,len(prandom)) # se busca un numero random para poner subindice posteriormente
                x[j-1] = prandom[j-1] # Reemplaza la incognita con la letra en la posicion random
                print(user + ", La palabra de momento es: " + " ".join(x))
                proh7 = True # se cambia la bandera a True parano volver a usar la opción
                if "_" not in x: # En caso de que ya no hayan más incognitas en la x, queriendo decir que ya se descifró 
                    print("Has adivinado la palabra, " + user + "y tu puntaje del 1.0-10.0 es " + str(score) )
                    return
        elif opcion == "8": # Se hace la opción número 8
            if proh8: # Se revisa si la bandera es True para decir que ya se usó
                print("La opción 8 ya se usó")
            else:
                score -= 3.4 # Se baja al score por el uso del comodin
                if prandom in definiciones:
                    print(definiciones[prandom]) # Se imprime el key y la definición de la misma
                    proh8 = True # se cambia la bandera a True parano volver a usar la opción
                else:
                    print("No se encontró la definición de la palabra")
        elif opcion == "9": # Se hace la opción número 9
            print("Gracias por jugar. ¡Hasta luego!") # En caso de salirse se cierra el bucle
            return

        else:
            print("Opción inválida. Por favor, elige una opción válida.") # En caso de no poner ninguna opción se vuelve al bucle

    print("Faltan", n, "Vidas")
    root = tk.Tk()
    imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\PC\downloads\ss8.ico"))
    boton = tk.Button(image=imagen, command=root.quit)
    boton.pack()
    root.mainloop()
    print("Perdiste")
    print("La palabra era:", prandom) # Esto pasa en caso de acabar las vidas
print("¡Bienvenido!") # Se imprime el bienvenido
user = input("Ingresa tu nombre: ") # Se pide el nombre del user que posteriormente vamos a usar
ahorcadomj(prandom, user)