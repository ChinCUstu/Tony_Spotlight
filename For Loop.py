START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = .6214

print('KPH\t\t\tMPH')
print('--------------')
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t\t', format(mph, '.1f'))
