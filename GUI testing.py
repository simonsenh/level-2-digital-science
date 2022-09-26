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
tip_row = 0
Spending_categories = ["Housing", "Transportation", "Food", "Utilities", "Insurance", "Medical & Healthcare",
                       "Saving, Investing, & Debt Payments", "Personal Spending", "Recreation & Entertainment",
                       "Miscellaneous", "Income"]
clicked = StringVar()
clicked.set("Housing")
time_types = ["Days", "Weeks", "Months", "Years"]
click = StringVar()
click.set("Days")

# manually clear pickle
vari_1 = [["usernames"], ["passwords"]]
vari_2 = []
vari_3 = [["row"], ["category"], ["type"], ["amount"], ["time"]]
vari_6 = [["Housing", 0.196], ["Transportation", 0.17], ["Food", 0.074], ["Utilities", 0.137], ["Insurance", 0.026],
          ["Medical & Healthcare", 0.026],
          ["Personal Spending", 0.045], ["Recreation & Entertainment", 0.051], ["Miscellaneous", 0.05], ["Saving, Investing, & Debt Payments", 0.225]]
vari_7 = [["watch out for housing which is better in the area in which they want to live", "watch out for housing which is cheaper in the area in which they want to live"],
          ["It is important to spend money to visit new places and enjoy yourself", "Instead of making a trip whenever you think of something you need, make a list and only go out when this is necessary."],
          ["Consider buying fresh organic produce to improve the environment and your nutrition", "Growing your own vegetables is a good way of saving money and provide great satisfaction."],
          ["Consider moving to green energy supplier to support the environment", "get quotes from the utility suppliers in your area and change to the one that offers the best deal"],
          ["Insurance is important to prevent a financial catastrophe", "Look for better deals that might ofer you less"],
          ["you are financially able to spend money on healthcare", "Health problems cannot be avoid"],
          ["Its important to spend money on clothing to keep yourself warm and dry throughout the year", "Buying second-hand can save a lot of money, remember to always have money for needs"],
          ["Its important to spend some money to enjoy yourself", "Do I really need it or can I get by without it?"],
          ["You are free to spend money on your own things", "Try to think of something that you don't actually have to do"],
          ["Spending money on yourself now is important for your well being", "Savings are a crucial investment for your future and safety net in case things go wrong"]]
choose = input("Do you want to reset files?")
if choose == "yes":
    pickle.dump(vari_1, open("names.dat", "wb"))
    pickle.dump(vari_2, open("values.dat", "wb"))
    pickle.dump(vari_6, open("ratio.dat", "wb"))
    pickle.dump(vari_7, open("tips.dat", "wb"))

# test pickle
try:
    vari_4 = pickle.load(open("names.dat", "rb"))
except:
    print("error with names")
try:
    vari_5 = pickle.load(open("values.dat", "rb"))
except:
    print("error with values")

# Set error window
error = Toplevel()
error.title("ERROR")
error.withdraw()


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


# Go to main menu
def go_main_menu(frame):
    frame.grid_forget()
    main_menu.grid(row=0, column=0)


# Go to the login page
def go_login(frame):
    frame.grid_forget()
    login.grid(row=0, column=0)


# Display error message
def error_message(error_message_message):
    global error
    try:
        error.deiconify()
    except:
        error = Toplevel()
    error_frame = ttk.Frame(error)
    error_frame.grid(row=0, column=0)
    error_label_error = ttk.Label(error_frame, text=error_message_message, foreground="red")
    error_label_error.grid(row=0, column=0)


# Go to input page and display all rows
def go_input_page(frame):
    global counter, do_it
    do_it = 0
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1 or row[0].val.get() == 0:
            for integer in row:
                integer.destroy()
            rows.pop(row_s)
            counter -= 1
    values_go = pickle.load(open("values.dat", "rb"))
    highest_row = 0
    which_user = which_user_func()
    loop = 0
    counter_3 = 1
    length = len(values_go[which_user][1])
    lists = values_go[which_user][1]
    if length > 1:
        while loop == 0:
            v = lists[counter_3]
            if v > highest_row:
                highest_row = v
            counter_3 += 1
            if counter_3 >= length:
                loop = 1
        counter_3 = 0
        while counter_3 < highest_row:
            do_it = 1
            add_row()
            counter_3 += 1
    frame.grid_forget()
    input_page.grid(row=0, column=0)


# check if password and username is correct and then go to main menu
def login_func():
    global current_username
    username_tests = username_login_entry.get()
    password_test = password_login_entry.get()
    username_passwords = pickle.load(open("names.dat", "rb"))
    counter_3 = 0
    found = 0
    valid = 0
    valid_2 = 0
    check_user = 0
    check_pass = 0
    while found == 0:
        try:
            if username_tests == username_passwords[0][counter_3]:
                check_user = counter_3
                found = 1
            else:
                counter_3 += 1
        except:
            found = 2
    if found == 1:
        valid += 1
    else:
        valid_2 = 1
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
    if found == 1:
        valid += 1
    else:
        valid_2 = 2
    if valid == 2:
        if check_pass == check_user:
            valid += 1
        else:
            valid_2 = 2
    if valid_2 == 1:
        error_message("WRONG USERNAME!")
    elif valid_2 == 2:
        error_message("WRONG PASSWORD!")
    elif valid == 3:
        current_username = username_tests
        login.grid_forget()
        main_menu.grid(row=0, column=0)


# Go to sign up page
def signup_func():
    global username_signup_entry, password_signup_entry, password_signup_entry_check, error_message_message, should_error
    login.grid_forget()
    signup.grid(row=0, column=0)


# Check if the new username and passwords are up to standard then add them to data base
def signup_button_func():
    global username, password, password2
    username_passwords = pickle.load(open("names.dat", "rb"))
    username = username_signup_entry.get()
    password = password_signup_entry.get()
    password2 = password_signup_entry_check.get()
    loop = 0
    counter_3 = 1
    valid = 0
    while loop == 0:
        try:
            if username_passwords[0][counter_3] == username:
                loop = 1
            else:
                counter_3 += 1
        except:
            valid += 1
            loop = 1
    loop = 0
    counter_3 = 1
    while loop == 0:
        try:
            if username_passwords[1][counter_3] == password:
                loop = 1
            else:
                counter_3 += 1
        except:
            valid += 1
            loop = 1
    if valid == 2:
        if password != password2:
            error_message("PASSWORDS NEED TO MATCH!")
        elif len(username) > 20:
            error_message("USERNAME NEEDS TO BE LESS THAN TWENTY CHARACTERS!(security)")
        elif len(username) < 8:
            error_message("USERNAME NEEDS TO BE MORE THAN EIGHT CHARACTERS! (security)")
        elif len(password) < 8:
            error_message("PASSWORD NEEDS TO BE MORE THAN EIGHT CHARACTERS! (security)")
        elif len(password) > 20:
            error_message("PASSWORD NEEDS TO BE LESS THAN TWENTY CHARACTERS!(security)")
        else:
            username_passwords[0].append(username)
            username_passwords[1].append(password)
            pickle.dump(username_passwords, open("names.dat", "wb"))
            add_username = pickle.load(open("values.dat", "rb"))
            vari_3.insert(0, username)
            add_username.append(vari_3)
            pickle.dump(add_username, open("values.dat", "wb"))
            signup.grid_forget()
            login.grid(row=0, column=0)
    else:
        error_message("PASSWORD OR USERNAME HAS BEEN TAKEN!")


# Go to budget page
def budget_func():
    budget.grid(row=0, column=0)
    calculate_budget()


# Display a seperate window with a tip
def tips_func():
    # set up window
    tips_window = Tk()
    tips_window.title("TIP")
    tips_window.geometry('500x100')
    main_menu.grid_forget()
    # set up frame
    tips = ttk.Frame(tips_window)
    tips.grid(row=0, column=0)
    tips_page_label = ttk.Label(tips, text="")
    tips_page_label.grid(row=0, column=0)
    tips_page_label_2 = ttk.Label(tips, text="")
    tips_page_label_2.grid(row=1, column=0)
    # run function
    tips_load = pickle.load(open("tips.dat", "rb"))
    tips_category_load = pickle.load(open("ratio.dat", "rb"))
    counter_3 = 0
    while counter_3 < 10:
        if tip_row == counter_3 + 1:
            if 0 < row_2_list[counter_3] - total_spending_category[counter_3][1]:
                tips_page_label_2.config(text=tips_load[counter_3][1])
            elif row_2_list[counter_3] - total_spending_category[counter_3][1] == 0:
                tips_page_label_2.config(text="This account is perfect")
            else:
                tips_page_label_2.config(text=tips_load[counter_3][0])
        counter_3 += 1
    if 0 < row_2_list[tip_row - 1] - total_spending_category[tip_row - 1][1]:
        y = "OVER"
    else:
        y = "UNDER"
    x = (tips_category_load[(tip_row - 1)][0], y)
    tips_page_label.config(text=x)


# Add a row to the input page and go to edit that row
def add_row():
    global counter, counter_2, selected_row, do_it
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
    if do_it == 0:
        selected_row = counter - 2
        input_page.grid_forget()
        edit_input.grid(row=0, column=0)
    do_it = 0


# Delete a row and the data stored in that row
def delete_row():
    global counter
    selected = []
    selected_pop = []
    delete_variables = pickle.load(open("values.dat", "rb"))
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            selected.insert(0, 1)
            for integer in row:
                integer.destroy()
            rows.pop(row_s)
            counter -= 1
        else:
            selected.insert(0, 0)
    which_user = which_user_func()
    loop = 0
    counter_3 = 0
    while loop == 0:
        try:
            if selected[counter_3] == 1:
                selected_pop.append(counter_3 + 1)
            counter_3 += 1
        except:
            loop = 1
    counter_3 = 1
    a = len(delete_variables[which_user][1])
    while counter_3 < a:
        position = 0
        b = delete_variables[which_user][1][counter_3]
        c = len(selected_pop)
        counter_4 = 0
        while counter_4 < c:
            d = selected_pop[counter_4]
            if b == d:
                position = counter_3
            counter_4 += 1
        if position != 0:
            delete_variables[which_user][1].pop(position)
            delete_variables[which_user][2].pop(position)
            delete_variables[which_user][3].pop(position)
            delete_variables[which_user][4].pop(position)
            delete_variables[which_user][5].pop(position)
        e = len(delete_variables[which_user][1])
        if e == a:
            counter_3 += 1
        else:
            a = len(delete_variables[which_user][1])
    list_1 = delete_variables[which_user][1]
    list_1.pop(0)
    list_2 = []
    list_3 = []
    var_1 = 0
    var_2 = 0
    while var_2 < len(list_1):
        n = 0
        x = max(list_1)
        while n < len(list_1):
            if x == list_1[n]:
                list_2.insert(0, n)
                var_1 = n
            n += 1
        list_1[var_1] = 0
        var_2 += 1
    var_2 = 0
    while var_2 < len(list_2):
        list_3.append(0)
        var_2 += 1
    var_1 = 0
    var_2 = 0
    while var_2 < len(list_2):
        list_3[list_2[var_2]] = var_2 + 1
        var_2 += 1
    list_3.insert(0, "row")
    delete_variables[which_user][1] = list_3
    pickle.dump(delete_variables, open("values.dat", "wb"))


# Go to edit page if the correct amount of boxes have been ticked
def edit_row():
    global num_rows, selected_row
    num_rows = 0
    selected = []
    counter_3 = 0
    for row_s, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            selected.insert(0, 1)
            for _ in row:
                num_rows += 0.2
        else:
            selected.insert(0, 0)
    num_rows = round(num_rows)
    while counter_3 < len(selected):
        if selected[counter_3] == 1:
            selected_row = counter_3 + 1
        counter_3 += 1
    if num_rows > 1:
        error_message("CAN ONLY EDIT ONE ROW AT A TIME!")
    elif num_rows == 0:
        error_message("MUST SELECTED A ROW BEFORE YOU CAN EDIT!")
    else:
        input_page.grid_forget()
        edit_input.grid(row=0, column=0)


# Save inputted data to file if the data is valid
def edit_func():
    global times
    values_load = pickle.load(open("values.dat", "rb"))
    category = clicked.get()
    types = entry_edit_1.get()
    amount = entry_edit_2.get()
    time_category = click.get()
    which_user = which_user_func()
    check = 0
    try:
        amount = float(amount)
    except:
        amount = "s"
    if amount == "s":
        error_message("AMOUNT MUST BE A NUMBER!")
        check = 1
    elif category == "Income":
        if amount < 0:
            check = 1
            error_message("AMOUNT MUST BE POSITIVE!")
    else:
        if amount > 0:
            check = 1
            error_message("AMOUNT MUST BE NEGATIVE!")
    if check == 0:
        counter_3 = 1
        insert = 0
        while counter_3 < len(values_load[which_user][1]):
            if selected_row == values_load[which_user][1][counter_3]:
                insert = counter_3
            counter_3 += 1
        if insert == 0:
            values_load[which_user][1].append(selected_row)
            values_load[which_user][2].append(category)
            values_load[which_user][3].append(types)
            values_load[which_user][4].append(amount)
            values_load[which_user][5].append(time_category)
        else:
            values_load[which_user][1][insert] = selected_row
            values_load[which_user][2][insert] = category
            values_load[which_user][3][insert] = types
            values_load[which_user][4][insert] = amount
            values_load[which_user][5][insert] = time_category
        pickle.dump(values_load, open("values.dat", "wb"))
        go_input_page(edit_input)


# Set the text of each box in the input page based on data in the file
def set_text():
    global counter
    values_text = pickle.load(open("values.dat", "rb"))
    which_user = which_user_func()
    loop = 0
    texts = 0
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


# use financial information in the file to calculate a budget for the user
def calculate_budget():
    global row_2_list, total_spending_category
    income_monthly_label.delete(0, END)
    housing_label.delete(0, END)
    transport_label.delete(0, END)
    food_label.delete(0, END)
    utilities_label.delete(0, END)
    insurance_label.delete(0, END)
    medical_label.delete(0, END)
    savings_debt_label.delete(0, END)
    personal_spending_label.delete(0, END)
    recreation_label.delete(0, END)
    miscellaneous_label.delete(0, END)
    total_budget_label.delete(0, END)
    income_monthly_label_2.delete(0, END)
    housing_label_2.delete(0, END)
    transport_label_2.delete(0, END)
    food_label_2.delete(0, END)
    utilities_label_2.delete(0, END)
    insurance_label_2.delete(0, END)
    medical_label_2.delete(0, END)
    savings_debt_label_2.delete(0, END)
    personal_spending_label_2.delete(0, END)
    recreation_label_2.delete(0, END)
    miscellaneous_label_2.delete(0, END)
    total_budget_label_2.delete(0, END)
    income_monthly_label_3.delete(0, END)
    housing_label_3.delete(0, END)
    transport_label_3.delete(0, END)
    food_label_3.delete(0, END)
    utilities_label_3.delete(0, END)
    insurance_label_3.delete(0, END)
    medical_label_3.delete(0, END)
    savings_debt_label_3.delete(0, END)
    personal_spending_label_3.delete(0, END)
    recreation_label_3.delete(0, END)
    miscellaneous_label_3.delete(0, END)
    total_budget_label_3.delete(0, END)
    calculate = pickle.load(open("values.dat", "rb"))
    spending_ratios = pickle.load(open("ratio.dat", "rb"))
    which_user = which_user_func()
    total_amount = 0
    total_amount_2 = 0
    total_amount_3 = 0
    row_2_list = []
    total_spending_category = []
    counter_3 = 0
    while len(spending_ratios) != counter_3:
        total_spending_category.append([spending_ratios[counter_3][0], 0])
        counter_3 += 1
    total_spending_category.append(["Income", 0])
    counter_3 = 1
    while len(calculate[which_user][4]) > counter_3:
        if calculate[which_user][5][counter_3] == "Days":
            amount_per_month = 356 / 12
        elif calculate[which_user][5][counter_3] == "Weeks":
            amount_per_month = 52 / 12
        elif calculate[which_user][5][counter_3] == "Years":
            amount_per_month = 1 / 12
        else:
            amount_per_month = 1
        amount_per_month = calculate[which_user][4][counter_3] * amount_per_month
        amount_per_month = round(amount_per_month, ndigits=2)
        counter_4 = 0
        while counter_4 < 11:
            if calculate[which_user][2][counter_3] == total_spending_category[counter_4][0]:
                y = total_spending_category[counter_4][1]
                y += amount_per_month
                total_spending_category[counter_4][1] = y
            counter_4 += 1
        total_amount += amount_per_month
        total_amount = round(total_amount, ndigits=2)
        counter_3 += 1
    # row one
    income_monthly_label.insert(END, total_spending_category[10][1])
    housing_label.insert(END, total_spending_category[0][1])
    transport_label.insert(END, total_spending_category[1][1])
    food_label.insert(END, total_spending_category[2][1])
    utilities_label.insert(END, total_spending_category[3][1])
    insurance_label.insert(END, total_spending_category[4][1])
    medical_label.insert(END, total_spending_category[5][1])
    savings_debt_label.insert(END, total_spending_category[6][1])
    personal_spending_label.insert(END, total_spending_category[7][1])
    recreation_label.insert(END, total_spending_category[8][1])
    miscellaneous_label.insert(END, total_spending_category[9][1])
    total_budget_label.insert(END, total_amount)
    # row two
    counter_3 = 0
    while counter_3 < 10:
        total_amount_2 += total_spending_category[10][1] * spending_ratios[counter_3][1]
        y = -(total_spending_category[10][1] * spending_ratios[counter_3][1])
        y = round(y, ndigits=2)
        row_2_list.append(y)
        counter_3 += 1
    total_amount_2 = round(total_amount_2, ndigits=2)
    income_monthly_label_2.insert(END, total_spending_category[10][1])
    housing_label_2.insert(END, row_2_list[0])
    transport_label_2.insert(END, row_2_list[1])
    food_label_2.insert(END, row_2_list[2])
    utilities_label_2.insert(END, row_2_list[3])
    insurance_label_2.insert(END, row_2_list[4])
    medical_label_2.insert(END, row_2_list[5])
    savings_debt_label_2.insert(END, row_2_list[6])
    personal_spending_label_2.insert(END, row_2_list[7])
    recreation_label_2.insert(END, row_2_list[8])
    miscellaneous_label_2.insert(END, row_2_list[9])
    total_budget_label_2.insert(END, total_spending_category[10][1])
    # row three
    counter_3 = 0
    while counter_3 < 10:
        total_amount_3 += (row_2_list[counter_3] - total_spending_category[counter_3][1])
        counter_3 += 1
    total_amount_3 = round(total_amount_3, ndigits=2)
    income_monthly_label_3.insert(END, total_spending_category[10][1])
    housing_label_3.insert(END, row_2_list[0] - total_spending_category[0][1])
    transport_label_3.insert(END, row_2_list[1] - total_spending_category[1][1])
    food_label_3.insert(END, row_2_list[2] - total_spending_category[2][1])
    utilities_label_3.insert(END, row_2_list[3] - total_spending_category[3][1])
    insurance_label_3.insert(END, row_2_list[4] - total_spending_category[4][1])
    medical_label_3.insert(END, (row_2_list[5] - total_spending_category[5][1]))
    savings_debt_label_3.insert(END, row_2_list[6] - total_spending_category[6][1])
    personal_spending_label_3.insert(END, row_2_list[7] - total_spending_category[7][1])
    recreation_label_3.insert(END, row_2_list[8] - total_spending_category[8][1])
    miscellaneous_label_3.insert(END, row_2_list[9] - total_spending_category[9][1])
    total_budget_label_3.insert(END, total_spending_category[10][1])


# Functions for tips
def tip_row_func_1():
    global tip_row
    tip_row = 1
    tips_func()


def tip_row_func_2():
    global tip_row
    tip_row = 2
    tips_func()


def tip_row_func_3():
    global tip_row
    tip_row = 3
    tips_func()


def tip_row_func_4():
    global tip_row
    tip_row = 4
    tips_func()


def tip_row_func_5():
    global tip_row
    tip_row = 5
    tips_func()


def tip_row_func_6():
    global tip_row
    tip_row = 6
    tips_func()


def tip_row_func_7():
    global tip_row
    tip_row = 7
    tips_func()


def tip_row_func_8():
    global tip_row
    tip_row = 8
    tips_func()


def tip_row_func_9():
    global tip_row
    tip_row = 9
    tips_func()


def tip_row_func_10():
    global tip_row
    tip_row = 10
    tips_func()


# Function that finds the current user
def which_user_func():
    which_user_load = pickle.load(open("values.dat", "rb"))
    loop = 0
    counter_3 = 0
    which_user = 0
    while loop == 0:
        if which_user_load[counter_3][0] == current_username:
            which_user = counter_3
            loop = 1
        else:
            counter_3 += 1
    return which_user


# Function that displays in a seperate window instruction for how to use the applicattion
def how_to():
    how_to_window = Tk()
    how_to_window.title("H.S.Budget")
    how_to_window.geometry('600x200')
    how_to_frame = ttk.Frame(how_to_window)
    how_to_frame.grid(row=0, column=0)
    how_to_text = ttk.Label(how_to_frame, text="In order to start using this program you will need to input your finances\n To do this enter the input page\n next add a new row and you will find yourself editing this row\n Next input the category of spending(housing) and particular(rent)\n Then add the amount you are getting or spending ech time period\n Repeat this until all of you expenses are in the system\n Then exit the input page the the main menu and go to the Budgeting page\n The first column is what you are spending per month on a certain category(housing)\n The second column is what you should be spending\n The last column is how much more you need to spend\n If you need any advice on how to reduce or increase spending in a certain category click the show tip button")
    how_to_text.grid(row=0, column=0)


# login page
Login_title = ttk.Label(login, text="H.S.Budgeting")
Login_title.grid(row=0, column=2)

Login_explain = ttk.Label(login, text="Managing your finances for your future")
Login_explain.grid(row=1, column=2)

username_label = ttk.Label(login, text="USERNAME")
username_label.grid(row=3, column=0)

password_label = ttk.Label(login, text="PASSWORD")
password_label.grid(row=4, column=0)

username_login_entry = ttk.Entry(login)
username_login_entry.grid(row=3, column=1)

password_login_entry = ttk.Entry(login)
password_login_entry.grid(row=4, column=1)

login_button = ttk.Button(login, text="login", width=10, command=lambda: login_func())
login_button.grid(row=5, column=0)

signup_button = ttk.Button(login, text="sign up", width=10, command=lambda: signup_func())
signup_button.grid(row=5, column=1)

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

# Main menu
main_menu_title = ttk.Label(main_menu, text="TITLE")
main_menu_title.grid(row=0, column=0)

input_page_button = ttk.Button(main_menu, text="input page", width=10, command=lambda: go_input_page(main_menu))
input_page_button.grid(row=1, column=0)

budget_button = ttk.Button(main_menu, text="budget", width=10, command=lambda: budget_func())
budget_button.grid(row=1, column=1)

how_to_button = ttk.Button(main_menu, text="How to use H.S.Budget", width=20, command=lambda: how_to())
how_to_button.grid(row=1, column=2)

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
var_4.set('Time type')
entry_4.grid(row=1, column=4)

# edit input

username_label_signup = ttk.Label(edit_input, text="Edit row")
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
var_4_edit.set('Time category')
entry_4_edit.grid(row=1, column=3)

option_edit = OptionMenu(edit_input, clicked, *Spending_categories)
option_edit.grid(row=2, column=0)

entry_edit_1 = ttk.Entry(edit_input)
entry_edit_1.grid(row=2, column=1)

entry_edit_2 = ttk.Entry(edit_input)
entry_edit_2.grid(row=2, column=2)

option_edit_2 = OptionMenu(edit_input, click, *time_types)
option_edit_2.grid(row=2, column=3)

# budget
var_14_budget = StringVar()
entry_14_budget = Entry(budget, textvariable=var_14_budget, state='readonly')
var_14_budget.set('INCOME')
entry_14_budget.grid(row=2, column=0)

var_2_budget = StringVar()
entry_2_budget = Entry(budget, textvariable=var_2_budget, state='readonly')
var_2_budget.set('HOUSING')
entry_2_budget.grid(row=3, column=0)

var_3_budget = StringVar()
entry_3_budget = Entry(budget, textvariable=var_3_budget, state='readonly')
var_3_budget.set('TRANSPORT')
entry_3_budget.grid(row=4, column=0)

var_4_budget = StringVar()
entry_4_budget = Entry(budget, textvariable=var_4_budget, state='readonly')
var_4_budget.set('FOOD')
entry_4_budget.grid(row=5, column=0)

var_5_budget = StringVar()
entry_5_budget = Entry(budget, textvariable=var_5_budget, state='readonly')
var_5_budget.set('UTILITIES')
entry_5_budget.grid(row=6, column=0)

var_6_budget = StringVar()
entry_6_budget = Entry(budget, textvariable=var_6_budget, state='readonly')
var_6_budget.set('INSURANCE')
entry_6_budget.grid(row=7, column=0)

var_7_budget = StringVar()
entry_7_budget = Entry(budget, textvariable=var_7_budget, state='readonly')
var_7_budget.set('MEDICAL')
entry_7_budget.grid(row=8, column=0)

var_8_budget = StringVar()
entry_8_budget = Entry(budget, textvariable=var_8_budget, state='readonly')
var_8_budget.set('PERSONAL SPENDING')
entry_8_budget.grid(row=9, column=0)

var_9_budget = StringVar()
entry_9_budget = Entry(budget, textvariable=var_9_budget, state='readonly')
var_9_budget.set('RECREATION')
entry_9_budget.grid(row=10, column=0)

var_10_budget = StringVar()
entry_10_budget = Entry(budget, textvariable=var_10_budget, state='readonly')
var_10_budget.set('MISCELLANEOUS')
entry_10_budget.grid(row=11, column=0)

var_11_budget = StringVar()
entry_11_budget = Entry(budget, textvariable=var_11_budget, state='readonly')
var_11_budget.set('SAVINGS AND DEBT')
entry_11_budget.grid(row=12, column=0)

var_15_budget = StringVar()
entry_15_budget = Entry(budget, textvariable=var_15_budget, state='readonly')
var_15_budget.set('TOTAL')
entry_15_budget.grid(row=13, column=0)

var_1_budget = StringVar()
entry_1_budget = Entry(budget, textvariable=var_1_budget, state='readonly')
var_1_budget.set('Expenses per month')
entry_1_budget.grid(row=1, column=1)

var_12_budget = StringVar()
entry_12_budget = Entry(budget, textvariable=var_12_budget, state='readonly')
var_12_budget.set('Target Spending')
entry_12_budget.grid(row=1, column=2)

var_13_budget = StringVar()
entry_13_budget = Entry(budget, textvariable=var_13_budget, state='readonly')
var_13_budget.set('Underspend(negative)/'
                  'Overspend(positive)')
entry_13_budget.grid(row=1, column=3)

var_16_budget = StringVar()
entry_16_budget = Entry(budget, textvariable=var_16_budget, state='readonly')
var_16_budget.set('Show a Tip')
entry_16_budget.grid(row=1, column=4)

cancel_button_budget = ttk.Button(budget, text="cancel", width=10, command=lambda: go_main_menu(budget))
cancel_button_budget.grid(row=0, column=0)

income_monthly_label = ttk.Entry(budget)
income_monthly_label.grid(row=2, column=1)

housing_label = ttk.Entry(budget)
housing_label.grid(row=3, column=1)

transport_label = ttk.Entry(budget)
transport_label.grid(row=4, column=1)

food_label = ttk.Entry(budget)
food_label.grid(row=5, column=1)

utilities_label = ttk.Entry(budget)
utilities_label.grid(row=6, column=1)

insurance_label = ttk.Entry(budget)
insurance_label.grid(row=7, column=1)

medical_label = ttk.Entry(budget)
medical_label.grid(row=8, column=1)

personal_spending_label = ttk.Entry(budget)
personal_spending_label.grid(row=9, column=1)

recreation_label = ttk.Entry(budget)
recreation_label.grid(row=10, column=1)

miscellaneous_label = ttk.Entry(budget)
miscellaneous_label.grid(row=11, column=1)

savings_debt_label = ttk.Entry(budget)
savings_debt_label.grid(row=12, column=1)

total_budget_label = ttk.Entry(budget)
total_budget_label.grid(row=13, column=1)

income_monthly_label_2 = ttk.Entry(budget)
income_monthly_label_2.grid(row=2, column=2)

housing_label_2 = ttk.Entry(budget)
housing_label_2.grid(row=3, column=2)

transport_label_2 = ttk.Entry(budget)
transport_label_2.grid(row=4, column=2)

food_label_2 = ttk.Entry(budget)
food_label_2.grid(row=5, column=2)

utilities_label_2 = ttk.Entry(budget)
utilities_label_2.grid(row=6, column=2)

insurance_label_2 = ttk.Entry(budget)
insurance_label_2.grid(row=7, column=2)

medical_label_2 = ttk.Entry(budget)
medical_label_2.grid(row=8, column=2)

personal_spending_label_2 = ttk.Entry(budget)
personal_spending_label_2.grid(row=9, column=2)

recreation_label_2 = ttk.Entry(budget)
recreation_label_2.grid(row=10, column=2)

miscellaneous_label_2 = ttk.Entry(budget)
miscellaneous_label_2.grid(row=11, column=2)

savings_debt_label_2 = ttk.Entry(budget)
savings_debt_label_2.grid(row=12, column=2)

total_budget_label_2 = ttk.Entry(budget)
total_budget_label_2.grid(row=13, column=2)

income_monthly_label_3 = ttk.Entry(budget)
income_monthly_label_3.grid(row=2, column=3)

housing_label_3 = ttk.Entry(budget)
housing_label_3.grid(row=3, column=3)

transport_label_3 = ttk.Entry(budget)
transport_label_3.grid(row=4, column=3)

food_label_3 = ttk.Entry(budget)
food_label_3.grid(row=5, column=3)

utilities_label_3 = ttk.Entry(budget)
utilities_label_3.grid(row=6, column=3)

insurance_label_3 = ttk.Entry(budget)
insurance_label_3.grid(row=7, column=3)

medical_label_3 = ttk.Entry(budget)
medical_label_3.grid(row=8, column=3)

personal_spending_label_3 = ttk.Entry(budget)
personal_spending_label_3.grid(row=9, column=3)

recreation_label_3 = ttk.Entry(budget)
recreation_label_3.grid(row=10, column=3)

miscellaneous_label_3 = ttk.Entry(budget)
miscellaneous_label_3.grid(row=11, column=3)

savings_debt_label_3 = ttk.Entry(budget)
savings_debt_label_3.grid(row=12, column=3)

total_budget_label_3 = ttk.Entry(budget)
total_budget_label_3.grid(row=13, column=3)

tip_button_budget_1 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_1())
tip_button_budget_1.grid(row=3, column=4)

tip_button_budget_2 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_2())
tip_button_budget_2.grid(row=4, column=4)

tip_button_budget_3 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_3())
tip_button_budget_3.grid(row=5, column=4)

tip_button_budget_4 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_4())
tip_button_budget_4.grid(row=6, column=4)

tip_button_budget_5 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_5())
tip_button_budget_5.grid(row=7, column=4)

tip_button_budget_6 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_6())
tip_button_budget_6.grid(row=8, column=4)

tip_button_budget_7 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_7())
tip_button_budget_7.grid(row=9, column=4)

tip_button_budget_8 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_8())
tip_button_budget_8.grid(row=10, column=4)

tip_button_budget_9 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_9())
tip_button_budget_9.grid(row=11, column=4)

tip_button_budget_10 = ttk.Button(budget, text="show tip", width=10, command=lambda: tip_row_func_10())
tip_button_budget_10.grid(row=12, column=4)

# run main loop
main.mainloop()

# load file
yes_no = input("do you want to load file?")
if yes_no == "yes":
    show1 = pickle.load(open("names.dat", "rb"))
    show2 = pickle.load(open("values.dat", "rb"))
    show3 = pickle.load(open("ratio.dat", "rb"))
    print(show1, show2, show3)
else:
    print("ok")
