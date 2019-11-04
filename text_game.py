#   python project #1
#   alicisation game: system calling commands adventure

from sys import exit as exx


def exit():
    print("\nAs you wish. Come soon!")
    exx(0)

def turn_on():  #startup check
    start = input('Press A to enter the game\nPress B to turn off\n\n')
    if len(start) == 1:
        if start.lower() == 'a':
            pass
        elif start.lower() == 'b':
            exit()
        else:
            print('\nInvalid input. Reinitialize\n')
            start = turn_on()
    else:
        print('\nInvalid input. Reinitialize\n')
        start = turn_on()


turn_on()


"""
def loading(secs): #fancy fake loading
    from random import randint as rand
    from time import sleep

    ran = rand(0,secs)
    for r in range(ran):
        for x in range(3):
            print('.', end = '')
            sleep(1)
        print('\n')
"""
print('\nTHE ALICISATION PROJECT: LOADING\n')  #startup + fake loading

"""loading(3)"""

#login section
import json

def check_login_data(input_ , data, input_type):    #checks in the saved data if login and password credentials are correct
    if input_ == data:
        print('\nCorrect %s\n' % input_type)
    else:
        print('\nWrong %s. Try again\n' % input_type)
        raise TypeError



def login(data_user, data_pssw): #The login function
    print('\nLog in to your account\n')
    while True:
        try:
            input_user = input('\nPlease enter your username\n').strip()
            check_login_data(input_user, data_user, 'username')
            break
        except TypeError:
            pass
    while True:
        try:
            input_pssw = input('\nPlease enter your password\n').strip()
            check_login_data(input_pssw, data_pssw, 'password')
            break
        except TypeError:
            pass


def check_signup_data(input_ , data, input_type):    # checks if the user has
    if len(input_) < 2:
        print('\nShort %s. Try again\n' % input_type)
        raise TypeError
    else:
        if input_ == data:
            print('\nCorrect %s\n' % input_type)
        else:
            print('\nWrong %s. Try again\n' % input_type)
            raise TypeError

def saving():
    with open('sao_game_data_save.json', 'w') as file:
        json.dump(game_data , file , indent = 8 , separators = (', ' , ': ') , sort_keys = True)

def sign_up(): #creates the saving file
    print('\nRegister your new account\n')
    while True:
        try:
            input_user_1 , input_user_2 = input('\nPlease enter your username\n').strip() , input('\nNow please double check your username\n').strip()
            check_signup_data(input_user_1, input_user_2, 'username')
            break
        except TypeError:
            pass
    while True:
        try:
            input_pssw_1 , input_pssw_2 = input('\nPlease enter your password\n').strip() , input('\nNow please double check your password\n').strip()
            check_signup_data(input_pssw_1, input_pssw_2, 'password')
            break
        except TypeError:
            pass
    global game_data
    game_data = {'username': input_user_1 , 'password': input_pssw_1}
    saving()

def reset(file):  #deletes the saving file
    import os
    os.remove(file)
    print('\nData reinitialized.\n')

try:
    with open('sao_game_data_save.json', 'r') as file:
        game_data = json.load(file)
    saved_username = game_data['username']
    saved_password = game_data['password']

    def data_save_try():
        ok = input('\nGame data found. Join in or reset?\n           \
\nPress J to login. Digit "Reset" [without quotation marks, with Capital R] to reset\n')
        if ok.lower() == 'j':
            login(saved_username, saved_password)
        elif ok == 'Reset':
            login(saved_username, saved_password)
            reset('sao_game_data_save.json')
            sign_up()
        else:
            print('\nRequest denied, invalid input. Please select the correct input.\n' )
            data_save_try()
    data_save_try()

except FileNotFoundError :
    print('\nGame data not found. A new game will start.\n')
    sign_up()
except json.JSONDecodeError :
    print('\nGame data damaged. Previous data will be deleted and a new game will start.\n')
    reset('sao_game_data_save.json')
    sign_up()
finally:
    print('\nWelcome to the Underworld\n')


#_________________
#some useful funcs
#_________________



def printy(s):
    print('\n' + ' '*8  + '='*len(s) + '\n'+ ' '*8 + s + '\n' + ' '*8 + '='*len(s) + '\n')

def stringy(j):
    j = '\n' + j + '\n'
    return j

def dstringy(j):
    j = stringy(stringy(j))
    return j

def prints(j):
    print(stringy(j))

def print2s(j):
    print(dstringy(j))

def chappy(n):
    return 'Chapter' + str(n)

def pchan(x):
    printy(chappy(x))

#---------------
#The game starts

if 'chapter' not in game_data:
    game_data['chapter'] = 0

if game_data['chapter'] == 0:
    pchan(0)
    alf = 'abcdefghijklmnopqrstuvwxyz '
    print(stringy('Outside\'s raining... you are all wet and cold. You\'re wearing only an old hemp sack sewed togheter... \
while knocking on the orphanotrophy door, you\'re trembling. \
A pretty lady opens the door.\n-What are you doing there?- she asks. -My parents died in the fire that reached our \
farm a few days ago. I\'m alone now-. -Come in- the woman says.\nShe takes you to the canteen and offers you a warm soup. While \
checking you out she can\'t tell if you\'re a boy or a girl, probably your short hair and your young face confuses her.'))

    def check_sex():
        sex = input('\n-Are you male[m] or female[f]-?\n')
        if sex.lower() == 'm':
            okay = input(stringy('-So you are a boy[y/n]?-'))
            if okay == 'y':
                sex = 'male'
                game_data['sex'] = sex
            elif okay == 'n':
                print(stringy("-Are you kidding me?-"))
                check_sex()
            else:
                print(stringy('-Come oon...-'))
                check_sex()
        elif sex.lower() == 'f':
            okay = input('-So you are a girl[y/n]?-')
            if okay == 'y':
                sex = 'female'
                game_data['sex'] = sex
            elif okay == 'n':
                print(stringy("-Are you kidding me?-"))
                check_sex()
            else:
                print(stringy('-Come oon...-'))
                check_sex()
        else:
            print(stringy('-Come oon...-'))
            check_sex()
    check_sex()

    print(stringy('She seems quite anxious. While giving you a glass with some red-purple-like liquid inside she tells you to drink it. \
-It will warm you-. Beside the strong smell, it\'s not that bad and you immediately feel a fire flowing from your stomach to your head. \
She sits in front of you and watches you eating for some time.'))
    def check_name():
        name = input(stringy("-What's your name?-"))
        for i in name:
            if i.lower() not in alf:
                print("\n-I'm sure that's not your name, tell me what your name truly is! [only alphabet letters]\nSo...-\n")
                name = check_name()
                break
            else:
                pass
        return name

    name = check_name()
    game_data['name'] = name
    prints(f'-Stay here-. She goes out of the room. You can hardly listen to her speaking with some other woman, probably older. \
After a while she comes back. -Ok {name}, we\'ll let \
you stay here for the night-. The sun has already gone, so she takes you to a free bed in the dormitory. -\'Night- and leaves you alone with some other guys, \
already sleeping')
    game_data['chapter'] = 1

#do you want to save

    while True:
        alert = input(stringy("[It's night and you are sleeping like a child. Would you like to save?[y/n] \
You may lose your game data otherwise. ]"))
        if alert.lower() == 'y':
            saving()
            break
        elif alert.lower() == 'n':
            prints('You take your own risks')
            break
        else:
            prints('Invalid input.')
            pass

#continue or quit

    while True:
        alert = input(stringy('[Would you prefer to sleep[s] till dawn or to exit[e] the game for a while?]'))
        if alert.lower() == 's':
            break
        elif alert.lower() == 'e':
            exit()
        else:
            prints('Invalid input.')
            pass

if game_data['chapter'] == 1:
    pchan(1)

"""
if game_data['chapter'] == 2:
if game_data['chapter'] == 3:
if game_data['chapter'] == 4:
if game_data['chapter'] == 5:
if game_data['chapter'] == 6:
"""
#save name in game data

print('executed')
