print "EXERCISE 19. Functions and variables"
print "." * 53
def apples_and_pears(apples_count, pears_count):
	print "You have %d apples" % apples_count
	print "You have %d pears" % pears_count
	print "get a blanket \n"

print "we can pass the numbers to the function directly:"
apples_and_pears(20, 30)

print "OR we can use variables from our script:"
number_of_apples = 20
number_of_pears = 30
apples_and_pears(number_of_apples, number_of_pears)

print "We can even do math inside of the function call:"
apples_and_pears(10 + 10, 20 + 10)

print "And we can combine variables and math:"
apples_and_pears(number_of_apples + 20, number_of_pears - 10)

print "." * 53, "\n"