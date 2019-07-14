
numbers = [1, 2, 3, 4, 5, 6, 7]

for i in range (0, 7):
	print "number %d : %d" % (i, numbers[i])

numbers.append(9)
print "append 9. Print the list again:"

for i in range (0, 8):
	print "number %d : %d" % (i, numbers[i])

print "extend [4, 5]. Print the list again:"
numbers.extend([4, 5])

print numbers

numbers.insert(0, 7)
print "insert (0,7) and print again:"
print numbers

numbers.remove(4)
print "erase 4 and print:"
print numbers

#erase(x) removes the first element that is equal to x 

numbers.pop(3)
print "pop the 3rd element:"
print numbers
print "pop(x) returns the value of x-th element:"
print numbers.pop(3)


print "numbers.count(5) - counts the number of times that 5 appears in the list:"
print numbers.count(5)
print numbers

print "numbers.index(x) returns the index of the first element which value is equal to x"
print "numbers.index(2): " , numbers.index(2)


#Actually, the clear() was added in python starting from 3.3
#print "Let's clear the list now and print it again:"
#numbers.clear()
#print "numbers" , numbers