orders = [];

alive = True;
while(alive):
    order = input("order apa ? (Q untuk quit)");
    if order.upper() == 'Q':
        alive = False;
    else:
        orders.append(order);
print(orders);