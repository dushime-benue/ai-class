name='benue'
age=16
gender='male'
school='st peters'
print(f'my name is', name)
print(f'my age is', age)
print(f'I am a', gender)
print(f'i was learning at', school)

#BMI calculator function
def calculate_bmi(weight,hieght):
    bmi=weight/hieght**2
    return round(bmi,2)
#user input
w = float(input('enter your weight:'))
h = float(input('type your height in m:'))
# invoke the functionpy
result=calculate_bmi(w,h)
print('your bmi is',result )


#progranm to check age
def check_age(age):
    if age < 18:
        return 'you are immature'
    else:
         return 'you are an adult'
user_age= int(input('enter your age'))         
result_age= check_age(user_age)
print(result_age)

# program to check pionts
def check_point(points):
    if points > 36:
        return 'sorry, you have failed'
    else:
        return 'congratulation, you have passed'

user_points= int(input('enter your points'))
result_points= check_point(user_points)

print(result_points)
   






                                                                                                                                                             