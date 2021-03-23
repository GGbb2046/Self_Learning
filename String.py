import re
'''
import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. Ruth and Peter, their parents, have 3 kids."""
  
    # YOUR CODE HERE
    return re.findall("[A-Z]\\S+",simple_string)
    #raise NotImplementedError()
print(names())

assert len(names()) == 4, "There are four names in the simple_string" 
'''


def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
        
    #YOUR CODE HERE
    pattern = "([A-Z]\\S+): B"
    return re.findall(pattern,grades)
    #raise NotImplementedError()

print(grades())
