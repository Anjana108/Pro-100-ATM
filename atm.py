class Atm(object):

    def __init__(self, balance):
        self.balance = balance

    def main(self):
        print("""***Welcome to PRO-100 ATM***
    Please insert your card.""")
        input('Once done, please press ENTER.')
        account = str(input('Please enter you account number:          '))
        uid = str(input('Please enter you Username/ID:          '))
        password = str(input('Please enter your password:          '))
        if account == '123456789':
            if uid.lower() == 'pavithra':
                if password.lower() == '7123':
                    toDo = input('''What would you like to do?
    Enter 1 for Balance,
          2 for Cash withdrawal,
          3 for Cash deposition,
          4 for Logging out
          
          :     ''')
                    if toDo == '1':
                        self.view_balance()
                    if toDo == '2':
                        self.withdrawal()
                    if toDo == '3':
                        self.deposition()
                    if toDo == '4':
                        self.logOut()
                        
                else: 
                    print('Incorrect password. Try again.')
                
            else: 
                print('Incorrect Username/ID')

        elif account == '234567890':    
            if uid.lower() == 'anjana':
                if password.lower() == '6123':
                    toDo = input('''What would you like to do?
    Enter 1 for Balance,
          2 for Cash withdrawal,
          3 for Cash deposition,
          4 for Logging out
          
          :     ''')
                    if toDo == '1':
                        self.view_balance()
                    if toDo == '2':
                        self.withdrawal()
                    if toDo == '3':
                        self.deposition()
                    if toDo == '4':
                        self.logOut()
                        
                else: 
                    print('Incorrect password. Try again.')

            else: 
                print('Incorrect Username/ID')

        else:
            print('Unidentified account number. Register at your bank before using it.')

    def view_balance(self):
        print('Your current account balance is, ' + str(self.balance))  

    def withdrawal(self):
        toWithdraw = int(input('How much do you want to withdraw from your account?          '))
        self.balance = self.balance-toWithdraw
        if self.balance-toWithdraw < 0:
            print('You do not have enough balance left.')
            self.balance = 0
        else: 
            print('Withdrawn successfully. You current balance is ' + str(self.balance))

    def deposition(self):
        toDeposit = int(input('How much do you want to deposit into your account?          '))
        self.balance = self.balance+toDeposit
        print('Deposit successfull. Your current balance is ' + str(self.balance))

    def logOut(self):
        print('Logout successfull.')

bank = Atm(100000)
bank.main()