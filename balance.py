balance = 100000
amount = int(input("enter amount"))
if amount <= balance:
    balance -= amount
    print("withdrawa Successful")
    print("Remaining Blance:",balance)
else:
    print("Insuffieient Balance Amount ..!!")