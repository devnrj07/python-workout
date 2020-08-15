# Yes or No polling app

print('\n Welcomre to the polling system.')
poll_question = input('\n What is the polling for (mention th issue) : ').title().strip()
max_voters = int(input('\n Enter the maximum number of voters allowed. : '))
master_password = input('\n Enter the master password. : ').strip()

yes_count = 0
no_count = 0
vote_result = dict()

for i in range(max_voters):
    voter_name = input('\n Enter your full name : ').lower().strip()
    if voter_name in vote_result:
        print('\n Sorry! You have already voted!')
    else:
        print(f'\n {poll_question}')
        voter_response = input('\n Enter your response for above displayed question.(y/n) : ').lower().strip()
        if voter_response.startswith('y'):
            yes_count += 1
            vote_result.update({voter_name:'yes'})
        elif voter_response.startswith('n'):
            no_count += 1
            vote_result.update({voter_name:'no'})
        else:
            print('\n You entered an invalid response. It has been recorded but it will not affect the poll results.')
        print('\n Thank you for taking part in this poll. ')

print(f'\n Total number voters that took part : {max_voters}')
for name in vote_result:
    print(f'\n {name}')
print(f'\n -----------Voting summary-----------')
print(f'\n The Issue : {poll_question}')
print(f'\n Yes : {yes_count} \t\t No: {no_count}')

if yes_count > no_count:
    print('\n Yes Won the poll. ')
elif yes_count < no_count:
    print('\n No Won the poll. ')
else: 
    print('\n It was a tie.') 

entered_password = input('\n Enter the master password if you wish to see the poll results in detail. ').strip()
if entered_password == master_password:
    for name, vote in vote_result.items():
        print(f'\n {name} - {vote}')
else:
    print('\nIncorrect password')
print('\n Thank you for using our program.')             