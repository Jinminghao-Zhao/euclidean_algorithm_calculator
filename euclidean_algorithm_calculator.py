def recursive_find_gcd(bigger_integer, smaller_integer):
    if smaller_integer == 0:
        gcd = bigger_integer
        return gcd
    else:
        remainder = bigger_integer % smaller_integer
        quotient = int((bigger_integer - remainder)/smaller_integer)
        print(f'\n{bigger_integer} = {smaller_integer} * {quotient} + {remainder}')
        gcd = recursive_find_gcd(smaller_integer, remainder)
        return gcd

def int_size_decider(first_integer, second_integer):
    if first_integer > second_integer:
        return first_integer, second_integer
    else:
        return second_integer, first_integer

def find_gcd(bigger_integer, smaller_integer):
    print(f'Since {bigger_integer} is larger than {smaller_integer}, we can rewrite {bigger_integer} as {smaller_integer} * q + r where q is the quotient and r is our remainder. Remember! The last non-zero remainder is our gcd (unless both integers are the same, then what you get is that the gcd is... well... the integer)! Therefore...')
    gcd = recursive_find_gcd(bigger_integer, smaller_integer)
    print(f'\n... {gcd} is the GCD of {bigger_integer} and {smaller_integer}!')

def collect_numbers():
    gather_two_integers = False

    while not gather_two_integers:
        first_integer = input('Please enter the first integer you want to find the GCD of! ')
        second_integer = input('Please enter the second integer you want to find the GCD of! ')
        try:
            first_integer = int(first_integer)
            second_integer = int(second_integer)
        except ValueError:
            print("One or both of the... things you typed in are not integers. Please type in two integers.")
        else:
            print("Thank you for typing in two integers!")
            gather_two_integers = True
    
    return first_integer, second_integer

def main():
    print("Hi! This is a calculator that uses and displays the Euclidean Algorithm of finding the Greatest Common Divisor (GCD) of two given integers!")
    start = input("For now, do you want to start using the calculator? (enter y for yes and n for no)\n")
    while start not in ('y','n'):
        start = input("Sorry, that wasn't a choice that you could make. Do you want to start using the calculator? (again, enter y for yes and n for no)\n")
    
    if start == 'y':
        first_integer, second_integer = collect_numbers()
        bigger_integer, smaller_integer = int_size_decider(first_integer, second_integer)
        gcd = find_gcd(bigger_integer, smaller_integer)
    elif start == 'n':
        print('I see. Goodbye then!')


if __name__ == "__main__":
    main()