# This program will get an input from the user(age) and checks if the user is illegible of driving under legal driving age of 18

name = input('Please provide your Name to continue>> ')

print(f'Hello {name}! Please provide your age to continue>> ')

age = int(input(f'{name} How old are you? '))
# another way to convert input is 
# age = int(age)

if age < 18:
    print(f'Sorry {name} you are not authorized to drive at {age} \n')
elif age == 18:
    print(f'Congrat! {name} you are {age} year old. The minimum age for driving in this state. Please be safe')
else:
    print(f'Congratulation! {name} you are authorized to drive at {age}. Please drive safely. \n')