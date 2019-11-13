#   The_game


from The_game_mechanics import The_game
from useful_functions import *

game = The_game('The_game')

game.turn_on()

game.reading('THE ALICISATION PROJECT: LOADING')

game.fake_loading(3)

game.start()


#---------------
#The game starts


if 'chapter' not in game.data:
    game.data['chapter'] = 0
    game.check_text_speed()

if game.data['chapter'] == 0:
    pchan(0)

    game.extracting_preparatory()
    game.reading(game.text_extracting())

    sex = game.check_sex()
    game.data['sex'] = sex


    game.reading(game.text_extracting())
    name = game.check_name()
    game.data['name'] = name


    game.reading(game.text_extracting().format(name))
    game.data['chapter'] = 1


    game.night_save()


if game.data['chapter'] == 1:
    pchan(1)
