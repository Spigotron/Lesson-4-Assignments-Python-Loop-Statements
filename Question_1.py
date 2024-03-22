days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["happy", "sad", "calm", "energetic", "serious", "ecstatic", "angry"]

import random

for day in days:
    mood_swing = random.choice(moods)
    print(f"On {day}, you were feeling {mood_swing}")