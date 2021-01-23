# code to rename a slippi file based off of the characters in the game

# just some testing stuff to remember how python works

import random
import os
# import slippi
from slippi import Game
import re

characters = ['falcon', 'doc', 'luigi', 'marth', 'mario', 'sheik', 'ganondorf', 'zelda', 'pikachu', 'pichu']


'''for num in range(10):

    print(random.choice(characters))'''


def main(directory):
    #renames files in a given directory with a random melee character + a number at the end
    for count, filename in enumerate(os.listdir(directory)):
        print('filename:', filename)
        new_filename = random.choice(characters) + str(count) + ".slp"
        og_filename = 'C:\\Users\\talen\\Desktop\\testfolder\\' + filename
        new_filename = 'C:\\Users\\talen\\Desktop\\testfolder\\' + new_filename

        print ('new_filename:', new_filename)
        print ('og_filename:', og_filename)
        # rename() function will
        # rename all the files

        os.rename(og_filename, new_filename)


def get_info(given_slippi_file):
    # tries to rename a specific hard-coded slippi file based off of info from within the file
    # filename =
    # slippifile = Game('C:\\Users\\talen\\Desktop\\testfolder\\realgame.slp')
    slippifile = Game(given_slippi_file)
    slippifile.frames[0]
    player1_name = slippifile.metadata.players[0].netplay.name
    player2_name = slippifile.metadata.players[1].netplay.name
    # uses regular expressions to remove forbidden characters that may appear in your filename accidentally
    # looking at you "ttv/tweekssb"...

    player1_name = re.sub(r'[\\/*?:"<>|]',"",player1_name)
    player2_name = re.sub(r'[\\/*?:"<>|]', "", player2_name)
    game_datetime = slippifile.metadata.date
    stagestr = slippifile.start.stage
    stage = str(stagestr).split('.')[1]
    #print(game_datetime.date())
    #print(game_datetime.time())
    formatted_datetime = (str(game_datetime.date()) + ' ' + str(game_datetime.time())).replace(':', '')
    #print ('player1_name:', player1_name)
    #print ('player2_name:', player2_name)
    #print(slippifile)
    #print('---')
    #gets character names from both players
    character_names = []
    #for num in range(2):
    num=0
    #print ('slippifile.metadata.players:', slippifile.metadata.players)
    #print ('slippifile.metadata.players[0]', slippifile.metadata.players[0].characters)

    '''probably update this section to be more efficient later lol'''
    for key in slippifile.metadata.players[0].characters:
        #print ('key:', key)
        #print(slippifile.metadata.players.characters)
        char_name = str(key).split('.')[1]
        character_names.append(char_name)

    for key in slippifile.metadata.players[1].characters:
        #print ('key:', key)
        #print(slippifile.metadata.players.characters)
        char_name = str(key).split('.')[1]
        character_names.append(char_name)

    # print(character_names)
    player1_char = character_names[0]
    player2_char = character_names[1]
    #print('stage:', stage)
    formatted_file_name = '{} ({}) vs {} ({}) - {} - {}'.format(player1_name, player1_char, player2_name, player2_char, stage, str(formatted_datetime))
    return formatted_file_name


    # print(slippifile.metadata.players[0].characters[0])


def rename_slippi_files(directory):

    # renames files in a given directory with a random melee character + a number at the end
    for count, filename in enumerate(os.listdir(directory)):
        #print('filename:', filename)

        #new_filename = random.choice(characters) + str(count) + ".slp"
        og_filename = directory + '\\' + filename
        full_filepath = directory + '\\' + filename
        new_filename = directory + '\\' + get_info(full_filepath) + '.slp'

        #print('full_filepath:', full_filepath)
        #print('new_filename:', new_filename)
        #print('og_filename:', og_filename)
        # rename() function will
        # rename all the files

        os.rename(og_filename, new_filename)




if __name__ == '__main__':
    # Calling main() function
    # main("C:\\Users\\talen\\Desktop\\testfolder")
    # get_info('C:\\Users\\talen\\Desktop\\testfolder\\realgame.slp')
    #directory = str(input('Please input the folder path that contains your slippi files you wish to rename'))
    #rename_slippi_files(directory)

    rename_slippi_files('C:\\Users\\talen\\Desktop\\testfolder')


