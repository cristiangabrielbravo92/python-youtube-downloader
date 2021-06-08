from pytube import YouTube

video_url  =    input('Pegur aquí la URL del video que desea descargar y luego presione Enter: ')


video_a_descargar  = YouTube(video_url)

print("Descargando el video " + video_a_descargar.title)

video_a_descargar = video_a_descargar.streams.get_highest_resolution()

video_a_descargar.download()