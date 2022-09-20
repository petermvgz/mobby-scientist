A = 93
B = 90
C = 70
D = 60

score = int(input('Enter your test score: '))

if score >= A:
    print('Your grade is A')
else:
    if score >= B:
        print('Your grade B')
    else:
        if score >= C:
            print('Your grade is C')
        else:
            if score >= D:
                print('Your grade is D')
            else:
                print('Your grade is F')