import tkinter as tk
from InterfazDeUsuario.setting_vent import ABRIR_SET
from LogicaYDatos.config import LEER_CONF

def SIM_OPC():
    pass

def ACT_VIS(vent, lbl):
    conf = LEER_CONF()
    
    fondo = "#2b2b2b" if conf.get("tema") == "oscuro" else "#ffffff"
    vent.config(bg=fondo)
    
    lbl.config(
        text=f"Usuario: {conf.get('usuario')}\nIdioma: {conf.get('idioma')}",
        fg=conf.get("color_letra"),
        bg=fondo,
        font=("Arial", conf.get("tam_fuente"))
    )

def INI_PRINC():
    vent = tk.Tk()
    vent.title("Panel Principal - Gestor de Archivos")
    vent.geometry("600x400")

    menu_bar = tk.Menu(vent)
    
    m_arch = tk.Menu(menu_bar, tearoff=0)
    m_arch.add_command(label="Opcion Simulada", command=SIM_OPC)
    menu_bar.add_cascade(label="Archivo", menu=m_arch)

    m_edi = tk.Menu(menu_bar, tearoff=0)
    m_edi.add_command(label="Opcion Simulada", command=SIM_OPC)
    menu_bar.add_cascade(label="Edición", menu=m_edi)

    m_ver = tk.Menu(menu_bar, tearoff=0)
    m_ver.add_command(label="Opcion Simulada", command=SIM_OPC)
    menu_bar.add_cascade(label="Ver", menu=m_ver)

    menu_bar.add_command(label="Settings", command=lambda: ABRIR_SET(vent))

    vent.config(menu=menu_bar)

    lbl_usu = tk.Label(vent)
    lbl_usu.pack(expand=True)

    btn_act = tk.Button(vent, text="Actualizar Interfaz", command=lambda: ACT_VIS(vent, lbl_usu))
    btn_act.pack(pady=25)

    ACT_VIS(vent, lbl_usu)

    vent.mainloop()