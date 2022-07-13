
from . import Bank , Account

class Customer:

    customerId = 0
    customers = []

    def __init__(self , customerId , firstName , lastName , accounts , totalBalance):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName
        self.accounts = accounts
        self.totalBalance = totalBalance

    @staticmethod
    def createCustomer(firstName , lastName):
        Customer.customerId += 1
        customer = Customer(Customer.customerId , firstName , lastName , list() , 0)
        Customer.customers.append(customer)
        return customer

    
    @staticmethod
    def transaction(amount , creditorId , debitorId):
        if Account.getAccount(creditorId):
            if Account.withdrawCash(amount , debitorId):
                Account.depositCash(amount , creditorId)
            else : 
                return "Bank Issue"
        else :
            return "Account Not Found Plz check your details"

    
    def createAccount(self , fullName , bankAbbreviation):
        account = Account.createAccount(fullName , bankAbbreviation)
        if account:
            print("Account successfully created")
            self.accounts.append(account)
        else : 
            print("Bank Issue ....Please try again")

    def getBalanceOfAllAccounts(self):
        totalBalance = 0
        for account in self.accounts:
            totalBalance += account.balance
        return totalBalance

    @staticmethod
    def getCustomer(customerId):
        for customer in Customer.customers:
            if customer.customerId == customerId :
                return True , customer
        return False , None 


    def getAccount(self , accountId):
        for account in self.accounts:
            if account.accountId == accountId:
                return account

    def deposit(self , amount , accountId):
        Account.depositCash(amount , accountId)
    
    def withraw(self , amount , accountId):
        Account.withdrawCash(amount , accountId)

    def getBalance(self , accountId):
        account = Account.getAccount(accountId)
        if not account:
            print("The Account does not exist")
        else:
            return account.balance




    



