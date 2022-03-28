import re

def checking(func):
    def wrapper(email, password):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)

        if(re.fullmatch(regex, email)):
            pass
        else:
            print("Invalid Email")

        if mat:
            pass
        else:
            print("Password invalid !!")
        func(email, password)

    return wrapper


def authorization(email, password):
    with open('users.txt') as file:
        for line in file.readlines():
            if email and password in line:
                print('======\nWellcome back, my friend!\n======')
            else:
                print('Check your email or password!')


@checking
def registration(email, password):
    with open('users.txt', 'a') as file:
        L = [f'{email}:{password}', '\n']
        file.writelines(L)
        file.close()
    return print('======\nRegistration complete! Now you can Sign in!\n======')


if __name__ == '__main__':
    while True:
        answer = input('Menu:\n1 - Sing in\n2 - Sing up!\n0 - Exit\nYour choise? ')
        if answer == '1':
            email = input('Please enter an email!\n')
            password = input('Please enter a password! \nPassword should have at least one numeral,\none uppercase and one special symbol!\n')
            authorization(email, password)

        elif answer == '2':
            email = input('Please enter an email!\n')
            password = input('Please enter a password! \nPassword should have at least one numeral,\none uppercase and one special symbol!\n')
            registration(email, password)

        elif answer == '0':
            break

        else:
            print('Answer is incorrect')
