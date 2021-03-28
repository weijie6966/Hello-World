import random

friend=['tj','hakim','diana','ali','bula','cadu']
for x in friend:
    print(x)

print("\nAdd 2 name")
friend.append('lol')
friend.append('joker')
for x in friend:
    print(x)

print("\nDel last name")
friend.remove('joker')
for x in friend:
    print(x)

lucky_friend = random.choice(friend)
print("you are the lucky friend "+lucky_friend)    
