import pickle
yes_no = input("do you want to load file?")
if yes_no == "yes":
    show = pickle.load(open("names.dat", "rb"))
    print(show)

no_yes = input("would you like to add an account")
list = pickle.load(open("names.dat", "rb"))
if no_yes == "yes":
    username = input("what is your username")
    password = input("what is your password")
    list[0].append(username)
    list[1].append(password)

username_login = input("login username:")
password_login = input("login password:")
found = 0
counter = 0
while found == 0:
    try:
        if username_login == list[0][counter]:
            found = 1
        else:
            counter += 1
    except:
        found = 2
if found == 1:
    print("correct username")
else:
    print("incorrect username")
a = 0
b = 0
while a == 0:
    try:
        if password_login == list[1][b]:
            a = 1
        else:
            b += 1
    except:
        a = 2
if a == 1:
    print("correct password")
else:
    print("incorrect password")

pickle.dump(list, open("names.dat", "wb"))
