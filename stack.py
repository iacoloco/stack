#stack

#created a class stack with all of the function to work with a stack

class Stack:
    
    #function to create a new instance in the class stack
    def __init__(self):
        self.items = []
    
    #funtion to check if my object is empty: it will return false if is not empty
    def isEmpty(self):
        return self.items == []
    
    #funtion to append at the top to my item 
    def push(self, items):
        self.items.append(items)
    
    #function to remove the last item added from the object 
    def pop(self):
        return self.items.pop()
    
    #return the time before the last one
    def peek(self):
        return self.items[len(self.items) -1 ]
    
    #
    def size(self):
        return len(self.items)
    

#ex 1: given the following sequence of stack operation, what is the stack when the sequence is complete:
    # push x , push y , pop , push z 

   


# Create an instance of the Stack class
s = Stack()

# Perform the sequence of stack operations
s.push("x")
s.push("y")
s.pop()
s.push("z")
print(s.peek())  # Output: z




    
    