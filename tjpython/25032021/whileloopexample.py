orders = []
order=input("what would  you like to order (Q to Quit)")

while (order.upper() !='Q'):
    #find the order and add it to the list if it exists
    if found:
        orders.append(order)
    else:
        print("menu item done't exist")

    #see if the customer wants to order anything else
    order=input("Anything else?(Q to Quit)")

    orders = [];



# alive = True;

# while(alive):

#     order = input("order apa ? (Q untuk quit)");

#     if order.upper() == 'Q':

#         alive = False;

#     else:

#         orders.append(order);

# print(orders);