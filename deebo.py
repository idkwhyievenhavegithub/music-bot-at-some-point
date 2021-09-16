import deezer
from rich import print
dc = deezer.Client()

song_name = input("/> ")

res = dc.search(song_name)
lim = 0

for x in res:
    if lim == 5:
        break
    else:
        pass
    print("Title: "+str(x.as_dict()["title"])+"\nArtist: "+str(x.as_dict()['artist']['name'])+"\nAlbum: "+str(x.as_dict()['album']['title']))
    lim += 1