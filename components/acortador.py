import os

def acortar():
    for song in os.listdir("."):
        song = os.rename(song, song.strip('[dVUmSgzgOqs]'))
