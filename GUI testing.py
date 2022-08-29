from tkinter import *
from tkinter import ttk
import pickle

# setting up the main window
main = Tk()
main.title("Henry Simonsen Budgeting Software")
main.geometry('700x500')

# variables
username = 0
password = 0
username2 = 0
password2 = 0
password3 = 0
counter = 2
rows = []
Spending_categories = ["Housing", "Transportation", "Food", "Utilities", "Insurance", "Medical & Healthcare",
                       "Saving, Investing, & Debt Payments", "Personal Spending", "Recreation & Entertainment",
                       "Miscellaneous"]
clicked = StringVar()
clicked.set("Housing")

# Frames
login = ttk.Frame(main)
login.grid(row=0, column=0)
signup = ttk.Frame(main)
signup.grid(row=0, column=0)
signup.grid_forget()
main_menu = ttk.Frame(main)
main_menu.grid(row=0, column=0)
main_menu.grid_forget()
input_page = ttk.Frame(main)
input_page.grid(row=0, column=0)
input_page.grid_forget()
edit_input = ttk.Frame(main)
edit_input.grid(row=0, column=0)
edit_input.grid_forget()
budget = ttk.Frame(main)
budget.grid(row=0, column=0)
budget.grid_forget()
tips = ttk.Frame(main)
tips.grid(row=0, column=0)
tips.grid_forget()


# Go to main menu
def go_main_menu(frame):
    frame.grid_forget()
    main_menu.grid(row=0, column=0)


def go_login(frame):
    frame.grid_forget()
    login.grid(row=0, column=0)


def go_input_page(frame):
    frame.grid_forget()
    input_page.grid(row=0, column=0)


def login_func():
    username_test = username_login_entry.get()
    password_test = password_login_entry.get()
    username_passwords = pickle.load(open("names.dat", "rb"))
    counter_2 = 0
    found = 0
    valid = 0
    check_user = 0
    check_pass = 0
    while found == 0:
        try:
            if username_test == username_passwords[0][counter_2]:
                check_user = counter_2
                found = 1
            else:
                counter_2 += 1
        except:
            found = 2
    if found != 1:
        error_message_login.config(text="WRONG USERNAME!")
    else:
        valid += 1
    counter_2 = 0
    found = 0
    while found == 0:
        try:
            if password_test == username_passwords[1][counter_2]:
                check_pass = counter_2
                found = 1
            else:
                counter_2 += 1
        except:
            found = 2
    if found != 1:
        error_message_login.config(text="WRONG PASSWORD!")
    else:
        valid += 1
    if check_pass == check_user:
        valid += 1
    else:
        error_message_login.config(text="WRONG PASSWORD!")
    if valid == 3:
        login.grid_forget()
        main_menu.grid(row=0, column=0)


def signup_func():
    global username_signup_entry, password_signup_entry, password_signup_entry_check
    login.grid_forget()
    signup.grid(row=0, column=0)


def signup_button_func():
    global username, password, password2
    username = username_signup_entry.get()
    password = password_signup_entry.get()
    password2 = password_signup_entry_check.get()
    if password != password2:
        error_message.config(text="PASSWORDS NEED TO MATCH!                                                                    ")
    elif len(username) > 20:
        error_message.config(text="USERNAME NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
    elif len(username) < 8:
        error_message.config(text="USERNAME NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
    elif len(password) < 8:
        error_message.config(text="PASSWORD NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
    elif len(password) > 20:
        error_message.config(text="PASSWORD NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
    else:
        username_passwords = pickle.load(open("names.dat", "rb"))
        username_passwords[0].append(username)
        username_passwords[1].append(password)
        pickle.dump(username_passwords, open("names.dat", "wb"))
        signup.grid_forget()
        login.grid(row=0, column=0)


def input_page_func():
    main_menu.grid_forget()
    input_page.grid(row=0, column=0)


def budget_func():
    main_menu.grid_forget()
    budget.grid(row=0, column=0)


def tips_func():
    main_menu.grid_forget()
    tips.grid(row=0, column=0)


def add_row():
    global counter
    counter += 1
    items = []
    var = IntVar()
    check = Checkbutton(input_page, variable=var)
    check.val = var
    items.append(check)
    check.grid(row=counter, column=0)
    counter_2 = 0
    while counter_2 != 4:
        entry = Entry(input_page)
        items.append(entry)
        entry.grid(row=counter, column=(counter_2 + 1))
        counter_2 += 1
    rows.append(items)


def delete_row():
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            for integer in row:
                integer.destroy()
            rows.pop(row_s)


def edit_row():
    global num_rows, selected
    num_rows = 0
    selected = []
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            selected.append(1)
            for integer in row:
                num_rows += 0.2
        else:
            selected.append(0)
    num_rows = round(num_rows)
    print(num_rows)
    print(selected)


# login page
Login_title = ttk.Label(login, text="TITLE")
Login_title.grid(row=0, column=3)

username_label = ttk.Label(login, text="USERNAME")
username_label.grid(row=0, column=0)

password_label = ttk.Label(login, text="PASSWORD")
password_label.grid(row=1, column=0)

username_login_entry = ttk.Entry(login)
username_login_entry.grid(row=0, column=1)

password_login_entry = ttk.Entry(login)
password_login_entry.grid(row=1, column=1)

login_button = ttk.Button(login, text="login", width=10, command=lambda: login_func())
login_button.grid(row=3, column=0)

signup_button = ttk.Button(login, text="sign up", width=10, command=lambda: signup_func())
signup_button.grid(row=3, column=1)

error_message_login = ttk.Label(login, text="", foreground="red")
error_message_login.grid(row=2, column=0)

# signup page
signup_title = ttk.Label(signup, text="TITLE")
signup_title.grid(row=0, column=3)

username_label_signup = ttk.Label(signup, text="USERNAME")
username_label_signup.grid(row=0, column=0)

password_label_signup = ttk.Label(signup, text="PASSWORD")
password_label_signup.grid(row=1, column=0)

password_label_signup_check = ttk.Label(signup, text="PASSWORD AGAIN")
password_label_signup_check.grid(row=2, column=0)

username_signup_entry = ttk.Entry(signup)
username_signup_entry.grid(row=0, column=1)

password_signup_entry = ttk.Entry(signup)
password_signup_entry.grid(row=1, column=1)

password_signup_entry_check = ttk.Entry(signup)
password_signup_entry_check.grid(row=2, column=1)

signup_page_button = ttk.Button(signup, text="sign up", width=10, command=lambda: signup_button_func())
signup_page_button.grid(row=4, column=0)

cancel_button = ttk.Button(signup, text="cancel", width=10, command=lambda: go_login(signup))
cancel_button.grid(row=4, column=1)

error_message = ttk.Label(signup, text="", foreground="red")
error_message.grid(row=3, column=0)

# Main menu
main_menu_title = ttk.Label(main_menu, text="TITLE")
main_menu_title.grid(row=0, column=0)

input_page_button = ttk.Button(main_menu, text="input page", width=10, command=lambda: input_page_func())
input_page_button.grid(row=1, column=0)

budget_button = ttk.Button(main_menu, text="budget", width=10, command=lambda: budget_func())
budget_button.grid(row=1, column=1)

tips_button = ttk.Button(main_menu, text="tips", width=10, command=lambda: tips_func())
tips_button.grid(row=1, column=2)

# input page
add_row_button = ttk.Button(input_page, text='Add Row', command=add_row)
add_row_button.grid(row=0, column=0)

delete_row_button = ttk.Button(input_page, text='Delete Row', command=delete_row)
delete_row_button.grid(row=0, column=1)

edit_row_button = ttk.Button(input_page, text="Edit Row", width=10, command=lambda: edit_row())
edit_row_button.grid(row=0, column=2)

cancel_button_input = ttk.Button(input_page, text="cancel", width=10, command=lambda: go_main_menu(input_page))
cancel_button_input.grid(row=0, column=3)

var_0 = StringVar()
entry_0 = Entry(input_page, textvariable=var_0, state='readonly')
var_0.set('Select')
entry_0.grid(row=1, column=0)

var_1 = StringVar()
entry_1 = Entry(input_page, textvariable=var_1, state='readonly')
var_1.set('Spending category')
entry_1.grid(row=1, column=1)

var_2 = StringVar()
entry_2 = Entry(input_page, textvariable=var_2, state='readonly')
var_2.set('Spending type')
entry_2.grid(row=1, column=2)

var_3 = StringVar()
entry_3 = Entry(input_page, textvariable=var_3, state='readonly')
var_3.set('Amount')
entry_3.grid(row=1, column=3)

var_4 = StringVar()
entry_4 = Entry(input_page, textvariable=var_4, state='readonly')
var_4.set('Time per payment')
entry_4.grid(row=1, column=4)

# budget
cancel_button_budget = ttk.Button(budget, text="cancel", width=10, command=lambda: go_main_menu(budget))
cancel_button_budget.grid(row=0, column=0)

# tips
cancel_button_tips = ttk.Button(tips, text="cancel", width=10, command=lambda: go_main_menu(tips))
cancel_button_tips.grid(row=0, column=0)

main.mainloop()

# load file
yes_no = input("do you want to load file?")
if yes_no == "yes":
    show = pickle.load(open("names.dat", "rb"))
    print(show)
else:
    print("ok")

# b = OptionMenu(input_page, clicked, *Spending_categories)
