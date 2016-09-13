# How conditionals are used
# a conditional is an expression with evaluates to true or false

a = 99
b = 0
if a < b:
    print (str(a) + " bottles of beer on the wall" )
    print (str(a) + " bottles of beer")
    print 'if one of those beers should happen to fall'
    print a-1, 'bottles of beer on the wall\n'
elif a > b:
    print (str(a) + " is greater than " + str(b))
else:
    print (str(a) + " is equal to " + str(b))

print " "
# while loop -- continues as long as the condition is true

a = 99
b = 0

while a > b:
    print (str(a) + " bottles of beer on the wall" )
    print (str(a) + " bottles of beer")
    print 'if one of those beers should happen to fall'
    print a-1, 'bottles of beer on the wall\n'
    a -= 1 #subtract 1

print ""
# for loop -- iterates a fixed number of times
