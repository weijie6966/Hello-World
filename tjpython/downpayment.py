house_price=300000
credit = input ("your creadit\n")
downpayment=0

if  credit== "GOOD":  
    print("GOOD creadit entitled 10 persem downpayment")
    downpayment=house_price*0.1
    print("downpayment are"+str(downpayment))

elif credit=="NOTGOOD":
    print("NOT GOOD creadit entitled 28 persem downpayment") 
    downpayment=house_price*2.8 
    print("downpayment are"+str(downpayment)) 
else:
    print("try again")    



goodcreadt= True

if goodcreadt:
    downpayment=house_price*0.1

else:
    downpayment=house_price*0.28