import time
'''
print('WELCOME TO STOP_WATCH V1')
time.sleep(1)
user_input = int(input('Minute stopwatch - Enter number in minutes: '))
converted = user_input * 60
for x in range(converted, 0, -1):
    print(x, 'seconds')
    time.sleep(1)
    x -= 1
print('Timer completed')
'''
print('WELCOME TO STOP_WATCH V1')

user_input = int(input('Minute stopwatch - Enter number in minutes: '))
converted = user_input * 60
while converted != 0:
    print(converted, 'seconds')
    time.sleep(1)
    converted -= 1
print(converted, 'seconds')
print('Timer completed')
    
