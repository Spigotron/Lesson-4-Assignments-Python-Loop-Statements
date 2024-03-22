days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times = ["morning", "afternoon", "evening"]
moods = ["amazed", "amused", "angry", "awestruck", "bemused", "calm", "cheerful", "delighted", "depressed", "despondent", "discouraged", "dispirited", "frightened", "happy", "ecstatic", "energetic", "furious", "horrified", "incredulous", "puzzled", "reverent", "sad", "scared", "serious", "somber", "spirited", "stupefied", "terrified"]

import random

for day in days:
    for time in times:
        mood_swing = random.choice(moods)
        print(f"On {day} {time}, you were feeling {mood_swing}")