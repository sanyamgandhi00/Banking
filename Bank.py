class Bank:
  bankId = 0
  banks = [] 
  def __init__(self , bankAbbrevation , bankName , bankID):
    self.bankAbbrevation = bankAbbrevation
    self.bankName = bankName
    self.bankId = Bank.bankId

  @staticmethod
  def bankExistsWithTheAbbrevation(bankAbbrevation):
    for bank in Bank.banks:
      if bank.bankAbbrevation == bankAbbrevation :
        return True , bank
    else :
      return False , None 
      
  @staticmethod
  def bankExistsWithTheName(bankName):
    for bank in Bank.banks:
      if bank.bankName == bankName :
        return True , bank
    else :
      return False , None 

  @staticmethod 
  def createBank(bankAbbrevation , bankName):
    bankAbbrevationExist , bankObject = Bank.bankExistsWithTheAbbrevation(bankAbbrevation) 
    if(bankAbbrevationExist == True) :
      return "Bank Already Exist with this name"
    bankNameExist , bankObject = Bank.bankExistsWithTheName(bankAbbrevation) 
    if(bankNameExist == True) :
      return "Bank Already Exist with this name"
    
    Bank.bankId +=1
    bankId = Bank.bankId 
    bankObject = Bank(bankAbbrevation , bankName , bankId) 
    Bank.banks += [bankObject] 

    return "Bank Created"
    
