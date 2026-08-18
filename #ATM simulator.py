#ATM simulator
print("==Welcome to python bank===")
balance=5000 #initial balance
pin=3423
entered_pin=int(input("Enter your pin:"))
if entered_pin==pin:
    print("Login successful!\n")
    print("1. Check balance..")
    print("2. Deposit Money..")
    print("3. withdraw Money..")
    print("4. Exit......")
    choice=int(input("enter your choice(1-4): "))
    if choice==1:
        print(f"your balance is:₹{balance}")
    elif choice==2:
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{balance}")
        print("................................................................................................")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance:
            balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using Python Bank. Goodbye!")

    else:
        print("Invalid choice! Please try again.")

else:
    print("Incorrect PIN! Access denied.")