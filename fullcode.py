def kilometers_conveter():
    kilometers=float(input('Enter kilometers'))
    miles=kilometers*0.621371
    print(f'{kilometers}km = {miles:.2f} miles')

def temp_conveter():
    temp_c= float(input('Enter celsius temp:'))
    temp_f= (temp_c*9/5)+32
    print(f'{temp_c}C= {temp_f:.1f}F')

def calculate_discount(  ):
    cost= float(input('enter the cost'))
    if cost > 400000:
        final= cost*0.8
    elif cost >=200000:
        final= cost*0.9
    else:
        final=cost
    print(calculate_discount(final))

def main():
    print('welcom to smart tools!')
    print('1. kilometer to miles conveter')
    print('2. temperature convetor(C to F)')
    print('3. shop discount conveter')

    choice = input('choose an option  (1-3):')
    if choice == '1':
            kilometers_conveter()
    elif choice == '2':
            temp_conveter()
    elif choice == '3':
            calculate_discount()
    else:
        print('invalid choice. try again!')
main()
