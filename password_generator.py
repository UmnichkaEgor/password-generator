import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation =  "!$%&*+-=?@^_"

lol = ["yes"]
print("Hi. Its the 'Secure Password Generation'")
menge = int(input("How much do you want to have passwords?: "))

def password():
    a = input(f"Your password should to have: ' {digits} '. Yes or No?: ").strip().lower()
    b = input(f"Your password should to have: ' {lowercase_letters} '. Yes or No?: ").strip().lower()
    c = input(f"Your password should to have: ' {uppercase_letters} '. Yes or No?: ").strip().lower()
    d = input(f"Your password should to have: ' {punctuation} '. Yes or No?: ").strip().lower()

    for i in range(1, menge + 1):
        lange = int(input(f"How many characters should your password number {i} be?: "))
        chairs = ""
        while lange > 0:
            if a in lol and lange > 0:
                chairs += random.choice(digits)
                lange -= 1

            if b in lol and lange > 0:
                chairs += random.choice(lowercase_letters)
                lange -= 1

            if c in lol and lange > 0:
                chairs += random.choice(uppercase_letters)
                lange -= 1

            if d in lol and lange > 0:
                chairs += random.choice(punctuation)
                lange -= 1

            www = list()
            
        for w in chairs:
            www.append(w)

        random.shuffle(www)
        print(f"Your password number {i} is ' {"".join(www)} '.")


password()