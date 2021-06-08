from pytube import Youtube

url  =    input('Ingresar URL del video que desea descargar: ')
video_a_descargar  = YouTube(url)

print("Descargando el video " + video_a_descargar.title)

video_a_descargar = video_a_descargar.streams.get_highest_resolution()

video_a_descargar.download()