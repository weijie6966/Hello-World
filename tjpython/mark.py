mark=float(input("your mark\n"))

if mark>=80 and mark<=100 :
   print("you get A")
 
elif mark>=60 and mark<=79:
    print("you get B")
 
elif mark>=40 and mark<=59:
    print("you get C")
 
elif mark>=0 and mark<=39:
    print("you get failed")
 
elif mark>101 :
    print("You have input the invalid marks")
 
else:
    print("try input again")