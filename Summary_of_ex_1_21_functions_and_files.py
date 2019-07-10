def write_into_file(filename, in_data):
	file = open(filename, 'a') # 'a' - append
	file.write(in_data)
	file.close()

def print_all(filename):
	file = open(filename, 'r')
	print file.read(), "\n" 

def print_line_from_file(line_count, filename):
	file = open(filename, 'r')
	lines = file.readlines()
	return lines[line_count]

def len_of_line (line_count, filename):
	current_line = print_line_from_file(line_count, filename)
	return len(current_line)

def copy_file (filename_in, filename_to):
	file_in = open(filename_in, 'r')
	content = file_in.read()
	file_out = open(filename_to, 'w')
	file_out.write(content)
	file_in.close()
	file_out.close()	

def clear_file(filename): 
	file = open(filename, 'w')
	file.truncate()


prompt = "> "

print "1. Lets first create an input file \n"
print "Type in the name of the file: "

filename_in = raw_input(prompt)

print "\n2. Lets write some info into the file! \n"
print "How many lines do you want?"

number_of_lines = raw_input(prompt)

print "So, you want the input file to contain %s lines \n" % number_of_lines

for l in range(int(number_of_lines)):
	print "Type the content of the line # %d" % l
	indata = raw_input(prompt) + "\n"
	write_into_file(filename_in, indata)


print "\n 3. Let's now print the content of the input file: "
print_all(filename_in)

print "4. Let's print only some line. Which line?"
to_print = raw_input(prompt)
print print_line_from_file(int(to_print), filename_in)
print "This line has %d characters." % len_of_line(int(to_print), filename_in), "\n"

print "5. Let's make a copy of the file"
print "Type in the name"
filename_copy = raw_input(prompt)
copy_file(filename_in, filename_copy)

print "The content of file %s was copied to the file %s" % (filename_in, filename_copy)


print "\n6. Let's now clear the input file and print its content again:"
clear_file(filename_in)
print_all(filename_in)