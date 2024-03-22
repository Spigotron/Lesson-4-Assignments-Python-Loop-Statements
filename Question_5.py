# Task 1

import random

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
tracks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_track = random.choice(tracks)

for genre in genres:
    if genre == "Jazz":
        print(f"You're listening to track #{random_track} in the jazz genre!")
    if genre == "Rock":
        print(f"You're listening to track #{random_track} in the rock genre!")
    if genre == "Hip-hop":
        print(f"You're listening to track #{random_track} in the hip-hop genre!")
    if genre == "Classical":
        print(f"You're listening to track #{random_track} in the classical genre!")

# Task 2
        
import random

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
tracks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_track = random.choice(tracks)
index = 0
while index < len(genres):
    genre = genres[index]
    print(f"You're listening to track #{random_track} in the {genre} genre!")
    if genre == "Hip-hop":
        print("No hip-hop allowed! Turning off radio.")
        break
    index += 1

# Task 3
    
import random

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
tracks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_track = random.choice(tracks)

for i in range(len(genres)):
    genre = genres[i]
    if genre == "Classical":
        continue
    print(f"The light show is ready! It's time for track #{random_track} in {genre}!")