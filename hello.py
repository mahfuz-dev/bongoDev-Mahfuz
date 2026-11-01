# hello.py
name = input("Your name: ")
age = int(input("Your age: "))

print(f"Hello, {name}!")

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

for i in range(1, 4):
    print(f"Count: {i}")