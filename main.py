from yt_dlp import YoutubeDL
import ffmpeg
from components.acortador import acortar
import os

def precarga():
    for folder in os.listdir("."):
        if folder == "descargado":
            creacion = False
        else:
            creacion = True
    if creacion == False:
        os.mkdir("descargado")
    else:
        pass
    
    os.chdir("./descargado")


def cargar():
    url = input("Ingrese el url a descargar \n")
    cargar = "s"

    while cargar == "s":
        urls = []

        urls.append(url)

        cargar = input("Desea cargar otro url?  S / N  \n")

    return urls

def seleccion(urls):
    while urls:
        opcion = input("Seleccione que va a descargar: 1 - Video   ||  2 - Musica  || Presiona cualquier letra para salir \n")

        if opcion == "1":
            descargarVideos(urls)

        elif opcion == "2":
            descargarMusica(urls)
        else:
            break



def descargarVideos(urls):
    
    ydl_opts = {
        'format': 'mp4/bestvideo*/best'

    }

    with YoutubeDL() as ydl:
        ydl.download(urls)


def descargarMusica(urls):

    ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

    with YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)

def main():
    precarga()
    urls = cargar()
    seleccion(urls)
    acortar()


if __name__ == '__main__':
    main()