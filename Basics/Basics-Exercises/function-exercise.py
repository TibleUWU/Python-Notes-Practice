# 1. Add a function named 'list_benefits()' that returns the following list of strings. 'More organized code', 'More readable code', 'Easier code reuse', 'Allowing programmers to share and connect code together'
# 2. Add a function named 'build_sentence(info)' which recieves a single argument containing a string and returns a sentence starting with the given strings and ending with the string ' is a benefit of functions!'
# 3. Run code

# Mofify Function to return list of strings above

def list_benefits():
    return 'More organized code', 'More readable code', 'Easier code reuse', 'Allowing programmers to share and connect code together'

# Modify function to concatenate to each benefit - ' is a benefit of functions!'
def build_sentence(benefit):
    return "%s is a benefits of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()