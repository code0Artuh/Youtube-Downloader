from pytube import YouTube
from pytube import Playlist 
import os

playlist = Playlist(str(input('Cole o link da playlist: ')))

pasta = str(input('Digite um nome para a pasta: \n'))
os.mkdir(pasta)
pasta= os.getcwd()+'/'+pasta

for id,video in enumerate(playlist):
    try:
        youtube = YouTube(video)
        arquivo= youtube.streams.filter(only_audio=True).first().download(pasta)
        base, ext = os.path.splitext(arquivo)
        novoArquivo = base + '.mp3'
        os.rename(arquivo, novoArquivo)
        print(f"{youtube.title} -- Download Finalizado")
    except:
        print(f'Deu ruim nessa musica, playlist muito antiga {youtube.title}')
