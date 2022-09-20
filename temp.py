
MAX_TEMP = 102.5

temperature = float(input('Enter temperature in Celcius: '))

while temperature > MAX_TEMP :
    print('The temperature is too high')
    print('Turn the thermostat down and wait')
    print('5 minutes and take the temperature')
    print('wait again and enter it')
    temperature = float('Enter the new Celsius temperature: ')

print('The temperature is acceptable')
print('Check it again in 15 minutes')