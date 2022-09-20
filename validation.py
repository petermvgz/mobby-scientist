MARKUP = 2.5
another = 'y'

while another == 'y' or another == 'y':
    wholesale = float(input('The items wholesale cost: '))

    while wholesale < 0:
        print(' Error: the cost can not be negative.')
        wholesale = float(input('Enter the correct wholesale cost: '))
    retail = wholesale * MARKUP

    print('Reatil price $',retail)

    another = input('Do you have another item? (Enter y for yes):')