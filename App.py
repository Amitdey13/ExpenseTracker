from Database import Database
from tkinter import *
from PIL import ImageTk
import datetime


# Expense Tracker
class ExpenseTracker:

    def __init__(self):
        # connect with database
        self.db = Database()

        # user
        self.Id = 0
        self.name = ""
        self.total_expense = 0

        # load gui
        self.load_gui("login")

    def load_gui(self, state):
        self.root = Tk()
        self.root.geometry("500x700+950+50")
        self.root.resizable(False, False)
        self.logo = PhotoImage(file="images/icon.png")
        self.root.iconphoto(False, self.logo)
        self.root.title("Expense Tracker")

        self.switch_frame(state)

        self.root.mainloop()

    def switch_frame(self, state, data=()):
        self.main_frame = Frame(self.root, bg="#00ff91")
        self.main_frame.place(x=0, y=0, height=700, width=500)
        if state == "login" or state == "signup":
            self.login_signup_gui(state)
        elif state == "login-error" or state == "signup-error":
            self.error_gui(state)
        elif state == "homepage":
            self.homepage()
        elif state == "addexpense" or state == "editexpense":
            self.add_edit_expense_gui(state, data)
        elif state == "showexpense":
            self.show_expense(data)

    def login_signup_gui(self, state):
        self.bg_clip = Label(self.main_frame, bg="#00ff91").place(x=0, y=0)
        if state == "login":
            self.login_frame = Frame(self.main_frame, bg="#06060f")
            self.login_frame.place(x=60, y=70, height=560, width=380)
            self.label1 = Label(self.login_frame, text="Login Here", font=("Impact", "28", "bold"), bg="#06060f", fg="#ffffff").place(x=30, y=95)
            self.Email = Label(self.login_frame, text="Enter Email*:", font=("Goudy old style", "15", "bold"), bg="#06060f", fg="#ffffff").place(x=30, y=165)
            self.email_input = Entry(self.login_frame, font=("Times new roman", "15"), insertbackground="#ffffff", bd=0, fg="#ffffff", bg="#06060f")
            self.email_input.place(x=33, y=200, width=280, height=30)
            self.label = Label(self.login_frame, text="", font=("Impact", "28", "bold"), bg="#ffffff").place(x=33, y=230, height=1, width=280)

            self.Password = Label(self.login_frame, text="Enter Password*:", font=("Goudy old style", "15", "bold"), bg="#06060f", fg="#ffffff").place(x=30, y=255)
            self.password_input = Entry(self.login_frame, show="*", font=("Times new roman", "15"), insertbackground="#ffffff", bd=0, bg="#06060f", fg="#ffffff")
            self.password_input.place(x=33, y=287, width=280, height=30)
            self.label = Label(self.login_frame, text="", font=("Impact", "28", "bold"), bg="#ffffff").place(x=33,
                                                                                                              y=317,
                                                                                                              height=1,
                                                                                                              width=280)
            self.login_btn = Button(self.login_frame, bd=0, text="Login", font=("Roboto", "13", "bold"), bg="#ffffff", fg="#06060f", command=lambda :self.login_signup("login")).place(x=34, y=367, width=100, height=35)
            self.btn = Button(self.login_frame, bd=0, text="Not a member? Register here.", font=("Times", "10", "bold"), bg="#06060f",
                          fg="#ffffff", command=lambda: self.switch_frame("signup")).place(x=34, y=407)

        elif state == "signup":
            self.login_frame = Frame(self.main_frame, bg="#06060f")
            self.login_frame.place(x=60, y=70, height=560, width=380)

            self.label1 = Label(self.login_frame, text="Signup Here", font=("Impact", "28", "bold"), bg="#06060f",
                                fg="#ffffff").place(x=30, y=95)

            self.Name = Label(self.login_frame, text="Enter Name*:", font=("Goudy old style", "15", "bold"),
                               bg="#06060f", fg="#ffffff").place(x=30, y=165)
            self.name_input = Entry(self.login_frame, font=("Times new roman", "15"), insertbackground="#ffffff", bd=0, bg="#06060f", fg="#ffffff")
            self.name_input.place(x=33, y=200, width=280, height=30)
            self.label = Label(self.login_frame, text="", font=("Impact", "28", "bold"), bg="#ffffff").place(x=33,
                                                                                                             y=230,
                                                                                                             height=1,
                                                                                                             width=280)

            self.Email = Label(self.login_frame, text="Enter Email*:", font=("Goudy old style", "15", "bold"),
                               bg="#06060f", fg="#ffffff").place(x=30, y=245)
            self.email_input = Entry(self.login_frame, font=("Times new roman", "15"), insertbackground="#ffffff", bd=0, bg="#06060f", fg="#ffffff")
            self.email_input.place(x=33, y=280, width=280, height=30)
            self.label = Label(self.login_frame, text="", font=("Impact", "28", "bold"), bg="#ffffff").place(x=33,
                                                                                                             y=310,
                                                                                                             height=1,
                                                                                                             width=280)

            self.Password = Label(self.login_frame, text="Enter Password*:", font=("Goudy old style", "15", "bold"),
                                  bg="#06060f", fg="#ffffff").place(x=30, y=325)
            self.password_input = Entry(self.login_frame, show="*", font=("Times new roman", "15"), insertbackground="#ffffff", bd=0, bg="#06060f", fg="#ffffff")
            self.password_input.place(x=33, y=360, width=280, height=30)
            self.label = Label(self.login_frame, text="", font=("Impact", "28", "bold"), bg="#ffffff").place(x=33,
                                                                                                             y=390,
                                                                                                             height=1,
                                                                                                             width=280)
            self.signup_btn = Button(self.login_frame, bd=0, text="Signup", font=("Roboto", "13", "bold"), bg="#ffffff",
                              fg="#06060f", command=lambda:self.login_signup("signup")).place(x=34, y=417, width=100, height=35)
            self.btn = Button(self.login_frame, bd=0, text="Already registered? Login here.", font=("Times", "10", "bold"),
                              bg="#06060f",
                              fg="#ffffff", command=lambda: self.switch_frame("login")).place(x=34, y=457)

    def error_gui(self, state):
        self.bg = ImageTk.PhotoImage(file="images/error.jpg")
        self.bg_clip = Label(self.main_frame, image=self.bg).place(x=0, y=0)
        self.login_frame = Frame(self.main_frame, bg="#06060f")
        self.login_frame.place(x=60, y=70, height=560, width=380)

        if state == "login-error":
            self.label1 = Label(self.login_frame, text="Login Error", font=("Impact", "28", "bold"), bg="#06060f",
                                fg="#ffffff").place(x=30, y=95)

            self.err = Label(self.login_frame, text="Incorrect email or password!", font=("Goudy old style", "15", "bold"),
                               bg="#06060f", fg="#ffffff").place(x=30, y=165)
            self.try_again_btn = Button(self.login_frame, bd=0, text="Try again", font=("Roboto", "10", "bold"), bg="#ffffff",
                                    fg="#06060f", command=lambda: self.switch_frame("login")).place(x=34, y=327,
                                                                                                    width=100,
                                                                                                    height=30)
        else:
            self.label1 = Label(self.login_frame, text="Signup Error", font=("Impact", "28", "bold"), bg="#06060f",
                                fg="#ffffff").place(x=30, y=95)

            self.err = Label(self.login_frame, text="An account already registered",
                               font=("Goudy old style", "15", "bold"),
                               bg="#06060f", fg="#ffffff").place(x=30, y=165)
            self.err = Label(self.login_frame, text="with this email.",
                               font=("Goudy old style", "15", "bold"),
                               bg="#06060f", fg="#ffffff").place(x=30, y=200)
            self.login_btn = Button(self.login_frame, bd=0, text="Login", font=("Roboto", "10", "bold"),
                                    bg="#ffffff",
                                    fg="#06060f", command=lambda: self.switch_frame("login")).place(x=34, y=327,
                                                                                                    width=100,
                                                                                                    height=30)
            self.btn = Button(self.login_frame, bd=0, text="Register with another email.",
                              font=("Times", "10", "bold"),
                              bg="#06060f",
                              fg="#ffffff", command=lambda: self.switch_frame("signup")).place(x=34, y=407)

    def login_signup(self, state):
        if state == "login":
            email = self.email_input.get()
            password = self.password_input.get()
            if email != "" and password != "":
                data = self.db.login_signup(state, "", email, password)
                if data == []:
                    self.switch_frame("login-error")
                else:
                    self.Id = data[0][0]
                    self.name = data[0][1]
                    self.switch_frame("homepage")
        else:
            name = self.name_input.get()
            email = self.email_input.get()
            password = self.password_input.get()
            if name != "" and email != "" and password != "":
                data = self.db.login_signup(state, name, email, password)
                if data == 1:
                    self.Id = self.db.get_id(email)[0][0]
                    self.name = name
                    self.switch_frame("homepage")
                else:
                    self.switch_frame("signup-error")

    def homepage(self):
        self.frame = Frame(self.main_frame, bg="#00ff91").place(x=0, y=0, height=700, width=500)
        self.total_expense = self.db.total_expense(self.Id)[0][0]
        self.avatar = PhotoImage(file="images/avatar.png")
        self.ava = Button(self.frame, image=self.avatar, bd=0, fg="#000314", bg="#00ff91").place(x=30, y=20)
        self.label1 = Label(self.frame, text=self.name, font=("Gill Sans MT", 14, "bold"), fg="#000314", bg="#00ff91").place(x=65, y=20)
        self.logout = Button(self.frame, text="logout", bd=0, font=("Gill Sans MT", 13), fg="#000314", bg="#00ff91", command=lambda:self.switch_frame("login")).place(x=400, y=20)
        self.show_total_expense = Label(self.frame, text=u"\u20B9" + str(self.total_expense), font=("Comic Sans MS", 45, "bold"), fg="#000314",
                            bg="#00ff91").place(relx=0.49, rely=0.2, anchor=CENTER)
        self.label3 = Label(self.frame, text="Total expense", font=("Gill Sans MT", 12, "bold"), fg="#000314",
                            bg="#00ff91").place(relx=0.51, rely=0.26, anchor=CENTER)
        self.add = PhotoImage(file="images/add_expense.png")
        self.label4 = Button(self.frame, image=self.add, bd=0, fg="#000314", bg="#00ff91",command=lambda:self.switch_frame("addexpense")).place(relx=0.5, rely=0.35, anchor=CENTER)
        self.label5 = Label(self.frame, text="Expenses", font=("Gill Sans MT", 14, "bold"), fg="#000314", bg="#00ff91").place(x=42, y=280)
        self.label5 = Label(self.frame, bg="#000314").place(x=45, y=310, width=416, height=2)
        self.expenses = LabelFrame(self.frame, bd=0, bg="#00ff91")
        self.scrollbar = Scrollbar(self.expenses, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.expenses.place(x=0, y=313, height=430, width=500)
        expenses = self.db.expenses(self.Id)
        self.expense = PhotoImage(file="images/expense.png")
        self.edit = PhotoImage(file="images/edit.png")
        self.delete = PhotoImage(file="images/delete.png")
        self.expense_list = Canvas(self.expenses, yscrollcommand=self.scrollbar.set, bg="#00ff91", bd=0)
        self.expenses_frame = Frame(self.expense_list, bg="#00ff91", bd=0, width=440)
        top = 0
        for i in expenses[::-1]:
            self.expense_gui(top, i)
            top += 1
        self.expense_list.create_window(50, 0, window=self.expenses_frame)
        self.expense_list.update_idletasks()
        self.expense_list.pack(fill=Y, expand=TRUE)
        self.scrollbar.config(command=self.expense_list.yview)
        self.expense_list.configure(scrollregion=self.expense_list.bbox("all"))

    def datetime_stamp(self):

        x = datetime.datetime.now()
        day = x.strftime("%d")
        month = x.strftime("%m")
        year = x.strftime("%Y")
        time = x.strftime("%X")

        stamp = str(day) + '-' + str(month) + '-' + str(year) + ' ' + str(time)
        return stamp

    def add_edit_expense_gui(self, state, data):
        self.frame = Frame(self.main_frame, bg="#00ff91").place(x=0, y=0, height=700, width=500)
        self.avatar = PhotoImage(file="images/avatar.png")
        self.ava = Button(self.frame, image=self.avatar, bd=0, fg="#000314", bg="#00ff91").place(x=30, y=20)
        self.label1 = Label(self.frame, text=self.name, font=("Gill Sans MT", 14, "bold"), fg="#000314",
                            bg="#00ff91").place(x=65, y=20)
        self.home_icon = PhotoImage(file="images/home.png")
        self.home = Button(self.frame, image=self.home_icon, bd=0, fg="#000314", bg="#00ff91", command=lambda:self.switch_frame("homepage") ).place(x=410, y=20)

        if state == "addexpense":
            self.label1 = Label(self.frame, text="Add expense", font=("Gill Sans MT", "28", "bold"), bg="#00ff91",
                                fg="#000314").place(x=50, y=95)
            self.Expense_type = Label(self.frame, text="Expense type*:", font=("Goudy old style", "15", "bold"),
                              bg="#00ff91", fg="#000314").place(x=60, y=165)
            self.expense_type = Entry(self.frame, font=("Times new roman", "15"), insertbackground="#000314", bd=0,
                                    bg="#00ff91", fg="#000314")
            self.expense_type.place(x=63, y=200, width=280, height=30)
            self.label = Label(self.frame, text="", font=("Impact", "28", "bold"), bg="#000314").place(x=63,
                                                                                                             y=230,
                                                                                                             height=1,
                                                                                                             width=280)
            self.amount = Label(self.frame, text="Amount*:", font=("Goudy old style", "15", "bold"),
                               bg="#00ff91", fg="#000314").place(x=60, y=245)
            self.amount = Entry(self.frame, font=("Times new roman", "15"), insertbackground="#000314", bd=0,
                                     bg="#00ff91", fg="#000314")
            self.amount.place(x=63, y=280, width=280, height=30)
            self.label = Label(self.frame, text="", font=("Impact", "28", "bold"), bg="#000314").place(x=63,  y=310, height=1,  width=280)

            self.add_expense = Button(self.frame, bd=0, text="Add expense", font=("Roboto", "13", "bold"), bg="#000314",
                                     fg="#ffffff", command=lambda: self.add_edit_expense(state)).place(x=64, y=417, width=120, height=35)

        else:
            self.label1 = Label(self.frame, text="Edit expense", font=("Gill Sans MT", "28", "bold"), bg="#00ff91",
                                fg="#000314").place(x=50, y=95)

            self.Expense_type = Label(self.frame, text="Expense type*:", font=("Goudy old style", "15", "bold"),
                                      bg="#00ff91", fg="#000314").place(x=60, y=165)
            self.expense_type = Entry(self.frame, font=("Times new roman", "15"), insertbackground="#000314", bd=0,
                                      bg="#00ff91", fg="#000314")
            self.expense_type.insert(0, data[2])
            self.expense_type.place(x=63, y=200, width=280, height=30)
            self.label = Label(self.frame, text="", font=("Impact", "28", "bold"), bg="#000314").place(x=63,
                                                                                                       y=230,
                                                                                                       height=1,
                                                                                                       width=280)

            self.amount = Label(self.frame, text="Amount*:", font=("Goudy old style", "15", "bold"),
                                bg="#00ff91", fg="#000314").place(x=60, y=245)
            self.amount = Entry(self.frame, font=("Times new roman", "15"), insertbackground="#000314", bd=0,
                                bg="#00ff91", fg="#000314")
            self.amount.insert(0, data[3])
            self.amount.place(x=63, y=280, width=280, height=30)
            self.label = Label(self.frame, text="", font=("Impact", "28", "bold"), bg="#000314").place(x=63, y=310,
                                                                                                       height=1,
                                                                                                       width=280)

            self.edit_expense = Button(self.frame, bd=0, text="Save changes", font=("Roboto", "13", "bold"), bg="#000314",
                                      fg="#ffffff", command=lambda: self.add_edit_expense(state, data[0], data[3])).place(x=64, y=417,
                                                                                                        width=120,
                                                                                                        height=35)

    def add_edit_expense(self, state, expense_id = 0, preamount = 0):
        if state == "addexpense":
            expense_type = self.expense_type.get()
            amount = self.amount.get()
            date = self.datetime_stamp()
            if expense_type != "" and amount != "":
                success_data = self.db.add_edit_expense(state, self.Id, expense_type, amount, date)
                data = self.db.update_expense(self.Id, self.total_expense+int(amount))
                if success_data == 1:
                    self.switch_frame("homepage")
        else:
            expense_type = self.expense_type.get()
            amount = self.amount.get()
            if expense_type != "" and amount != "":
                success_data = self.db.add_edit_expense(state, self.Id, expense_type, amount, expense_id)
                data = self.db.update_expense(self.Id, self.total_expense - int(preamount) + int(amount))
                if success_data == 1:
                    self.switch_frame("homepage")

    def expense_gui(self, row, data):
        self.expense_img_label = Label(self.expenses_frame, image=self.expense, fg="#000314", width=35, height=40, bg="#00ff91").grid(column = 0, row=row, sticky=W)
        self.expense_type_label = Button(self.expenses_frame, justify=LEFT, font=("Times", 13, "bold"), text=data[2], bd=0, fg="#000314", bg="#00ff91", command=lambda :self.switch_frame("showexpense", data)).grid(column = 1, row=row)
        self.expense_label = Label(self.expenses_frame, font=("Times", 12, "bold"), width=23, text=data[3], fg="#000314", bg="#00ff91").grid(column = 2, row=row)
        self.edit_btn = Button(self.expenses_frame, font=("Times", 12, "bold"), width=35, image=self.edit, bd=0, fg="#000314",
                                   bg="#00ff91", command=lambda :self.switch_frame("editexpense", data)).grid(column = 3, row=row)
        self.delete_btn = Button(self.expenses_frame, justify=RIGHT, font=("Times", 12, "bold"), width=35, image=self.delete, bd=0, fg="#000314",
                               bg="#00ff91", command=lambda:self.delete_expense(data)).grid(column = 6, row=row)

    def show_expense(self, data):
        self.frame = Frame(self.main_frame, bg="#00ff91").place(x=0, y=0, height=700, width=500)
        self.avatar = PhotoImage(file="images/avatar.png")
        self.ava = Button(self.frame, image=self.avatar, bd=0, fg="#000314", bg="#00ff91").place(x=30, y=20)
        self.label1 = Label(self.frame, text=self.name, font=("Gill Sans MT", 14, "bold"), fg="#000314",
                            bg="#00ff91").place(x=65, y=20)
        self.home_icon = PhotoImage(file="images/home.png")
        self.home = Button(self.frame, image=self.home_icon, bd=0, fg="#000314", bg="#00ff91",
                           command=lambda: self.switch_frame("homepage")).place(x=410, y=20)
        self.expense_icon = PhotoImage(file="images/expense1.png")
        self.expense_img_label = Label(self.frame, font=("Times", 10, "bold"), image=self.expense_icon, fg="#000314",
                                       bg="#00ff91").place(x=43, y=115)
        self.label1 = Label(self.frame, text='Expense details', font=("Gill Sans MT", 20, "bold"), bg="#00ff91",
                            fg="#000314").place(x=80, y=115)
        self.edit_btn = Button(self.frame, font=("Times", 12, "bold"), image=self.edit, bd=0, fg="#000314",
                               bg="#00ff91", command=lambda: self.switch_frame("editexpense", data)).place(x=360, y=127)
        self.delete_btn = Button(self.frame, font=("Times", 12, "bold"), image=self.delete, bd=0, fg="#000314",
                                 bg="#00ff91", command=lambda: self.delete_expense(data)).place(x=410, y=127)
        self.expense_type_label = Label(self.frame, text='Expense type:', font=("Gill Sans MT", 13), bg="#00ff91",
                            fg="#000314").place(x=80, y=175)
        self.expense_type_value = Label(self.frame, text=data[2], font=("Gill Sans MT", 17),
                                        bg="#00ff91",
                                        fg="#000314").place(x=80, y=205)
        self.amount_label = Label(self.frame, text='Amount:', font=("Gill Sans MT", 13), bg="#00ff91",
                                        fg="#000314").place(x=80, y=265)
        self.amount_value = Label(self.frame, text=u"\u20B9" + str(data[3]), font=("Gill Sans MT", 17),
                                        bg="#00ff91",
                                        fg="#000314").place(x=80, y=295)
        self.created_label = Label(self.frame, text='Created at:', font=("Gill Sans MT", 13), bg="#00ff91",
                                        fg="#000314").place(x=80, y=355)
        self.created_value = Label(self.frame, text=data[4], font=("Gill Sans MT", 17),
                                        bg="#00ff91",
                                        fg="#000314").place(x=80, y=385)

    def delete_expense(self, data):
        self.db.delete_expense(data[0])
        self.db.update_expense(self.Id, self.total_expense - int(data[3]))
        self.switch_frame("homepage")


obj = ExpenseTracker()
