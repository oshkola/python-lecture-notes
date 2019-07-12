print "EXERCISES 1 and 2. Printing out and commenting out the code"
print '.....................................................'
print "Hello World!"
print 'Yay! Printing.'
print "I'd much rather you 'not'"
print 'I "said" do not touch this'
# The comment; Anything after # is ignored
print "# is not treated as a comment as it is inside the string  "
print '......................................................'


print "#EXERCISE 3. Numbers and math"
print '.....................................................'
print "2 + 2 :"
print 2 + 2

print "2 - 2 :"
print 2 - 2

print "2 * 2 :"
print 2 * 2

print "10 / 4 :"
print 10 / 4

print "10.0 / 4.0 :"
print 10.0 / 4.0

print "10 % 4 :"
print 10 % 4

print "3 + 2 > 5"
print 3 + 2 > 5

print "3 + 2 >= 5"
print 3 + 2 >= 5

print "What is 5 -7 ?", 5-7
print "is 5 greater than 7 ?", 5 > 7

# One can simply type "python" on terminal and use Python as a calculator
print '.....................................................'


print "EXERCISE 4. Variables and names"
print '.....................................................'
cars = 100
space_in_a_car = 4.0
drivers = 20
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "car available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "passengers today"
print "We have", passengers, "passengers today"
print "We need to put about", average_passengers_per_car, "people in each car"
print '.....................................................'


print "EXERCISE 5. More variables and printing"
print '.....................................................'
# Everything that is in " "  or ' ' is a string
my_name = 'Oleh Shkola'
my_name_1 = "Oleh Shkola"

print my_name
print my_name_1

my_height_cm = 172
my_weight_kg = 85

my_eyes = 'Grey'
my_hair = 'Black'

print "let's talk about %s" % my_name
print "I am %d cm tall" % my_height_cm
print "I am %d kg heavy" % my_weight_kg
print "I've got %s eyes and %s hair" % (my_eyes, my_hair)
print "If I add %d and %d , I get %d" % (my_height_cm, my_weight_kg, my_weight_kg + my_height_cm)

# some more format characters
# $d, %i - Signed integer decimal.
# %u Unsigned decimal
# %f, %F - Floating point decimal format.
# %e - Floating point exponential format (lowercase).
# %E - Floating point exponential format (uppercase).
# %r - String (converts any python object using repr()).
# %x - Unsigned hexadecimal (lowercase).
# %o - Unsigned octal.

print "Once again using 'r' format character : %r + %r makes %r" % (my_height_cm, my_weight_kg, my_weight_kg + my_height_cm)

my_weight_lb = my_weight_kg * 2.2046
print "My weight in lb is %f" % my_weight_lb
print "My weight in lb in exp form %e" % my_weight_lb

print "Lets round 3.14 : %f" % round(3.14)
print '.....................................................'


print "EXERCISE 6. Strings and text"
print '.....................................................'
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"


# string is inside another string here
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said %r" % x
print "I also said : '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

print w + e
print '.....................................................'

print "EXERCISE 7. More printing"
print '.....................................................'
print "Marry had a little lamb"
print "Its fleece was white as %s" % "snow"
print "And everywhere that Mary went."
print "." * 10 # prints "." 10 times on the same line

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# comma makes those two printings at the same line
print end1 + end2 + end3 + end4 + end5 + end6, 
print end7 + end8 + end9 + end10 + end11 + end12

print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12
print '.....................................................'


print "EXERCISE 8. Printing, printing"
print "." * 53
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."

	)
print "." * 53


print "EXERCISE 9. Printing, printing, printing"
print "." * 53
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months, "\n"
print "Here are the months: %r" % months
print "\n"
print """
There's something going on here.
With the three double-quotes. 
We'l be able to type as much as we like.
"""
print "." * 53, "\n"


print "EXERCISE 10. What was that?"
print "." * 53
print "I am 6'2\" tall."
print 'I am 6\'2" tall. \n'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
#	for i in ["/","- ","|","\\","|"]:
#		print "%s\r" % i,

print "." * 53