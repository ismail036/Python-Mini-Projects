from pytube import YouTube
from pytube.streams import Stream

yt = YouTube("https://www.youtube.com/watch?v=s3JNELX_5Vc")

stream = yt.streams.get_by_itag(22)

stream.download()