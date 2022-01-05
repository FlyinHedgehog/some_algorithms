
# A program for the edit distance (lavenshtein distance) problem

import numpy as np
from tabulate import tabulate
from time import sleep

def min_edit_count(word1, word2):

    word1 = ' ' + word1     #
    word2 = ' ' + word2     # add a space before original words

    len_w1 = len(word1)     #
    len_w2 = len(word2)     # calculate the lengths of new words

    edit_matrix = np.zeros((len_w2, len_w1), dtype = int)
    # create a matrix with all zeros

    edit_matrix[0, :] = range(len_w1)  
    # assign numbers from 0 to len_w1 in the first row of the edit_matrix 
    edit_matrix[:, 0] = range(len_w2)
    # assign numbers from 0 to len_w2 in the first column of the edit_matrix 

    for i in range(1, len_w2):
        for j in range(1, len_w1):
            # edit_matrix[i-1][j] --> remove
            # edit_matrix[i][j-1] --> insert
            # edit_matrix[i-1][j-1] --> replace

            temp1 = edit_matrix[i-1][j] + 1
            temp2 = edit_matrix[i][j-1] + 1
            # add 1 to edit_matrix[i-1][j] and edit_matrix[i][j-1]

            temp3 = edit_matrix[i-1][j-1] + 1 if word1[j] != word2[i] else edit_matrix[i-1][j-1]
            # if last characters are same don't add 1 to edit_matrix[i-1][j-1].
            # no need to replace

            edit_count = min(temp1, temp2, temp3)
            # find min between three numbers
            edit_matrix[i][j] = edit_count

    min_edit = int(edit_matrix[len_w2 - 1, len_w1 - 1])
    # minimum edit count is the last number calculated
    
    return min_edit, edit_matrix

def get_words():

    original  = input('original word: ')
    edited = input('edited word: ')

    return original, edited

def create_table(edit_matrix, word1, word2):

    edit_table = np.empty((len(word2) + 2, len(word1) + 2), dtype = object)

    edit_table[0, 0:2] = ['*', "''"]
    edit_table[1][0] = "''"

    edit_table[2:(len(word2)+2), 0] = list(word2)
    edit_table[0, 2:(len(word1)+2)] = list(word1) 
    for i in range(len(word2) + 1):
        edit_table[i + 1, 1:len(word1)+2] = edit_matrix[i, :]

    edit_table = tabulate(edit_table, tablefmt = 'fancy_grid')

    return edit_table

def main():

    menu = '''
    Please choose:\n
    1 - calculate minimum edit distance
    2 - show minimum edit distance table
    Enter any other key to exit
    '''

    print(menu)
    choice = input('--> ')

    if choice == '1':
        word1, word2 = get_words()
        result = min_edit_count(word1, word2)[0]
        print(f'Minimum edit distance is {result}')
    elif choice == '2':
        word1, word2 = get_words()
        edit_matrix = min_edit_count(word1, word2)[1]
        min_edit_table = create_table(edit_matrix, word1, word2)
        print(min_edit_table)
    else:
        print('exiting...'); sleep(2)

    return 1


main()