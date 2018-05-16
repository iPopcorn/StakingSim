import random

numberPerAttempt = int(input('Tests per attempt: '))
prob = float(input('What is the chance? Enter a decimal: '))
totalAttempts = int(input('Total Attempts: '))
baseNumber = int(input('How much money to start with: '))
flipNumber = float(input('flip: '))

rand = 0
i = 0
count = 0
success = 0
totalSuccesses = 0
totalFails = 0
flip = flipNumber
max = 0
min = 999999999
while count < totalAttempts:
    if baseNumber > 0:
        while i < numberPerAttempt:
            rand = random.randint(0, 100)
            if prob >= rand:
                print('FLIP: ' + str(flip) + ' baseNumber: ' + str(baseNumber))
                success += 1
                baseNumber += flip
                flip = flipNumber
                break
            else:
                baseNumber -= flip
                flip = flip * 2
            i += 1
        if success > 0:
            totalSuccesses += 1
        else:
            totalFails += 1
            print('Cleaned. Stack: ' + str(baseNumber))
    if baseNumber > max:
        max = baseNumber
    if baseNumber < min:
        min = baseNumber

    flip = flipNumber
    success = 0
    count += 1
    i = 0

print('FLIP: ' + str(flip) + ' baseNumber: ' + str(baseNumber))
print('Total Successes: ' + str(totalSuccesses) + ' Total Fails: ' + str(totalFails))
print('Max Stack: ' + str(max) + str(min))
