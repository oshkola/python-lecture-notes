print "EXERCISE 13. Parameters, Unpacking, Variables"
print "." * 53

from sys import argv #add module sys
# argv - argument variable

script, first, second = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
#print "Your third variable is:", third

# Run it with python ex_13.py name1 name2 name3
print "." * 53, "\n"