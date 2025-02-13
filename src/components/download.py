from yt_dlp import YoutubeDL


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