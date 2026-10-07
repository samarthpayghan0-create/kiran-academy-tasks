age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 18:
    print("You are not eligible to vote")
    
elif age < 120:
    print("Invalid age")
else:
    print("You are eligible to vote")