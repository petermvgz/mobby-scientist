mass = float(input('How much is the mass of your object?: '))
weight = mass * 9.8
if weight >= 500:
    print('Object is too heavy!')
else:
    if weight <= 100:
        print('Object not over weight')

# Program that tells you whether an object is overweight or not, max = 500, min = 100
