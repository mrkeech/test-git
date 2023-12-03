def make_album(artist_name, album_name, tracks=''):
    if tracks:
        album = {'artist': artist_name, 'album': album_name, 'tracks': tracks}
        return album
    else:
        album = {'artist': artist_name, 'album': album_name}
        return album


album_details = make_album('Matt Keech', 'Wide Awake', 7)
print(album_details)

album_details = make_album('Jimi', 'Experience')
print(album_details)

album_details = make_album('Robert Plant', 'Zeppelin 1', 14)
print(album_details)