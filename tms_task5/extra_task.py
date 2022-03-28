import re
        
def checking_validation(func):
    def wrapper(email, password):
        reg_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        reg_pass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$"
        pat = re.compile(reg_pass)
        mat = re.search(pat, password)
        if not (re.fullmatch(reg_email, email)):
            raise Exception("Invalid Email")
        else:
            pass
        if not mat:
            raise Exception("Invalid Password!")
        else:
            pass
        func(email, password)
    return wrapper

def authorization(email, password: str):
    with open('users.txt') as file:
        for line in file.readlines():
            if email and password in line:
                print('======\nWellcome back, my friend!\n======')
            else:
                print('Check your email or password!')

@checking_validation
def registration(email, password: str):
    with open('users.txt', 'a') as file:
        L = [f'{email}:{password}', '\n']
        file.writelines(L)
        file.close()
    return print('======\nRegistration complete! Now you can Sign in!\n======')

if __name__ == '__main__':
    while True:
        em_text = 'Please enter an email!\n'
        pass_text = 'Please enter a password! \nPassword should have at least one numeral,\none uppercase and one special symbol!\n'
        answer = input('Menu:\n1 - Sing in\n2 - Sing up!\n0 - Exit\nYour choice? ')
        if answer == '1':
            email = input(em_text)
            password = input(pass_text)            
            authorization(email, password)
        elif answer == '2':
            email = input(em_text)
            password = input(pass_text)            
            registration(email, password)
        elif answer == '0':
            break
        else:
            print('Invalid choice')