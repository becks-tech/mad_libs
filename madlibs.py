import random

def select_story():
    with open('mad_lib_stories.txt') as f:
        stories = f.readlines()
        return random.choice(stories)


story = select_story()

adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")


completed_story = story.replace("__adjective__", adj).replace("__noun__", noun).replace("__verb__", verb).replace("__place__", place)

print(completed_story)