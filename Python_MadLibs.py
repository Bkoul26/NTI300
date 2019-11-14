#Bogdan Koul
#11/09/2019
#NTI 300
#Start
#!/usr/bin/python

import re

#Open Madlibs
madLibs = open("..\\MadLibs.txt")
content = madLibs.read()
madLibs.close()
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
# While Loop to check & go through the words needed to change
while True:
    result = check.search(content)
    if result == None:
        break
    if result.group() == "ADJECTIVE" or result.group() == "ADVERB": #conditional for input
        print("Enter an %s:" % (result.group().lower()))
    elif result.group() == "NOUN" or result.group() == "VERB":
        print("Enter a %s:" % (result.group().lower()))
    i = input()
    content = check.sub(i, content, 1)
print(content)
#Menu to choose file na,me
print("Name your file:")
name = input()
newFile = open("..\\%s.txt" % (name), "w")
newFile.write(content)
#end()
#create new file error
