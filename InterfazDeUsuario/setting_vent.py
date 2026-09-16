import tkinter as tk
from tkinter import ttk, filedialog, colorchooser, messagebox
from LogicaYDatos.config import LEER_CONF, GUARDAR_CONF #Llamamos a las funciones
#de guardado y lectura base


def ABRIR_SET(padre):
#Con esto nos permite leer el archivo de configuración 
    vent = tk.Toplevel(padre)
    vent.title("Settings")
    vent.geometry("350x400")

    conf = LEER_CONF()
#Configuración base
    var_usu = tk.StringVar(value=conf.get("usuario", ""))
    var_tema = tk.StringVar(value=conf.get("tema", "claro"))
    var_idioma = tk.StringVar(value=conf.get("idioma", "es-ES"))
    var_fuente = tk.IntVar(value=conf.get("tam_fuente", 12))
    var_col_menu = tk.StringVar(value=conf.get("color_menu", "#FFFFFF"))
    var_col_letra = tk.StringVar(value=conf.get("color_letra", "#000000"))
    var_foto = tk.StringVar(value=conf.get("foto_perfil", ""))

    def SEL_C_MENU(): #Usando colorchooser guardamos el hexadecimal y lo guardamos 
        color = colorchooser.askcolor(title="Color Menú")[1]
        if color: 
            var_col_menu.set(color)

    def SEL_C_LETRA():#Lo mismo que el color del menu pero ahora con el tamaño de letra
        color = colorchooser.askcolor(title="Color Letra")[1]
        if color: 
            var_col_letra.set(color)

    def SEL_FOTO():
#Abre el explorador de archivos para que el usuario seleccione foto de perfil 
        ruta = filedialog.askopenfilename(title="Foto Perfil", filetypes=[("Imágenes", "*.png *.jpg *.jpeg")])
        if ruta: 
            var_foto.set(ruta)

    def GUAR_DAT():
#Empaquetamos todo los datos obtenidos para luego usar "GUARDAR_CONF()"
#para usar su lógica interna para guardar el JSON
        nuevos = {
            "usuario": var_usu.get(),
            "tema": var_tema.get(),
            "idioma": var_idioma.get(),
            "tam_fuente": var_fuente.get(),
            "color_menu": var_col_menu.get(),
            "color_letra": var_col_letra.get(),
            "foto_perfil": var_foto.get()
        }
        if GUARDAR_CONF(nuevos):
            messagebox.showinfo("Éxito", "Configuración guardada.")
            vent.destroy()
        else:
            messagebox.showerror("Error", "No se pudo guardar (Permisos).")

    tk.Label(vent, text="Usuario:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
    tk.Entry(vent, textvariable=var_usu).grid(row=0, column=1)

    tk.Label(vent, text="Tema:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
    ttk.Combobox(vent, textvariable=var_tema, values=["claro", "oscuro"], state="readonly").grid(row=1, column=1)

    tk.Label(vent, text="Idioma:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
    ttk.Combobox(vent, textvariable=var_idioma, values=["es-ES", "en-US"], state="readonly").grid(row=2, column=1)

    tk.Label(vent, text="Tamaño Fuente:").grid(row=3, column=0, pady=10, padx=10, sticky="w")
    tk.Entry(vent, textvariable=var_fuente).grid(row=3, column=1)

    tk.Label(vent, text="Color Menú:").grid(row=4, column=0, pady=10, padx=10, sticky="w")
    tk.Button(vent, text="Elegir Color", command=SEL_C_MENU).grid(row=4, column=1)

    tk.Label(vent, text="Color Letra:").grid(row=5, column=0, pady=10, padx=10, sticky="w")
    tk.Button(vent, text="Elegir Color", command=SEL_C_LETRA).grid(row=5, column=1)

    tk.Label(vent, text="Foto Perfil:").grid(row=6, column=0, pady=10, padx=10, sticky="w")
    tk.Button(vent, text="Buscar Archivo", command=SEL_FOTO).grid(row=6, column=1)

    tk.Button(vent, text="GUARDAR", command=GUAR_DAT).grid(row=7, columnspan=2, pady=20)