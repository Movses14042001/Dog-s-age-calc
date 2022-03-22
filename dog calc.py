import traceback


def calculator(input_value):
    # Get dog age
  
    
human_age = [15, 12, 9.3, 8, 7.2, 7]

    try:
        if dog_age <= 0:
            print('Age cannot be a negative number and 0.')
        elif dog_age > 0 and dog_age < 0.9:
            print("Please wait for your dog's first birthday")
        elif dog_age == 1:
            calculated_age = float(human_age[0])
            print(f'The given dog age {input_value} is {calculated_age} in human years.')
        elif dog_age >= 1.1 and dog_age < 2.1:
            calculated_age = float(human_age[1]) * dog_age
            print(f'The given dog age {input_value} is {calculated_age} in human years.')
        elif dog_age == 3:
            calculated_age = round((float(human_age[2]) * dog_age), 9)
            print(f'The given dog age {input_value} is {calculated_age} in human years.')
        elif dog_age >= 2.1 and dog_age < 3.1:
            calculated_age = float(human_age[2]) * dog_age
            print(f'The given dog age {input_value} is {calculated_age} in human years.')
        elif dog_age >= 3.1 and dog_age < 4.1:
            calculated_age = float(human_age[3]) * dog_age
            print(f'The given dog age {input_value} is {calculated_age} in human years.')
        elif dog_age >= 4.1 and dog_age < 5.1:
            calculated_age = float(human_age[4]) * dog_age
            print(f'The given dog age {input_value} is {calculated_age} in human years.')
        elif dog_age >= 5.1 and dog_age < 20:
            calculated_age = dog_age * float(human_age[5]) + 1
            print(f'The given dog age {input_value} is {calculated_age} in human years.')
        elif dog_age >= 20:
            print(f"The given dog age {input_value} is not valid dogs don't live that much")
        else:
            print("Something is wrong cant calculate dog's age in human years")

    except ValueError as e:
        print(e)
        print(traceback.format_exc())

input_value = input("Input_dog_years.")
if input_value.isalpha():
    print(f"the given dog age {input_value} is not valid")

dog_age = float(input_value)
    
    
calculator(input_value)