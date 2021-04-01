import mysql.connector


class Database:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="expense_tracker")
            self.mycursor = self.conn.cursor()
        except:
            print("Connection error")
        else:
            print("Connection successful")

    def login_signup(self, state, name, email, password):
        if state == "login":
            self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password))
            data = self.mycursor.fetchall()
            return data
        else:
            try:
                self.mycursor.execute("INSERT INTO users VALUES (NULL, '{}', '{}', '{}', '{}')".format(name, email, password, 0))
                data = self.conn.commit()
            except:
                return -1
            else:
                return 1

    def total_expense(self, userid):
        self.mycursor.execute("SELECT total_expense FROM users WHERE id LIKE '{}'".format(userid))
        total_expense = self.mycursor.fetchall()
        return total_expense

    def update_expense(self, userid, amount):
        try:
            self.mycursor.execute("UPDATE users SET total_expense = '{}' WHERE users.Id = '{}'".format(amount, userid))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def get_id(self, email):
        self.mycursor.execute("SELECT id FROM users WHERE email LIKE '{}'".format(email))
        id = self.mycursor.fetchall()
        return id

    def expenses(self, userid):
        self.mycursor.execute("SELECT * FROM expenses WHERE user_id LIKE '{}'".format(userid))
        data = self.mycursor.fetchall()
        return data

    def add_edit_expense(self, state, user_id, expense_type, amount, date_or_expenseid):
        if state == 'addexpense':
            try:
                self.mycursor.execute(
                    "INSERT INTO expenses VALUES (NULL, '{}', '{}', '{}', '{}')".format(user_id, expense_type, amount, date_or_expenseid))
                data = self.conn.commit()
            except:
                return -1
            else:
                return 1
        else:
            try:
                self.mycursor.execute(
                    "UPDATE expenses SET expense_type = '{}', amount = '{}' WHERE expenses.expense_id = '{}'".format(expense_type, amount, date_or_expenseid))
                data = self.conn.commit()
            except:
                return -1
            else:
                return 1

    def delete_expense(self, expense_id):
        try:
            self.mycursor.execute(
                "DELETE FROM expenses WHERE expenses.expense_id = '{}'".format(expense_id))
            data = self.conn.commit()
        except:
            return -1
        else:
            return 1