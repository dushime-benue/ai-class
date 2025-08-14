print('select your choice')
print("1. ilometer-miles convetor")
print('2. temperature convetor')
print('3. discount calculator')

choice=input('enter your choice: (1/2/3) ')

if choice == '1':
    kilometers=float(input('Enter kilometers'))
    miles=kilometers*0.621371 
    print(miles)
     

elif choice == '2':
    temp_c= float(input('Enter celsius temp:'))
    temp_f= (temp_c*9/5)+32
    print(temp_f)

elif choice == '3':
    cost= float(input('enter the cost'))
    if cost > 400000:
        print(cost*0.8)
    elif cost >=200000:
        print(cost*0.9)
    else:                              
        print(cost)







