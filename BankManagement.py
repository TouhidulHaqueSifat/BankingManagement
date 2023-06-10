class Bank:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.balance = 0
        self.loan = 0
        self.loan_enabled = True

    def total_balance(self):
        print(f"Total Bank Balance is: {self.balance}")

    def total_loan(self):
        print(f"Total Bank loan is: {self.loan}")

    def enable_loan(self):
        self.loan_enabled = True

    def disable_loan(self):
        self.loan_enabled = False


class Person:
    def __init__(self, email, password, bank):
        self.email = email
        self.password = password
        self.bank = bank

    def create_acc(self, email, password):
        email = self.email
        password = self.password
        print("your account create successfully your email is:", email)


class User(Person):

    def __init__(self, email, password, bank):
        super().__init__(email, password, bank)
        self.user_balance = 0
        self.user_loan = 0
        self.history = []

    def cr_user_acc(self):
        self.create_acc(self.email, self.password)

    def deposit(self, amount):
        if amount > 0:
            self.user_balance += amount
            self.bank.balance += amount
            self.history.append(f'deposit: {amount}')

    def available_balance(self):
        print(f"{self.email} total balance is {self.user_balance}")

    def withdraw(self, amount):
        if amount <= self.user_balance and amount < self.bank.balance:
            self.user_balance -= amount
            self.bank.balance -= amount
            self.history.append(f"Withdraw : {amount}")
        elif amount > self.user_balance:
            print("You cant withdraw money your balance is less than your amount")
        else:
            print("Bank is bankrupt, Unable to withdraw")

    def transfer(self, amount, another_user):
        if amount <= self.user_balance and amount < self.bank.balance:
            self.user_balance -= amount
            another_user.user_balance += amount
            self.history.append(f"Transfer: {amount} to {another_user.email}")

        elif amount > self.user_balance:
            print("You can't Transfer money more Your balance is less then the amount")
        else:
            print("Bank is bankrupt, Unable to withdraw")

    def loan_requested(self, amount):
        loan_limit = self.user_balance * 2
        if amount <= loan_limit and amount < self.bank.balance and self.bank.loan_enabled:
            self.user_balance += amount
            self.bank.balance -= amount
            self.bank.loan += amount
            self.user_loan += amount
            self.bank.enable_loan()
            self.history.append(f"Take a loan of Tk {amount} from {self.bank.name} Bank ")
            print(f"{self.email} Take a loan of Tk {amount} from {self.bank.name} Bank")
        else:
            print(f"{self.email} Your loan request denied")

    def user_total_loan(self):
        print(f"{self.email} total loan is {self.user_loan}")

    def his_tory(self):
        print(f"Transaction History of {self.email}: ")
        for i in self.history:
            print('.', i)


class Admin(User):
    def __init__(self, email, password, bank):
        super().__init__(email, password, bank)

    def cr_admin_acc(self):
        self.create_acc(self.email, self.password)

    def total_bank_balance(self):
        self.bank.total_balance()

    def total_bank_loan(self):
        self.bank.total_loan()


janata = Bank("janata", 'dhaka')
admin = Admin("admin@gmail.com", 1234, janata)
user = User("efg@gmail.com", 1234, janata)
user.cr_user_acc()
user.deposit(100)
user.withdraw(500)
user.available_balance()
user.deposit(100)
user.available_balance()

user2 = User("abc@gmail.com",1234, janata)
user2.deposit(500)
user2.deposit(600)
admin.total_bank_balance()
user2.his_tory()

user2.available_balance()
user2.transfer(500, user)
user2.his_tory()


user.loan_requested(1700)
user.available_balance()
user2.available_balance()
user2.loan_requested(500)
user.his_tory()
user2.user_total_loan()
user.user_total_loan()
admin.total_bank_loan()

admin.total_bank_balance()



