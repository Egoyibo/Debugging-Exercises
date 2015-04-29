
# Helpers
#########
def print_me(str):
    "This prints a passed string into this function"
    print str
    return

def kill_time():
    long_string = ""
    for i in range(1, 20):
        long_string = long_string + "a"*i + " "

    a = 'a'
    b = 'b'

    return long_string


import pdb; pdb.set_trace();

# n | c | b | b x | b x, condition
######################################

some_variable = "Hello"
other_variable = "World"
hello_world = some_variable + " " + other_variable

# pp - pretty print
####################
tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot',\
      ('fresh fruit',))))))))
ugly = ['a' * 10, tup, ['a' * 30, 'b' * 30], ['c' * 20, 'd' * 20]]


# s - step
###########

new_variable = "@Hackbright"
new_hello_world = hello_world + " " + new_variable
print_me(new_hello_world)

# unt - until | r - return
###########################
very_long_string = kill_time()
