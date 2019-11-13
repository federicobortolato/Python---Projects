#startup

from sys import exit
from random import randint as rand
from time import sleep
from os import remove
from json import dump , load , JSONDecodeError
from useful_functions import *

class base_game_mechanics():
    """ Some base game mechanics methods"""

    def __init__(self,game):
        self.name = game
        self.save_file = game + '.json'
        self.data = {}
        self.text_speed = 3

    def quit(self):
        self.reading("As you wish. Come soon!")
        exit(0)


    def turn_on(self):
        starting = input(stringy(f'Press A to enter {self.name}\nPress B to turn off\n')).strip()
        if starting.lower() == 'a':
            pass
        elif starting.lower() == 'b':
            self.quit()
        else:
            self.reading('Invalid input. Reinitialize')
            start = self.turn_on()


    def fake_loading(self,secs):
        ran = rand(0,secs)
        for r in range(ran):
            for x in range(3):
                print('.', end = '')
                sleep(1)
            print('\n')


    def check_data(self, data_1 , data_2 , data_type):
        if data_1 == data_2 :
            self.reading('Correct %s' % data_type)
        else:
            self.reading('Wrong %s. Try again' % data_type)
            raise ValueError


    def log_inputs(self,name, data_1):
        while True:
            try:
                data_2 = input(stringy('Please enter your %s' % name)).strip()
                self.check_data(data_1,data_2,name)
                break
            except ValueError:
                pass


    def login(self, data_user, data_pssw):
        self.reading('Log in to your account')
        self.log_inputs('username',data_user)
        self.log_inputs('password',data_pssw)


    def signup_inputs(self,name):
        while True:
            try:
                data_1 = input(stringy('Please enter your %s' % name)).strip()
                if len(data_1) < 3:
                    self.reading('Short %s [required >2] Try again' % name)
                    raise ValueError
                data_2 = input(stringy('Now please double check your %s' % name)).strip()
                self.check_data(data_1, data_2, name)
                break
            except ValueError:
                pass
        return data_1


    def sign_up(self):
        self.reading('Register your new account')
        username = self.signup_inputs('username')
        password = self.signup_inputs('password')
        self.data = {'username': username , 'password': password}
        self.saving()



    def reset(self, file = None):
        if not file:
            file = self.save_file
        remove(file)
        self.reading('Data reinitialized.')


    def saving(self , data = None , file = None):
        if not file:
            file = self.save_file
        if not data:
            data = self.data
        with open(file, 'w') as file:
            dump(data , file , indent = 8 , separators = (', ' , ': ') , sort_keys = True)


    def loading(self , file = None):
        if not file:
            file = self.save_file
        with open(file, 'r') as file:
            self.data = load(file)


    def start(self):
        try :
            self.loading()
            username , password , text_speed = self.data['username'] , self.data['password'] , self.data['text_speed']
            self.text_speed = text_speed
            while True :
                ok = input(stringy("Game data found. Join in or reset?\n  \
\nPress J to login. Digit 'Reset' [without quotation marks, with Capital R] to reset"))
                if ok.lower() == 'j' :
                    self.login(username , password)
                    break
                elif ok == 'Reset' :
                    self.login(username , password)
                    self.reset()
                    self.sign_up()
                    break
                else:
                    pass
        except FileNotFoundError :
            self.reading('Game data not found. A new game will start.')
            return self.sign_up()
        except (JSONDecodeError , KeyError) :
            self.reading('Game data damaged. Previous data will be deleted and a new game will start.')
            self.reset()
            return self.sign_up()
        finally :
            self.reading(f'Welcome into the world of {self.name}')


    def reading(self , text , speed = None):
        if not speed:
            speed = self.text_speed
        print('\n')
        for x in text:
            print(x , end = '')
            sleep(speed/100)
        print('\n')

    def check_text_speed(self):
        self.reading('[Please choose your text speed: here three examples:]')
        sleep(2)
        self.reading('[slow] Once upon a time, there was a little girl who lived in a village near the forest. \
Whenever she went out, the little girl wore a red riding cloak, so everyone in the village called her Little Red Riding Hood.' , 5)
        sleep(2)
        self.reading('[medium] One morning, Little Red Riding Hood asked her mother if she could go to visit her grandmother \
as it had been awhile since they\'d seen each other.' , 3)
        sleep(2)
        self.reading('[fast] "That\'s a good idea," her mother said.  So they packed a nice basket for Little Red Riding \
Hood to take to her grandmother.', 1)
        sleep(2)
        while True:
            speed = input(stringy('[Now choose your text speed, where 1 is the fastest and 5 the slowest:]'))
            try:
                speed = int(speed)
                if 1 <= speed <= 5:
                    self.text_speed = speed
                    self.data['text_speed'] = speed
                    self.reading('Enjoy this text game!')
                    break
            except ValueError:
                self.reading('Invalid input [only integers]')

    def extracting_preparatory(self , file = None):
        if not file:
            file = 'chapter' + str(self.data['chapter']) + '.txt'

        def line_yielder(file):
            with open(file) as fp:
                for line in fp:
                   yield line

        self.line_yielder = line_yielder

        a = self.line_yielder(file)

        def extracting():
            b = ''
            try:
                while True:
                    c = next(a)
                    b += c
                    if c == '\n':
                        return b
            except StopIteration:
                prints(f'ERROR: 1) please look for text corruption in {file};\n\
2) please notice that at the end of the last text one blank line must \
be left and one only\n3) please check that number of texts and number \
of iteration are the same')

        self.text_extracting = extracting
