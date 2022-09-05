from tkinter import *
from tkinter import ttk
import pickle

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
selected_row = 0
username_test = 0
counter_2 = 0
rows = []
Spending_categories = ["Housing", "Transportation", "Food", "Utilities", "Insurance", "Medical & Healthcare",
                       "Saving, Investing, & Debt Payments", "Personal Spending", "Recreation & Entertainment",
                       "Miscellaneous"]
clicked = StringVar()
clicked.set("Housing")

# manually clear pickle
vari_1 = [["usernames"], ["passwords"]]
vari_2 = []
vari_3 = [["row"], ["category"], ["type"], ["amount"], ["time"]]
choose = 0
choose = input("Do you want to reset files?")
if choose == "yes":
    pickle.dump(vari_1, open("names.dat", "wb"))
    pickle.dump(vari_2, open("values.dat", "wb"))

# set pickle titles
try:
    vari_4 = pickle.load(open("names.dat", "rb"))
except:
    print("error with names")
try:
    vari_5 = pickle.load(open("values.dat", "rb"))
except:
    print("error with values")

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
    global counter
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1 or row[0].val.get() == 0:
            for integer in row:
                integer.destroy()
            rows.pop(row_s)
            counter -= 1
    values_go = pickle.load(open("values.dat", "rb"))
    highest_row = 0
    which_user = 0
    counter_3 = 0
    loop = 0
    while loop == 0:
        if values_go[counter_3][0] == current_username:
            which_user = counter_3
            loop = 1
        else:
            counter_3 += 1
    loop = 0
    counter_3 = 1
    length = len(values_go[which_user][1])
    lists = values_go[which_user][1]
    while loop == 0:
        v = lists[counter_3]
        if v > highest_row:
            highest_row = v
        counter_3 += 1
        if counter_3 >= length:
            loop = 1
    counter_3 = 0
    while counter_3 < highest_row:
        add_row()
        counter_3 += 1
    frame.grid_forget()
    input_page.grid(row=0, column=0)


def login_func():
    global current_username
    username_test = username_login_entry.get()
    password_test = password_login_entry.get()
    username_passwords = pickle.load(open("names.dat", "rb"))
    counter_3 = 0
    found = 0
    valid = 0
    check_user = 0
    check_pass = 0
    while found == 0:
        try:
            if username_test == username_passwords[0][counter_3]:
                check_user = counter_3
                found = 1
            else:
                counter_3 += 1
        except:
            found = 2
    if found != 1:
        error_message_login.config(text="WRONG USERNAME!")
    else:
        valid += 1
    counter_3 = 0
    found = 0
    while found == 0:
        try:
            if password_test == username_passwords[1][counter_3]:
                check_pass = counter_3
                found = 1
            else:
                counter_3 += 1
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
        current_username = username_test
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
        error_message_signup.config(
            text="PASSWORDS NEED TO MATCH!                                                                    ")
    elif len(username) > 20:
        error_message_signup.config(text="USERNAME NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
    elif len(username) < 8:
        error_message_signup.config(text="USERNAME NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
    elif len(password) < 8:
        error_message_signup.config(text="PASSWORD NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
    elif len(password) > 20:
        error_message_signup.config(text="PASSWORD NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
    else:
        username_passwords = pickle.load(open("names.dat", "rb"))
        username_passwords[0].append(username)
        username_passwords[1].append(password)
        pickle.dump(username_passwords, open("names.dat", "wb"))
        add_username = pickle.load(open("values.dat", "rb"))
        vari_3.insert(0, username)
        add_username.append(vari_3)
        pickle.dump(add_username, open("values.dat", "wb"))
        signup.grid_forget()
        login.grid(row=0, column=0)


def budget_func():
    main_menu.grid_forget()
    budget.grid(row=0, column=0)


def tips_func():
    main_menu.grid_forget()
    tips.grid(row=0, column=0)


def add_row():
    global counter, counter_2
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
        entry.insert(END, set_text())
        items.append(entry)
        entry.grid(row=counter, column=(counter_2 + 1))
        counter_2 += 1
    rows.append(items)


def delete_row():
    global counter
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            for integer in row:
                integer.destroy()
            rows.pop(row_s)
            counter -= 1
            loop = 0
            while loop == 0:
                loop = 1


def edit_row():
    global num_rows, selected_row
    num_rows = 0
    selected = []
    counter_3 = 0
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            selected.insert(0, 1)
            for integer in row:
                num_rows += 0.2
        else:
            selected.insert(0, 0)
    num_rows = round(num_rows)
    while counter_3 < len(selected):
        if selected[counter_3] == 1:
            selected_row = counter_3 + 1
        counter_3 += 1
    print(selected_row)
    if num_rows > 1:
        error_message_input.config(text="CAN ONLY EDIT ONE ROW AT A TIME!                                 ")
    elif num_rows == 0:
        error_message_input.config(text="MUST SELECTED A ROW BEFORE YOU CAN EDIT!")
    else:
        error_message_input.config(
            text="                                                                                                       ")
        input_page.grid_forget()
        edit_input.grid(row=0, column=0)


def edit_func():
    values_load = pickle.load(open("values.dat", "rb"))
    category = clicked.get()
    types = entry_edit_1.get()
    amount = entry_edit_2.get()
    times = entry_edit_3.get()
    which_user = 0
    counter_3 = 0
    loop = 0
    while loop == 0:
        if values_load[counter_3][0] == current_username:
            which_user = counter_3
            loop = 1
        else:
            counter_3 += 1
    values_load[which_user][1].append(selected_row)
    values_load[which_user][2].append(category)
    values_load[which_user][3].append(types)
    values_load[which_user][4].append(amount)
    values_load[which_user][5].append(times)
    pickle.dump(values_load, open("values.dat", "wb"))
    edit_input.grid_forget()
    input_page.grid(row=0, column=0)


def set_text():
    global counter
    values_text = pickle.load(open("values.dat", "rb"))
    which_user = 0
    counter_3 = 0
    loop = 0
    texts = 0
    while loop == 0:
        if values_text[counter_3][0] == current_username:
            which_user = counter_3
            loop = 1
        else:
            counter_3 += 1
    loop = 0
    counter_3 = 1
    while loop == 0:
        try:
            if values_text[which_user][1][counter_3] == counter - 2:
                texts = values_text[which_user][counter_2 + 2][counter_3]
                loop = 1
            else:
                counter_3 += 1
        except:
            texts = []
            loop = 1
    return texts


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

error_message_signup = ttk.Label(signup, text="", foreground="red")
error_message_signup.grid(row=3, column=0)

# Main menu
main_menu_title = ttk.Label(main_menu, text="TITLE")
main_menu_title.grid(row=0, column=0)

input_page_button = ttk.Button(main_menu, text="input page", width=10, command=lambda: go_input_page(main_menu))
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

error_message_input = ttk.Label(input_page, text="", foreground="red")
error_message_input.grid(row=0, column=5)

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

# edit input

username_label_signup = ttk.Label(edit_input, text="Edit row {}".format(selected_row + 1))
username_label_signup.grid(row=0, column=0)

cancel_button_edit = ttk.Button(edit_input, text="cancel", width=10, command=lambda: go_input_page(edit_input))
cancel_button_edit.grid(row=0, column=1)

done_button_edit = ttk.Button(edit_input, text="done", width=10, command=lambda: edit_func())
done_button_edit.grid(row=0, column=2)

var_1_edit = StringVar()
entry_1_edit = Entry(edit_input, textvariable=var_1_edit, state='readonly')
var_1_edit.set('Spending category')
entry_1_edit.grid(row=1, column=0)

var_2_edit = StringVar()
entry_2_edit = Entry(edit_input, textvariable=var_2_edit, state='readonly')
var_2_edit.set('Spending type')
entry_2_edit.grid(row=1, column=1)

var_3_edit = StringVar()
entry_3_edit = Entry(edit_input, textvariable=var_3_edit, state='readonly')
var_3_edit.set('Amount')
entry_3_edit.grid(row=1, column=2)

var_4_edit = StringVar()
entry_4_edit = Entry(edit_input, textvariable=var_4_edit, state='readonly')
var_4_edit.set('Time per payment')
entry_4_edit.grid(row=1, column=3)

option_edit = OptionMenu(edit_input, clicked, *Spending_categories)
option_edit.grid(row=2, column=0)

entry_edit_1 = ttk.Entry(edit_input)
entry_edit_1.grid(row=2, column=1)

entry_edit_2 = ttk.Entry(edit_input)
entry_edit_2.grid(row=2, column=2)

entry_edit_3 = ttk.Entry(edit_input)
entry_edit_3.grid(row=2, column=3)

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
    show1 = pickle.load(open("names.dat", "rb"))
    show2 = pickle.load(open("values.dat", "rb"))
    print(show1, show2)
else:
    print("ok")

# b = OptionMenu(input_page, clicked, *Spending_categories)
