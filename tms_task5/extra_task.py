import re
import json

            
def checking_validation(func):
    def wrapper(email, password):
        reg_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        reg_pass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$"
        pat = re.compile(reg_pass)
        mat = re.search(pat, password)
        
        if not (re.fullmatch(reg_email, email)):
            raise Exception("Invalid Email")
        
        if not mat:
            raise Exception("Invalid Password!")
        
        func(email, password)
    
    return wrapper


class Account:
    @staticmethod
    def ask_credentials():
            em_text = 'Please enter an email!\n'
            pass_text = 'Please enter a password! \nPassword should have at least one numeral,\none uppercase and one special symbol!\n'
            email = input(em_text)
            password = input(pass_text)
            
            return email,password

    
    @staticmethod
    def authorization(email, password: str):
        with open('users.json', 'r') as file:
            data = json.load(file)
            users_emails = [users['Email'] for users in data]
            users_passwords = [users['Password'] for users in data]
            
            if email in users_emails and password in users_passwords:
                print('======\nWellcome back, my friend!\n======')
            
            else:
                print('Check your email or password!')


    @checking_validation
    @staticmethod
    def registration(email, password: str):
        users_to_add = []
        users = {
            'Email': email, 
            'Password': password
            }
        users_to_add.append(users)
        
        with open('users.json', 'w') as file:
            json.dump(users_to_add, file)
        
        return print('======\nRegistration complete! Now you can Sign in!\n======')


if __name__ == '__main__':
    while True:
        answer = input('Menu:\n1 - Sing in\n2 - Sing up!\n0 - Exit\nYour choice? ')
        
        if answer == '1':
            email, password = Account.ask_credentials()            
            Account.authorization(email, password)
        
        elif answer == '2':
            email, password = Account.ask_credentials()           
            Account.registration(email, password)
        
        elif answer == '0':
            break
        
        else:
            print('Invalid choice')