#Importación de las librerias requeridas. ("tktinter" para GUI y "random" para la generación de la contraseña aleatoria).
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

#Creación y personalización de la GUI.
root = tk.Tk()
root.geometry("450x120")
root.iconbitmap(r"C:\Users\USUARIO\Desktop\Nueva carpeta\Portafolio\proyecto_1_contraseñas_aleatorias\Back\Code\icono_app.ico")
root.title("Generador de contraseñas")
root.resizable(0, 0)
root.config(bg = "#f54242")

frame_uno = Frame()
frame_uno.pack()
frame_uno.config(width="390", height="100")
frame_uno.config(bg ="#f5c542")
entrada = ttk.Entry(frame_uno, justify = tk.CENTER, width = 10)
entrada.place(x = 163, y = 60)
etiqueta_uno = tk.Label(frame_uno, text = "Tu contraseña aleatoria de 8 caracteres y totalmente segura es:", )
etiqueta_uno.place(x = 25, y = 30)
etiqueta_jabes = tk.Label(root, text = "Public Domain  - By Jabes E. Monroy", bg = "#f54242", fg = "#f5c542",font = ("Times", 10, "italic"))
etiqueta_jabes.place(x = 241, y = 100)

#Función encargada de mezclar las variables aleatorias de forma al azar.
def mezclador (a):
    contraseña_definitiva = list(a)
    random.shuffle(contraseña_definitiva)
    return ''.join(contraseña_definitiva)

letras_mayusculas_1 = chr(random.randint(97,122))
letras_mayusculas_2 = chr(random.randint(97,122))
letras_minusculas_1 = chr(random.randint(65,90))
letras_minusculas_2 = chr(random.randint(65,90)) 
digito_numerico_1 = chr(random.randint(48,57))
digito_numerico_2 = chr(random.randint(48,57))
digito_simbolico_1 = chr(random.randint(33,148))
digito_simbolico_2 = chr(random.randint(33,148))
contraseña_ordenada = digito_simbolico_2 + digito_simbolico_1 + digito_numerico_2 + digito_numerico_1 + letras_minusculas_2 + letras_minusculas_1 + letras_mayusculas_2 + letras_mayusculas_1
password = mezclador(contraseña_ordenada)

#Salida de la contraseña aleatoria.
entrada.insert(0, password)
root.mainloop()
