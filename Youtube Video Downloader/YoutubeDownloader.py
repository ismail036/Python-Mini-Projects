from pytube import YouTube
from pytube.streams import Stream



yt = input("İndirmek istediğiniz videonun linkini giriniz ")

stream = yt.streams.get_by_itag(22)

stream.download()
