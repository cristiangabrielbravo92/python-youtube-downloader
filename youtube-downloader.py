from pytube import YouTube
import os
#import subprocess


video_url  =    input('Pegue aquí la URL del video que desea descargar y luego presione Enter: ')


video_a_descargar  = YouTube(video_url)

nombre_video = video_a_descargar.title

print("Descargando \'" + nombre_video + "\'")

video_a_descargar = video_a_descargar.streams.get_highest_resolution()

working_directory = os.getcwd() + "/"

print("Guardando el video en " + working_directory)

video_a_descargar.download()


#Revisar este bloque para que al terminar de descargar, se abra la ventana que contiene el archivo descargado y haga focus en el archivo
#wd_plus_file = working_directory + "readme.md"
#subprocess.Popen(r'explorer /select,"{}"'.format(wd_plus_file))

input("Programa Finalizado con éxito, presione Enter para salir")