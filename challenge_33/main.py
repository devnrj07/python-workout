# Bank Deposit and withdrawl app

def get_info():
    print('\n Welcome to the Fake Bank. ')
    name = input('\n Please enter your name. ')
    savings_account_bal = float(input(f'\n hi {name}, enter your initial deposit with savings account '))
    checking_account_bal = float(input(f'\n hi {name} enter your initial deposit with checking account '))

    user_info = {
        "user_name": name,
        "savings" : savings_account_bal,
        "checking" : checking_account_bal
    }
    return user_info

def make_deposit(bank_details : dict, acc_type: str, amount : float ):
    bank_details[acc_type] += amount
    print(f'\n {amount} added to your {acc_type} account. Total amount {bank_details[acc_type]}.')

def make_withdrawl(bank_details : dict, acc_type: str, amount:float):
    current_bal = bank_details[acc_type]
    current_bal -= amount

    if(current_bal > 0) :
        print(f'\n Transaction was successful')
        bank_details[acc_type] -= amount
        print(f'\n Updated balance in {acc_type} is {bank_details[acc_type]}')
    else :
        print(f'Insufficient balance to make this transaction.')        

def display_info(bank_details: dict):
    print('\n -------------- Account Summary -------------------')
    print(f'\n Name : {bank_details["user_name"]}')
    print(f'\n Savings : {bank_details["savings"]}')
    print(f'\n Checking : {bank_details["checking"]}')

if __name__ == "__main__":
  details = get_info()
  running= True 
  while running:
     acc_type : str= ""
     trans_type : str = ""
     amount : float= 0.0
     
     display_info(details)

     acc_type = input('\n Choose tha account type (checking/savings) ').lower()
     trans_type = input('\n Choose the type of transactions (withdrwal/deposit) ').lower() 
     amount = float(input('\n Enter the ammount'))

     if acc_type.startswith('c') :
         if trans_type.startswith('w'):
             make_withdrawl(details,'checking', amount)
         elif trans_type.startswith('d'):
             make_deposit(details, 'checking', amount)
         else:
             print('Invalid selection!')        
     elif acc_type.startswith('s'):
         if trans_type.startswith('w'):
             make_withdrawl(details,'savings', amount)
         elif trans_type.startswith('d'):
             make_deposit(details, 'savings', amount)
         else:
             print('Invalid selection!')
     else :
         print('Invalid Selection')    

     continue_app = input('\n Would you like to make another transaction ? (Y/N). ').lower()
     if continue_app.startswith('n'):
         display_info(details)
         print('\n Thank you for banking with us.')
         running =False     