total = 0;

expense = [];

expense_count = int(input("Enter of expense : "));

for i in range(expense_count):

    expense.append(float(input("Enter an expense : RM ")));

print (expense)


total = sum(expense);

formula = "";

for each in expense:

    formula +=str(each) +" + ";

print("\nYou spend "+formula+"0 = RM "+str(total));