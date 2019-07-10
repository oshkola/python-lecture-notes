print "EXERCISE 21. Functions can return something"
print "." * 53
# "return" a value from the dunction

def add(a, b):
	print "Adding %d and %d" % (a, b)
	return a+b

def subtract (a, b):
	print "Subtracting %d from %d" % (a, b)
	return a - b


print "\n"

height = add(70, 23)
print "Height = ", height
print "\n" 

weight = subtract (700, 40)
print "Weight = ", weight
print "\n"

print "sum of the %i and %i :" % (height, weight)
print height + weight
print "\n"


print "Here is a puzzle."

what = add(height, subtract(weight, add(height, weight)))
print "what?: ", what

print "." * 53, "\n"