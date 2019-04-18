# python_exercises_review.py - this prgm will follow along with DC day 4's python
#                              review exercises as indicated
#
# jf - 4/18

### n.b. - will use "inpt" to mean "input" as shorthand throughout ###

#######################
### Day of the Week ###
#######################

def day_of_the_week():
    '''
    param type  -> None
    return type -> String
    '''

    inpt = int(input("Day (0-6)? "))

    if inpt == 0:
        return "Monday"
    elif inpt == 1:
        return "Tuesday"
    elif inpt == 2:
        return "Wednesday"
    elif inpt == 3:
        return "Thursday"
    elif inpt == 4:
        return "Friday"
    elif inpt == 5:
        return "Saturday"
    else:
        return "Sunday"

def main_0():
    # main function for Day of the Week problem

    ret_val = day_of_the_week()
    print(ret_val)

#########################
### Work or Sleep In? ###
#########################

def work_or_sleep_in():
    '''
    param type  -> None
    return type -> String

    '''

    inpt = int(input("Day (0-6)? "))

    if inpt >+ 0 and inpt <= 4:
        return "Go to work"
    else:
        return "Sleep in"

def main_1():
    # main function for Work of Sleep In problem

    ret_val = work_or_sleep_in()
    print(ret_val)

#############################
### Celsius to Fahrenheit ###
#############################

def celsius_to_fahrenheit():
    '''
    param type  -> None
    return type -> Float
    '''

    inpt = float(input("Temperature in C? "))

    return (9/5) * inpt + 32.0

def main_2():
    # main function for Celsius to Fahrenheit problem
    
    ret_val = celsius_to_fahrenheit()
    print(str(ret_val) + " F")

######################
### Tip Calculator ###
######################

def tip_calculator():
    '''
    param type  -> None
    return type -> Tuple: Float, Float
    '''

    bill_amount = float(input("Total bill amount? "))
    level_of_service = input("Level of service? ")

    if level_of_service == "good":
        tip_amount = 0.2 * bill_amount
    elif level_of_service == "fair":
        tip_amount = 0.15 * bill_amount
    else:
        tip_amount = 0.1 * bill_amount

    total_amount = tip_amount + bill_amount

    return tip_amount, total_amount

def main_3():
    # main function for Tip Calculator problem
    
    tip_amount, total_amount = tip_calculator()
    
    print("Tip amount: $" + str(tip_amount))
    print("Total amount: $" + str(total_amount))

########################
### Tip Calculator 2 ###
########################

def tip_calculator_2():
    '''
    param type  -> None
    return type -> Tuple: Float, Float, Float
    '''

    tip_amount, total_amount = tip_calculator()

    number_of_people = int(input("Split how many ways? "))
    amount_per_person = total_amount / float(number_of_people)

    return tip_amount, total_amount, amount_per_person

def main_4():
    # main function for Tip Calculator 2 problem

    tip_amount, total_amount, amount_per_person = tip_calculator_2()

    print("Tip amount: $" + str(tip_amount))
    print("Total amount: $" + str(total_amount))
    print("Amount per person: $" + str(amount_per_person))

# to be called as script
if __name__ == "__main__":
    # main_0()
    # main_1()
    # main_2()
    # main_3()
    main_4()