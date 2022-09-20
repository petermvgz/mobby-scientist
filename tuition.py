print('tuition --- increase every year')
print('-----------------------------')

for YEARS in range(1,6):
    tuition = 8000
    tuitionIST = 8000 * 1.03 ** YEARS
    print(tuition,'\t',tuitionIST)
# tuition is increased from 8000 by 3% every year