MIN_SALARY = 45000
MIN_YEARS = 2

salary = float(input('Enter your yearly salary: '))
years_on_job = float(input('Enter years on the job: '))

if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
        print('You QUALIFY for loan!')
else:
        print('Sorry, You do  not QUALIFY for loan.')

