import time
import os


def clear():
    command = 'cls'
    os.system(command)


def fightscene():
    fight = input('choise')
    if fight == 'sword':
        print('you pick sword')
    elif fight == 'gun':
        print('you pick gun')
    else:
        ('didnt understand')
        return fightscene()


enter = input('enter the castle?')
if enter == 'yes':
    print('entered')
    time.sleep(1)
    clear()
    print('door')
    door = input('enter?')
    if door == 'yes':
        print('entered')
        time.sleep(1)
        clear()
        print('fight spiders')
        print('sword/gun')
        fightscene()
        h = input('')
        if h == 'yes':
            print('good')
        else:
            print('die')
    else:
        print('game over')
        g = input('')
        if g == 'yes':
            print('good')
        else:
            print('die')
else:
    print('got shot')