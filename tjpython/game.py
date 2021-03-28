from random import randint
# value = random.randint(1,10)
# print(value)
#0.2

print('colossal cave')
print('the first adventure')
name=input("what is your name?\n")
rolename=False
while rolename ==False :
    role=input('what is your role? [wizard,warrior,monk,mage]\n')

    if role=="wizard":
        rolename=True
    if role=="warrior":   
         rolename=True
    if role=="monk": 
         rolename=True
    if role=="mage": 
         rolename=True
    else:
        print("There is no such role name, please try again")
        rolename=False

age=int(input("what is your age?\n"))
#if 20 year old and below consibered young otherwise old
print("Hi",name,"your role is",role)

if age>=20:
    print("you are old!!")

else:
    print("you are so young!!")

pH =randint(50,100)
mH =randint(50,100)
#if pH<mH print(danger) if pH= mH print (you weill make) else print(sure win) 

print(pH,mH)

if pH<mH:
    print("danger")
elif pH==mH:
    print("you will make")
else:
    print("sure win")

monsters=['haha','baba','koko']

for monster in monsters :
    print(monster)

# [nilai monster health]
# [monster is bleeding :health]   

monster_health=[60,10,20,30] 

for a in monster_health :
    print("monster is bleeding",str(a))

if mH % age> 5 & pH<65:
    print("you got chances to get gold")

elif mH % age>3 & pH<40:
    print("you got coins instead")

else:
    print("no tresure for you")    