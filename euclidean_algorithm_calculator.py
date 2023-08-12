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

def collect_polynomials():
    gather_two_polynomials = False

    while not gather_two_polynomials:
        first_polynomial = input('Please enter the first polynomial you want to find the GCD of written in descending power, with no spaces between terms and operations. An example would be: 5x^4+4x^3-10x^2+54\n')
        second_polynomial = input('Please enter the second polynomial you want to find the GCD of written in descending power, in a form similar to the one you just gave.\n')

def collect_modulo():
    gather_modulo = False

    while not gather_modulo:
        modulo = input("Since the polynomials are in a field F[x], what is x? That is, what is the modulo?")
        try:
            modulo = int(modulo)
        except ValueError:
            print("That is not a valid response.")
        else:
            print("Good to know!")
            gather_modulo = True
    return modulo

def poly_size_decider(first_polynomial, second_polynomial):
    higher_power_poly = None
    lower_power_poly = None
    return higher_power_poly, lower_power_poly
def main():
    print("Hi! This is a calculator that uses and displays the Euclidean Algorithm of finding the Greatest Common Divisor (GCD) of two given integers or polynomials!")
    start = input("For now, do you want to start using the calculator? (enter y for yes and n for no)\n")
    while start not in ('y','n'):
        start = input("Sorry, that wasn't a choice that you could make. Do you want to start using the calculator? (again, enter y for yes and n for no)\n")
    
    if start == 'y':
        polynomial = None
        while polynomial not in (True, False):
            answer = input('Do you want to use the Integer or Polynomial mode? (enter 1 for integer, 2 for polynomial)')
            if answer == '1':
                polynomial = False
            if answer == '2':
                polynomial = True
            else:
                print('Invalid answer.')
        if polynomial == False:
            print("Got it!")
            first_integer, second_integer = collect_numbers()
            bigger_integer, smaller_integer = int_size_decider(first_integer, second_integer)
            gcd = find_gcd(bigger_integer, smaller_integer)
        elif polynomial == True:
            print("Understood!")
            field = None
            while field not in (True, False):
                reply = input('Is this polynomial in a field (F[x])? (y for yes, n for no)')
                if reply == 'y':
                    field = True
                elif reply == 'n':
                    field = False
                else:
                    print('Invalid answer.')
            print("Okay!")
            first_polynomial, second_polynomial = collect_polynomials()
            if field == True:
                modulo = collect_modulo()
            higher_power_poly, lower_power_poly = poly_size_decider(first_polynomial, second_polynomial)
                
        else:
            print("This shouldn't be happening.")
    elif start == 'n':
        print('I see. Goodbye then!')


if __name__ == "__main__":
    main()
