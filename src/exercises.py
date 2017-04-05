from dictionary_class import *
import re
from time import clock

filePath = "../project-exercises/"
fileName_definitions = "definitions.csv"
fileName_dictionary = "dictionary.csv"
fileName_words = "words.txt"



#number_of_words = 10000
num_dictionary_lines = sum(1 for line in open(filePath + fileName_dictionary)) -1 # skip counting header
num_definitions_lines = sum(1 for line in open(filePath + fileName_definitions)) -1 # skip counting header
num_words_lines = sum(1 for line in open(filePath + fileName_words))
dictionary_lines = 0
definitions_lines = 1
words_lines = 2

for number_of_lines in [[100,100,100], [1000,1000,1000], [2500, 2500, 2500],  [5000, 5000, 5000], [10000, 10000, 10000],
                        [num_dictionary_lines, num_definitions_lines, num_words_lines]]:

    fail_edit = 0
    success_edit = 0
    fail_search = 0
    success_search = 0
    fail_delete = 0
    success_delete = 0

    print '#############################################################################################################'
    print '#############################################################################################################'

    print 'Number of dicionary words: ', number_of_lines[dictionary_lines]
    start_clock = clock()

    dict = Dictionary()
    # add words from dictionary.csv
    print 'Reading words and definitions from dictionary.csv'
    dict.read_words_from_CSV(filePath, fileName_dictionary, number_of_lines[dictionary_lines])
    end_clock_1_read = clock()
    #print '___________________________________________________________________________________________________________'
    #print '___________________________________________________________________________________________________________'

    print 'Edit definitions using definitions.csv'
    # edit definitions using definitions.csv
    with open(filePath + fileName_definitions,'r') as f:
        # skip header line
        f.readline()
        for n in xrange(0, number_of_lines[definitions_lines]):
            line = f.readline()
            (word, definition) = line.split(',', 1)
            word = re.sub(r'^"*|"*$', '', word)
            definition = re.sub(r'^"*|"*\n', '', definition)
            results = dict.edit_definition(word,1,definition)
            if results[0] is True:
                success_edit += 1
            else:
                fail_edit += 1

    end_clock_2_edit = clock()
    #print '___________________________________________________________________________________________________________'
    #print '___________________________________________________________________________________________________________'

    print 'Search for words using words.txt'
    # search words from words.txt
    with open(filePath + fileName_words,'r') as f:

        results = []
        for n in xrange(0,number_of_lines[words_lines]):
            word = f.readline()
            word = re.sub(r'^"*|"*\n', '', word)
            result = dict.get_word_and_definitions(word)
            if result[0] is True:
                success_search += 1
            else:
                fail_search += 1

    end_clock_3_search = clock()
    #print '___________________________________________________________________________________________________________'
    #print '___________________________________________________________________________________________________________'

    print 'Delete words using words.txt'
    # delete words from dictionary matching words.txt
    with open(filePath + fileName_words, 'r') as f:
        for n in xrange(0,number_of_lines[words_lines]):
            word = f.readline()
            word = re.sub(r'^"*|"*\n', '', word)
            result = dict.delete_word(word)
            if result[0] is True:
                success_delete += 1
            else:
                fail_delete += 1

    end_clock_4_delete = clock()
    #print '___________________________________________________________________________________________________________'
    #print '___________________________________________________________________________________________________________'
    print '##########################'
    print 'Start Time: ', start_clock
    print 'Time to add ', number_of_lines[dictionary_lines], ' words: ', end_clock_1_read - start_clock
    print 'Time to edit ', number_of_lines[definitions_lines], ' words: ', end_clock_2_edit - end_clock_1_read
    print 'Time to search ', number_of_lines[words_lines], ' words: ', end_clock_3_search - end_clock_2_edit
    print 'Time to delete ', number_of_lines[words_lines], ' words: ', end_clock_4_delete - end_clock_3_search
    print 'Total time: ', end_clock_4_delete - start_clock
    print '##########################'
    print 'Success edits : ', str(success_edit)
    print 'Fail edits : ', str(fail_edit)
    print 'Success search : ', str(success_search)
    print 'Fail search : ', str(fail_search)
    print 'Success delete : ', str(success_delete)
    print 'Fail delete : ', str(fail_delete)


    #raw_input("continue?")