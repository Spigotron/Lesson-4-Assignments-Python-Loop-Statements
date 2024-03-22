# Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres[1:4]:
    print(genre)

# Task 2

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres:
    genre = str(genre)

list = [genre + " Music" for genre in genres]
print(list)

# Task 3

countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(countdown)):
    number = countdown[i]
    print(number)
print("The beat drops now!")