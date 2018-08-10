print("Welcome to In-N-Out!")

hb = 3.25
cb = 4.10
ff = 2.45
vs = 3.00
ss = 3.75

price = 0.0
burger = input("Would you like a Hamburger or a Cheeseburger? ")

if burger.lower() == "hamburger":
    print("Got it, one hamburger.")
    price = price + hb
elif burger.lower() == "cheeseburger":
    print("Comin up, one cheeseburger.")
    price = price + cb

fries = input("Would you like fries? ")

if fries.lower() == "yes":
    print("Great")
    price = price + ff
    
shake = input("Would you like a Strawberry Shake or a Vanilla Shake? ")

if shake.lower() == "strawberry":
    print("My favorite, you're all set.")
    price = price + ss
elif shake.lower() == "vanilla":
    print("Great, you are set.")
    price = price + vs
print("You're total price is: $"+ str(price))