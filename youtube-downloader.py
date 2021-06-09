from pytube import YouTube
import os
import sys
import subprocess

'''
Script para descargar videos de youtube en su mejor resolución y guardarlos en la carpeta donde se ejecuta el script a partir de ingresar la url del video durante la ejecución.
'''

def open_folder(path):
	´´´
	Esta función chequea qué sistema operativo está siendo usado para ver cómo abrir una carpeta.
	Más info en:
	- https://docs.python.org/3/library/sys.html	
	´´´
    if sys.platform.startswith('darwin'):
        subprocess.check_call(['open', '--', path])
    elif sys.platform.startswhith('linux'):
        subprocess.check_call(['gnome-open', '--', path])
    elif sys.platform.startswith('win32'):
        subprocess.check_call(['explorer', path])

video_url  =    input('Pegue aquí la URL del video que desea descargar y luego presione Enter: ')
video_a_descargar  = YouTube(video_url)

nombre_video = video_a_descargar.title #obtiene el nombre del video para mostrarlo en pantalla en la siguiente línea
print("Descargando \'" + nombre_video + "\'")

working_directory = os.getcwd() #obtiene la ubicación donde se está ejecutando el script y donde se guardará el video 
print("Guardando el video en " + working_directory)

video_a_descargar = video_a_descargar.streams.get_highest_resolution() #obtiene la mejor resolución disponible del video
video_a_descargar.download() #y la descarga

subprocess.Popen('explorer "{}"'.format(working_directory)) #antes de finalizar, abre en el explorador de archivos la carpeta donde se descargó

input("Programa Finalizado con éxito, presione Enter para salir")
