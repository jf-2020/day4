# string_exercises.py - this prgm will follow along with the DC day 4
#                     string string_exercises
#
# jf - 4/18

# n.b. 'inpt' will be shorthand for 'input' throughout


##########################
### Uppercase a String ###
##########################


def uppercase_a_string(str):
    '''
    param:
        type(str) -> String
    return:
        type() -> String
    '''

    return str.upper()

def main_0():
    # main function for Uppercase a String problem
    
    inpt = input("Input a string: ")
    print(uppercase_a_string(inpt))


###########################
### Capitalize a String ###
###########################


def capitalize_a_string(str):
    '''
    param:
        type(str) -> String
    return:
        type() -> String
    '''
    
    return str.capitalize()

def main_1():
    # main function for Capitalize a String problem

    inpt = input("Input a string: ")
    print(capitalize_a_string(inpt))


########################
### Reverse a String ###
########################


def reverse_a_string(str):
    '''
    param:
        type(str) -> String
    return:
        type() -> String
    '''

    return str[::-1]

def main_2():
    # main function for Reverse a String problem

    inpt = input("Input a string: ")
    print(reverse_a_string(inpt))


#################
### Leetspeak ###
#################


def leetspeak(str):
    '''
    param:
        type(str) -> String
    return:
        type(ret_val) -> String
    '''

    # don't update in place
    ret_val = ''

    # values required to translate
    aegiost = 'aegiost'

    # corresponding values to which they must be translated (1-to-1 mapping)
    translate_table = '4361057'

    # enumerate over values in string, accounting for the index in
    # the enumeration is at currently, storing in idx said index and
    # char said character, respectively
    for idx, char in enumerate(str.lower()):
        
        # check if current character is in translatable values
        if char in aegiost:

            # get it's index in translatable values, so that value to translate
            # to can be accessed
            index = aegiost.index(char)

            # access the value in the (1-to-1) translate table via said index
            translate_char_to = translate_table[index]

            # update the value in the str arg
            ret_val += translate_char_to

        else:
            ret_val += str[idx]

    return ret_val

def main_3():
    # main function for Leetspeak problem

    inpt = input("Give me a string: ")
    print(leetspeak(inpt))


########################
### Long-long Vowels ###
########################


def long_long_vowels(str):
    '''
    param:
        type(str) -> String
    return:
        type(ret_val) -> String
    '''

    # assume str considers long vowels as an occurrence of EXACTLY two consecutive
    # vowels (no more, no less & actual phonics is irrelevant)

    ret_val = ''
    count = 0

    for char in str:

        if count + 1 < len(str) and str[count + 1] == char:
            ret_val += char*5

        elif count - 1 > 0 and str[count - 1] == char:
            count += 1
            continue
        
        else:
            ret_val += char

        count += 1

    return ret_val

def main_4():
    # main function for Long-long Vowels problem

    inpt = input("Give me a string: ")
    print(long_long_vowels(inpt))


#####################
### Caeser Cipher ###
#####################

def caesar_cipher(str):
    '''
    param:
        type(str) -> String
    return:
        type(ret_val) -> String
    '''

    # to apply the caesar cipher, we must rotate the alphabet by 13 positions,
    # so for example, A -> N, B -> O, etc...

    ret_val = ''

    for char in str:

        # skip spaces
        if char == ' ':
            ret_val += ' '
        
        # handle uppercase letters
        elif ord(char) < ord('a'):

            shifted_char_ascii_val = ((ord(char) - ord('A') + 13) % 26) + ord('A')
            ret_val += chr(shifted_char_ascii_val)

        # otherwise, it's lowercase
        else:

            shifted_char_ascii_val = ((ord(char) - ord('a') + 13) % 26) + ord('a')
            ret_val += chr(shifted_char_ascii_val)

    return ret_val

def main_5():
    # main function for Caesar Cipher problem

    inpt = input("Give me some plaintext: ")
    print("Here is the cipher text:", caesar_cipher(inpt))


# to be run as script
if __name__ == "__main__":
    # main_0()
    # main_1()
    # main_2()
    # main_3()
    # main_4()
    main_5()