binary="binary"
don_not="don't"
y="Those who know %s and those who %s." %(binary,don_not)
x='test x'

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
print w + e
