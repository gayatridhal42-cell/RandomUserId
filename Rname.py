import random
name = input("enter your name :")
vibes = ["cool","girly","ag","bg","confused"]

for i in range(5):
    print(name + random.choice(vibes) + str(random.randint(1,100)))
