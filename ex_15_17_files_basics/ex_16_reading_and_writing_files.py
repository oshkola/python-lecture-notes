print "EXERCISE 16. Reading and writing files"
print "." * 53
# close - closes the file.
# read - reads the content of the file
# truncate - empies the file
# write - writes stuff to the file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C ^C)."
print "If you do want that, hit RETURN."

raw_input("?")
print "\n"

print "Opening the file..."
target = open(filename, 'w') # w - write mode

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Mow I'm going to wtite these to the file."
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line2)
target.write("\n")

print "And finally, we close it."
target.close()
print "." * 53, "\n"