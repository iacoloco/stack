

#ex 1: given the following sequence of stack operation, what is the stack when the sequence is complete:
    # push x , push y , pop , push z 

 #First create a instance
from stack import Stack

# Create an instance of the Stack class
s = Stack()

# Perform the sequence of stack operations
s.push("x")
s.push("y")
s.pop()
s.push("z")

peek_result = s.peek()

# Print the result
print(peek_result) 

