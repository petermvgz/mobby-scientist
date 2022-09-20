BASE_HOURS = 40

OT_MULTIPLIER = 1.5

hours = float(input('Enter number of hours works in a week: '))
pay_rate = float(input('Enter your hourly pay rate' ))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    gross_pay = BASE_HOURS * pay_rate

print('The Gross pay is $', format(gross_pay, '.2f'))
