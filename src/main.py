## this is the main entry for the program
# read dictionary.csv from project exercises
# operations: Search, add, delete, edit the definition
import re
import os


fileName = "dictionary.csv"
filePath = "../project-exercises/"

# Reading dictionary.csv
d = {}
with open(filePath + fileName) as f:
    # skip header line
    f.readline()
    for line in f:
       (key, val) = line.split(',',1)
       key = re.sub(r'^"*|"*$', '', key)
       val = re.sub(r'^"*|"*\n','',val)
       if d.has_key(key):
           d[key] = d[key] + [val]
       else:
           d[key] = [val]

#writing to our dictionary
fileName = "dictionary.csv"
filePath = "../data/"
if not os.path.exists(filePath):
    os.makedirs(filePath)
with open(filePath + fileName, 'w+') as f:
    for word in d:
        for defination in d[word]:
            f.writelines(word + ',' + defination + '\n')
    #for word in d:
     #       f.writelines(word)
'''
# print word defination(s)
i = 0
for defination in d['word']:
    i+=1
    print str(i) + "\t" + defination
'''