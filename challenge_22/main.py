# Database Admin App
print('\n Welcome to the Hasura Database ')

log_on_info = {
    "admin00": "admin00",
    "user1": "abcdefgh",
    "user2": "zxcvbnm,",
    "user3": "qweasdzxc",
    "user4": "poiuytre",
    "user5": "rfvtgbyhn"
}

username = input('\n Enter your user name : ').lower().strip()

if username in log_on_info:
    password = input('\n Enter your password : ')
    if password == log_on_info[username]:
        print(f'\n Welcome {username}, You\'re now logged In')
        if username == 'admin00':
            print(f'\n All registered users :')
            for key, value in log_on_info.items():
                print(f'\n {key} - {value}')
        else:
            response = input(
                '\n Would you like to change your password sir!(y/n) : ').lower().strip()
            if response == 'y':
                new_password = input(
                    '\n Enter your new password (8 characters long)').lower().strip()
                if len(new_password) >= 8:
                    log_on_info[username] = new_password
                    print(f'\n Hi {username}, your password is updated with {new_password}.')
                else:
                    print('\n password length too short!. Try again next time.')
            else:
                print('\n Ok! GoodBye. You\'re logged out!')
    else:
        print('\n No such user exists!')