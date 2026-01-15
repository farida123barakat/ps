name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
    status = "minor"
elif age < 60:
    status = "adult"
else:
    status = "senior"

years_to_100 = 100 - age

print(f"Hello {name} 👋")
print(f"You are {age} years old and considered an {status}.")

if years_to_100 > 0:
    print(f"You will turn 100 in {years_to_100} years.")
else:
    print("You are already 100 or older! 🎉")
