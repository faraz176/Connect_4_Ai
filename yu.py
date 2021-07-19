import random


list_of_weathers = ['Snowing', 'Hailing', 'Clear', 'Thunderstorm']
num = random.randint(0, len(list_of_weathers)-1)
weather = list_of_weathers[num]

if weather == 'Snowing':
    print('Making Snowman')
elif weather == 'Hailing':
    print('Ice is falling')
elif weather == 'Clear':
    print('Go outside')
elif weather == 'Thunderstorm':
    print('The old man is snoring')    
else: print("It isn't that cold outside")    



