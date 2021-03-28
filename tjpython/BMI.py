bmi=0
kg=0
hight=0

kg=float(input(("kg=")))

hight=float(input(("M=")))

bmi=kg/(hight*hight)

if bmi<18.5:
    print("you BMI are" + str(bmi))
    print("you are underweight")
    
elif bmi>=18.5  and bmi<=24.9:
    print("you BMI are" + str(bmi))
    print("you are Normal weight")

elif bmi>=25.0  and bmi<=29.9:
    print("you BMI are" + str(bmi))
    print("you are Overweight") 

elif bmi>=30.0  and bmi<=34.9:
    print("you BMI are" + str(bmi))
    print("you are Obesity class 1")

elif bmi>=35.0  and bmi<=39.9:
    print("you BMI are" + str(bmi))
    print("you are Obesity class 2")

elif bmi>=40:
    print("you BMI are" + str(bmi))
    print("you are Obesity class 3")

else:
    print("try input again")
