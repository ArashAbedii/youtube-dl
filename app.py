import youtube_dl

ydl=youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})


with ydl:
    result = ydl.extract_info(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        download=False # We just want to extract the info
    )

print(result)