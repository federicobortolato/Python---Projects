#sao_game_class

from useful_functions import *
from startup import base_game_mechanics


class The_game(base_game_mechanics):


    def check_sex(self):
        while True:
            sex = input('\n-Are you male[m] or female[f]-?\n')
            sexes = ['m','f']
            types = ['boy','girl']
            if sex.lower().strip() in sexes:
                okay = input(stringy(f'-So you are a {types[sexes.index(sex)]}[y/n]?-'))
                if okay == 'y':
                    return sex
                elif okay == 'n':
                    print(stringy("-Are you kidding me?-"))
                    pass
                else:
                    print(stringy('-Come oon...I won\'t eat you...-'))
                    pass


    def check_name(self):
        name = input(stringy("-What's your name?-"))
        alf = 'abcdefghijklmnopqrstuvwxyz '
        for i in name:
            if i.lower() not in alf:
                print("\n-I'm sure that's not your name, tell me what your name truly is! [only alphabet letters]\nSo...-\n")
                name = self.check_name()
                break
            else:
                pass
        return name


    def night_save(self , data = None):
        while True:
            alert = input(stringy("[It's night and you are sleeping like a child. Well, in fact, you are one. \
Anyway, would you like to save?[y/n] You may lose your game data otherwise. ]"))
            if alert.lower() == 'y':
                self.saving(data)
                break
            elif alert.lower() == 'n':
                prints('You take your own risks')
                break
            else:
                prints('Invalid input.')
                pass
        while True:
            alert = input(stringy('[Would you prefer to sleep[s] till dawn or to exit[e] the game for a while?]'))
            if alert.lower() == 's':
                break
            elif alert.lower() == 'e':
                self.quit()
            else:
                prints('Invalid input.')
                pass
