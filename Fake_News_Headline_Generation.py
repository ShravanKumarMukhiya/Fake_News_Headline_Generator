
import random

subjects = [
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group Of Students",
    "A Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

action = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India Gate"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(action)
    places_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS:{subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip()

    if user_input == "no":
        break

    #print goodbye message
    print("\nThanks for using the Fake News Headline Generator. Have a fun day")
