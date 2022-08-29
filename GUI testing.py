from tkinter import *
from tkinter import ttk

# setting up the main window
main = Tk()
main.title("Henry Simonsen Budgeting Software")
main.geometry('500x500')

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


def login_func():
    global username, password
    valid = True
    username_test = username_login_entry.get()
    password_test = password_login_entry.get()
    if username_test != username:
        valid = False
    elif password_test != password:
        valid = False
    elif valid is True:
        login.grid_forget()
        main_menu.grid(row=0, column=0)


def signup_func():
    global username_signup_entry, password_signup_entry, password_signup_entry_check
    login.grid_forget()
    signup.grid(row=0, column=0)


def signup_button_func():
    global username2, password2, password3
    valid = True
    username2 = username_signup_entry.get()
    password2 = password_signup_entry.get()
    password3 = password_signup_entry_check.get()
    if password2 != password3:
        error_message.config(text="PASSWORDS NEED TO MATCH!                                                                    ")
        valid = False
    elif len(username2) > 20:
        error_message.config(text="USERNAME NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
        valid = False
    elif len(username2) < 8:
        error_message.config(text="USERNAME NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
        valid = False
    elif len(password2) < 8:
        error_message.config(text="PASSWORD NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
        valid = False
    elif len(password2) > 20:
        error_message.config(text="PASSWORD NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
        valid = False
    elif valid is True:
        username2 = username
        password2 = password
        signup.grid_forget()


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
    c = 0
    while c != 4:
        if c == 0:
            b = OptionMenu(input_page, clicked, *Spending_categories)
        else:
            b = Entry(input_page)
        items.append(b)
        b.grid(row=counter, column=(c + 1))
        c += 1
    rows.append(items)


def delete_row():
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            for i in row:
                i.destroy()
            rows.pop(row_s)


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
login_button.grid(row=2, column=0)

signup_button = ttk.Button(login, text="sign up", width=10, command=lambda: signup_func())
signup_button.grid(row=2, column=1)

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
cancel_button_input = ttk.Button(input_page, text="cancel", width=10, command=lambda: go_main_menu(input_page))
cancel_button_input.grid(row=0, column=0)

add_row_button = ttk.Button(input_page, text='Add Row', command=add_row)
add_row_button.grid(row=0, column=0)

delete_row_button = ttk.Button(input_page, text='Delete Row', command=delete_row)
delete_row_button.grid(row=0, column=1)

v0 = StringVar()
e0 = Entry(input_page, textvariable=v0, state='readonly')
v0.set('Select')
e0.grid(row=1, column=0)

v1 = StringVar()
e1 = Entry(input_page, textvariable=v1, state='readonly')
v1.set('Spending category')
e1.grid(row=1, column=1)

v2 = StringVar()
e2 = Entry(input_page, textvariable=v2, state='readonly')
v2.set('Spending type')
e2.grid(row=1, column=2)

v3 = StringVar()
e3 = Entry(input_page, textvariable=v3, state='readonly')
v3.set('Amount')
e3.grid(row=1, column=3)

v4 = StringVar()
e4 = Entry(input_page, textvariable=v4, state='readonly')
v4.set('Time per payment')
e4.grid(row=1, column=4)

# budget
cancel_button_budget = ttk.Button(budget, text="cancel", width=10, command=lambda: go_main_menu(budget))
cancel_button_budget.grid(row=0, column=0)

# tips
cancel_button_tips = ttk.Button(tips, text="cancel", width=10, command=lambda: go_main_menu(tips))
cancel_button_tips.grid(row=0, column=0)

main.mainloop()
