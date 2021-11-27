import time

# For loop

users = ["Lena", "Jürgen", "Mia-Sophie"]

for user in users:
    print(f"Hallo {user}"+"x")

name = "Baltrescu"

for letter in name:
    print(letter)

# While Loop

letter1 = 1
pw1 = 15

while letter1 < 23:
    print("abc")
    time.sleep(0.1)
    letter1 += 1
    print(letter1)
    if (letter1 == 15):
        print("Tja, erste Buchstabe erraten, bitch!")
        break
