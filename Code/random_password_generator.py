#Importación de las librerias requeridas
#("tktinter" para GUI y "random" para la construcción de la contraseña aleatoria).
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

#Creación y personalización de la GUI.
root = tk.Tk()
root.geometry("450x140")
root.title("Generador de contraseñas")
root.resizable(0, 0)
root.config(bg = "#f54242")

#Se continua el proceso de creación de la GUI con un frame (Widget) y dentro de este sus elementos.
frame_uno = Frame()
frame_uno.pack()
frame_uno.config(width="390", height="120")
frame_uno.config(bg ="#f5c542")
#Cuadro de texto donde se mostrará la contraseña.
salida_contraseña = ttk.Entry(frame_uno, justify = tk.CENTER, width = 13) 
salida_contraseña.place(x = 152, y = 52)
#Etiquetas de texto.
etiqueta_uno_titulo = tk.Label(frame_uno, text = "Tu contraseña aleatoria y totalmente segura es:", )
etiqueta_uno_titulo.place(x = 70, y = 17)
etiqueta_dos_nombre = tk.Label(root, text = "Public Domain  - By Jabes E. Monroy", bg = "#f54242", fg = "#f5c542",font = ("Times", 10, "italic"))
etiqueta_dos_nombre.place(x = 241, y = 120)

#Función encargada de mezclar las variables con valores aleatorios de forma al azar.
def mezclador (a):
    contraseña_desordedana_definitiva = list(a)
    random.shuffle(contraseña_desordedana_definitiva)
    return ''.join(contraseña_desordedana_definitiva)

#Función ordenada por "boton_copiar" encargada de copiar al portapales la contraseña enseñada en el campo de texto.
def copiar_al_portapapeles():
    frame_uno.clipboard_clear()
    frame_uno.clipboard_append(salida_contraseña.get())

#Función ordenada por "boton_generador" encargada de generar una contraseña aleatoria, 
# además de llamar a la función "mezclador" para desordenar los caracteres generados 
# y por último mostrarla en el campo de texto "salida_contraseña".
def generar_contraseña(): 
    salida_contraseña.delete("0","end")   
    letra_mayuscula_1 = chr(random.randint(97,122))
    letra_mayuscula_2 = chr(random.randint(97,122))
    letra_minuscula_1 = chr(random.randint(65,90))
    letra_minuscula_2 = chr(random.randint(65,90)) 
    digito_numero_1 = chr(random.randint(48,57))
    digito_numero_2 = chr(random.randint(48,57))
    digito_simbolo_1 = chr(random.randint(33,148))
    digito_simbolo_2 = chr(random.randint(33,148))
    contraseña_ordenada = digito_simbolo_2 + digito_simbolo_1 + digito_numero_2 + digito_numero_1 + letra_minuscula_2 + letra_minuscula_1 + letra_mayuscula_2 + letra_mayuscula_1
    contraseña_definitiva = mezclador(contraseña_ordenada)
    return salida_contraseña.insert(0, contraseña_definitiva) #Devuelve la contraseña aleatoria.

#Se crean los botones "boton_copiar" y "boton_generador" para la GUI con sus command.
boton_copiar = Button(frame_uno, text = "Copiar contraseña", command = copiar_al_portapapeles).place(x = 87, y = 85)
boton_generador = Button(frame_uno, text = "Generar contraseña", command = generar_contraseña).place(x = 205,y = 85)
root.mainloop()