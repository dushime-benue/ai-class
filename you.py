# login system
user_names= ["ben","cyber","joel","cruz","centhia","amanda","syphila"]
user_input= input('enter your name to logIn  ')
valid = ''
for i in user_names:
    if user_input in user_names:
        valid += f'Welcome {user_input}'
        break
    valid += f'{user_input} is not recognised'
    break
print(valid)

password= ["b102","c14","jay4","z12","ty17","a209","s24"]
input_password= input('enter your password:  ')
valid = ''
for i in password:
    if input_password in password:
        valid += f'welcome'
        break
    valid += f'invalid password'
    break
print(valid)    




class bank_account:
    def __init__(self,deposit,withdraw):
        self.deposit = deposit
        self.withdraw = withdraw