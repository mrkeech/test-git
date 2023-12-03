def make_album(artist, album):
    music = {'artist': artist, 'album': album}
    return music
while True:
    a_name = input("What artist would you like to hear? ")
    album_name = input("What album do you want to play? ")
    
        

    listen_now = make_album(a_name, album_name)
    print(listen_now)