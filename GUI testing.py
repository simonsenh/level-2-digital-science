import tkinter as tk
from tkinter import *

login_page = Tk()
login_page.title("Login page")
login_page_var = 0
username = 0
password = 0

message_label = Label(login_page, text="Login page", wraplength=500)
message_label.pack()


def login():
    def check():
        Username = usernames.get()
        Password = passwords.get()
        error_message = tk.Label(Login, text="", fg="red")
        error_message.grid(row=3, column=1)
        if Password != password:
            error_message.config(text="INCORRECT PASSWORD")
        elif Username != username:
            error_message.config(text="INCORRECT USERNAME")
        else:
            error_message.config(
                text="                                                                                ")
            Login.destroy()
            login_page.destroy()
            main_menu = tk.Tk()
            main_menu.title("MAIN MENU")

            def get_data():
                def destroy():
                    Login.destroy()

                def ok():
                    saving_try = savings.get()
                    month_income_try = month_incomes.get()
                    month_expense_try = month_expenses.get()
                    time_try = times.get()
                    loan_try = loans.get()
                    loan_due_try = loan_dues.get()
                    try:
                        float(saving_try + month_income_try + month_expense_try + time_try + loan_try + loan_due_try)
                    except Exception:
                        wrong_message = tk.Label(data, text="INPUT NUMBER!", fg="red")
                        wrong_message.grid(row=6, column=1)
                    else:
                        global saving
                        saving = saving_try
                        global month_income
                        month_income = month_income_try
                        global month_expense
                        month_expense = month_expense_try
                        global time
                        time = time_try
                        global loan
                        loan = loan_try
                        global loan_due
                        loan_due = loan_due_try
                        global gross_month
                        gross_month = float(month_income) - float(month_expense)
                        global money_after_loan
                        money_after_loan = (float(saving) - float(loan)) + (float(gross_month) * float(loan_due))
                        global final_money
                        final_money = float(time) * float(gross_month) - float(loan) + float(saving)
                        print(saving, month_income, month_expense, time, loan, loan_due)
                        data.destroy()

                data = tk.Tk()
                data.title("Input your financial information")
                tk.Label(data, text="savings").grid(row=0)
                tk.Label(data, text="month_income").grid(row=1)
                tk.Label(data, text="month_expenses").grid(row=2)
                tk.Label(data, text="time").grid(row=3)
                tk.Label(data, text="loan").grid(row=4)
                tk.Label(data, text="loan_due").grid(row=5)
                savings = tk.Entry(data)
                month_incomes = tk.Entry(data)
                month_expenses = tk.Entry(data)
                times = tk.Entry(data)
                loans = tk.Entry(data)
                loan_dues = tk.Entry(data)
                savings.grid(row=0, column=1)
                month_incomes.grid(row=1, column=1)
                month_expenses.grid(row=2, column=1)
                times.grid(row=3, column=1)
                loans.grid(row=4, column=1)
                loan_dues.grid(row=5, column=1)
                e = Button(data, text="ok", command=ok)
                e.grid(row=6, column=2)
                f = Button(data, text="cancel", command=destroy)
                f.grid(row=6, column=3)

            def stat():
                stats = tk.Tk()
                message_1 = tk.Label(stats, text="You are making {}$ a month".format(gross_month))
                message_1.grid(row=1, column=1)
                message_2 = tk.Label(stats, text="After you pay off your loan you will have {}$".format(money_after_loan))
                message_2.grid(row=2, column=1)

            def graph():
                print("graph")

            def tips():
                print("tips")

            get_data = Button(main_menu, text="Input data", command=get_data, width=10)
            get_data.pack()
            stat = Button(main_menu, text="Show stats", command=stat, width=10)
            stat.pack()
            graph = Button(main_menu, text="Show graphs", command=graph, width=10)
            graph.pack()
            tips = Button(main_menu, text="Show tips", command=tips, width=10)
            tips.pack()

    def delete():
        Login.destroy()

    Login = tk.Tk()
    Login.title("login")
    tk.Label(Login, text="Username").grid(row=0)
    tk.Label(Login, text="Password").grid(row=1)
    usernames = tk.Entry(Login)
    passwords = tk.Entry(Login)
    usernames.grid(row=0, column=1)
    passwords.grid(row=1, column=1)
    c = Button(Login, text="ok", command=check)
    c.grid(row=4, column=2)
    d = Button(Login, text="cancel", command=delete)
    d.grid(row=4, column=3)


login_page.geometry("200x100")
a = Button(login_page, text="login", command=login, width=6)
a.pack()


def signup():
    def user_info():
        Username = usernames.get()
        Password = passwords.get()
        Confirm_Password = confirm_passwords.get()
        error_message = tk.Label(signup_page, text="", fg="red")
        error_message.grid(row=3, column=1)
        if len(Username) > 20:
            error_message.config(text="USERNAME NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
        elif len(Username) < 8:
            error_message.config(text="USERNAME NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
        elif len(Password) < 8:
            error_message.config(text="PASSWORD NEEDS TO BE MORE THAN EIGHT CHARACTERS! ")
        elif len(Password) > 20:
            error_message.config(text="PASSWORD NEEDS TO BE LESS THAN TWENTY CHARACTERS!")
        elif Password != Confirm_Password:
            error_message.config(text="YOUR PASSWORD'S DONT MATCH!                                             ")
        else:
            error_message.config(
                text="                                                                                                           ")
            global username
            username = Username
            global password
            password = Password
            signup_page.destroy()

    def delete():
        signup_page.destroy()

    signup_page = tk.Tk()
    signup_page.title("sign up page")
    tk.Label(signup_page, text="Username").grid(row=0)
    tk.Label(signup_page, text="Password").grid(row=1)
    tk.Label(signup_page, text="Confirm Password").grid(row=2)
    usernames = tk.Entry(signup_page)
    passwords = tk.Entry(signup_page)
    confirm_passwords = tk.Entry(signup_page)
    usernames.grid(row=0, column=1)
    passwords.grid(row=1, column=1)
    confirm_passwords.grid(row=2, column=1)
    c = Button(signup_page, text="ok", command=user_info)
    c.grid(row=4, column=2)
    d = Button(signup_page, text="cancel", command=delete)
    d.grid(row=4, column=3)


login_page.geometry("200x100")
b = Button(login_page, text="Sign up", command=signup, width=6)
b.pack()

login_page.mainloop()
print(username, password)
