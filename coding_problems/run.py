a = [1,2,48,7] # ['1', ]

array_string = [str(str_char) for str_char in a]
# print(array_string)


import random


def songs_playlist():
    '''songs database'''
    playlist = [
        'abc',
        'xyz'
    ]
    return playlist



class Song:
    playlist = [
        'abc',
        'xyz'
    ]
    def __init__(self, new_song, user_choice):
        self.new_song = new_song
        self.user_choice = user_choice


    def add_song(self):
            Song.playlist.append(self.new_song)
            print(f'New song added and playlist is- {Song.playlist}')

    def play_song(self):
        playlist = Song.playlist
        play_song = playlist[-1]
        print('song playing')
        return play_song
            # call the interface where playing logic implemented

    @classmethod
    def shuffle_playlist(cls):
        print('*'*6)
        print(Song.playlist)
        playlist = Song.playlist
        print('*'*6)
        random.shuffle(playlist) # appropriate method for shuffling to be imported
        print(f'shuffled playlist - {playlist}')
        return random.shuffle(playlist)
        



user_x = Song(new_song='SaReGaMa', user_choice=None)
user_x.add_song()
user_x = Song(new_song='mereDesk Ki Dharti', user_choice=None)
user_x.add_song()

user_x = Song(new_song=None, user_choice='SaReGaMa')
f_song = user_x.play_song()
print(f_song)
user_x = Song(new_song=None, user_choice='mereDesk Ki Dharti')
s_song = user_x.play_song()
print(s_song)
shuffled_list = Song(new_song=None, user_choice=None)
print(shuffled_list.shuffle_playlist())
