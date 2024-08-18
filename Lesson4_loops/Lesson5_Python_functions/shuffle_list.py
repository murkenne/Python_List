# Exercise 3: The Dynamic Playlist

def play_songs(song_list):
    for song in song_list:
        print(f"Now playing: {song}")
        
num_songs = int(input("How many songs would you like to add to the playlist? "))
    
user_playlist = []
    
for i in range(num_songs):
    song_name = input(f"Enter song {i+1}:")
    user_playlist.append(song_name)
play_songs(user_playlist) 