print "EXERCISE 14. Prompting and Passing"
print "." * 53
from sys import argv
script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script. " % (user_name, script)
print "I'd like to ask you a few questions.\n"
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)
print "\n"

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.

""" % (likes, lives)
print "." * 53, "\n"


