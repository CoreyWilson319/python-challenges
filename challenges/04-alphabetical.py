# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


string = input("What do you want to reverse?: ")

def sort_alpha(string):
    list = []
    for l in string:
        list.append(l)
    print(("").join(sorted(list)))

sort_alpha(string)