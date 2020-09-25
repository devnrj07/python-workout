#Loan Calculation app with graph
from matplotlib import pyplot


def get_loan_info():
    loan_details = {}
    loan_details['principle'] = float(input('Enter the loan amount : '))
    loan_details['rate'] = float(input('Enter the interest rate : '))/100
    loan_details['monthlyPayment'] = float(input('Enter your monthly payment : '))
    loan_details['moneyPaid'] = 0.0
    return loan_details

def show_loan_info(current_loan_details : dict, months : int):
    print(f'\n Current Loan Status after {months} :')
    for key,value in current_loan_details.items():
        print(f'\n {key} = {value}')

def collect_interest(current_loan_details: dict):
     current_loan_details['principle'] = current_loan_details['principle'] + current_loan_details['principle'] * current_loan_details['rate']/12
   

def make_monthly_payment(current_loan_details : dict) :
    current_loan_details['principle'] = current_loan_details['principle'] - current_loan_details['monthlyPayment']
    if current_loan_details['principle'] > 0 :
        current_loan_details['moneyPaid'] += current_loan_details['monthlyPayment']
    else :
        current_loan_details['moneyPaid'] += current_loan_details['monthlyPayment'] + current_loan_details['principle']
        current_loan_details['principle'] = 0


def summarize_loan(current_loan_details : dict, month : int, initial_principle : float):
    print("\nCongraulations! You paid off your loan in " + str(month) + "months!")
    
    print('\n -----------Your Loan Summary--------------- ')
    print(f'\n Initial Loan Amount : {initial_principle}')
    print('\n Monthly payment : '+ str(current_loan_details['monthlyPayment']))
    print(f'\n Interest Rounding : ' +  str(round(current_loan_details['moneyPaid'],2)))
    interest = round(current_loan_details['moneyPaid'] - initial_principle ,2)
    print(f'\n Total Rounding : {interest}')

def create_graph(data_set:list, loan:float):
    x_values = []
    y_values = []
    for tup in data_set:
        x_values.append(tup[0])
        y_values.append(tup[1])

    pyplot.plot(x_values, y_values)
    pyplot.title(str(100*loan['rate'])+ "% interest with $ "+ str(loan['monthlyPayment'])+ "monthly payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()

if __name__ == "__main__":
    print('Welcome to the Loan calculation app. ')
    month_number = 0

    loan = get_loan_info()
    starting_principle = loan['principle']
    data_to_plot = []

    #Display starting conditions of loan
    show_loan_info(loan, month_number)
    input("Press 'Enter' to begin paying off your loan.")

    while loan['principle'] > 0:
        if loan['principle'] > starting_principle:
            break

        month_number +=1
        collect_interest(loan)
        make_monthly_payment(loan)
        data_to_plot.append((month_number, loan['principle'])) 
        show_loan_info(loan, month_number)


#The loan is either paid off in full or it can NEVER be paid off...
#The loan was paid off in full
if loan['principle'] <= 0:
    summarize_loan(loan,month_number,starting_principle)
    create_graph(data_to_plot,loan)

#The loan can NEVER be paid off, can't get ahead of interest
else:
    print("\nYou will NEVER pay off your loan!!!")
    print("You cannot get ahead of the interest! :-(")




