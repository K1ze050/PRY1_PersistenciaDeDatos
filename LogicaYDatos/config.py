import json
import os

#Archivos temporales y base
ARCHIVO = "config.json" #Nuestro archivo base en formato JSON debido a su versatilidad y eficiencia 
#al momento de manejar los datos
TEMPORAL = "config.tmp"
RESPALDO = "config.bak"

# Valores iniciales que se manejaran para la creación de la interfaz gráfica
VALORES_DEFECTO = {
    "usuario": "Invitado",
    "tema": "claro",
    "idioma": "es-ES",
    "tam_fuente": 12,
    "color_menu": "#FFFFFF",
    "color_letra": "#000000",
    "foto_perfil": ""
}

def LEER_CONF(): #Con un open("r") y enconding utf-8 cargaremos en lectura nuestro archivo base
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError): #Excepciones a no encontrar el archivo
        #El archivo no sea JSON o error de permiso
        return VALORES_DEFECTO

def GUARDAR_CONF(nuevos_datos):#Guardamos configuración con una sobrescritura con open("w") y utf-8
    try:
        with open(TEMPORAL, "w", encoding="utf-8") as f:
            json.dump(nuevos_datos, f, indent=4, ensure_ascii=False)
        
        if os.path.exists(ARCHIVO): #Si nuestro archivo base ya existe 
            os.replace(ARCHIVO, RESPALDO) #Lo reemplazamos con nuestro respaldo
            
        os.replace(TEMPORAL, ARCHIVO)#Y asi nuestro archivo temporal sera reemplazado con nuestro archivo base
        return True
    except PermissionError:
        return False