print "EXERCISE 18. Names, Variables, Code, Functions"
print "." * 53

# this one looks like a previous script with argv
def print_two(*args):
	# is not a pointer; * means that print_two takes unlimited number of arguments
	# and I do not know how many of them will be in the end
	arg1, arg2, arg3 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# another function that takes only 2 arguments
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this one takes only one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes nothing
def print_none():
	print "I got nothing."


print_two("one", "two", "three")
print_two_again("one", "two")
print_one("first")
print_none()		


print "." * 53, "\n"