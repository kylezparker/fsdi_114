# anagram: must be same length and must use exact same characters(no more, no less)


# best case will be o(1) constant time
# worst case will be o(n) linear time

# extension dealing with caps and spaces (edgars code) is hw, replace() and lower()
# can use string builtins 


# ord("A") 65  chr(65)  A

def are_anagrams(string_a,string_b):


    if len(string_a) != (string_b):
        return False

    dict_a= {}
    dict_b= {}
    for i in range(len(string_a)):
        if string_a[i] in dict_a.keys():
            dict_a[string_a[i]] += 1
        else: 
            dict_a[string_a[i]] =1
        for string_b[i] in dict_b.keys():
            dict_b[string_b[i]] += 1
        else: 
            dict_b[string_b[i]] =1
    return dict_a == dict_b

# CLASS 2 REALLY

# THIS IS AN EX OF A STACK USING BUIILTIN DATA STRUCTURES
# user defined data structure(UDT)

class Stack:
    def __init__(self):
        self.items = []
        
    def push (self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# helper methodsjup
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]



# problem 2 invert a string

# take string push chars on to stack, pop them off and store in new string


def reverse(word):
    stack = Stack()
    reversed = ""
    for letter in word:
        stack.push(letter)
    while stack.is_empty() != True:
        reversed += stack.pop()
    return reversed   

something =reverse("aaaaaaaaaaaasssssssssssssdddddddddddddddddffffffffffffffffffff")
print(something)


# queues first in first out, good for task management (processing limitations), things are queued until they can be processed as tasks
# lets us store data in memory til were ready
class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue (self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

# helper methods
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

from dataclasses import dataclass
from random import randint
from time import sleep

def square_queue(elements):
    q = Queue()
    for element in elements:
        print("adding %s to our queue" % element)
        q.enqueue(element)
    while not q.is_empty():
        datum = q.dequeue()
        sleep(randint(1,3))
        print("%s squared is %s" % (datum,datum**2))


square_queue([1,2,3,4,5])


# some data types pass by value and some pass by reference, native/primary pass by value. integers, floats, boolean. 
x=5 
y=x
x=+ 1
print(y)
# passes value of 5. instead of referencing x for value

# pass by reference
x= [1,2,3]
y=x
x.append(4)
print(y)

# 1,2,3,4


class Node:
    def __init__(self):
        self.data = data
        self.above = None
        

class Stack:
    def __init__(self):
        self.base = None
        
    def push (self, item):
        if not self.base:
            self.base = Node(item)
        else:
            current = self.base
            while current.above:  # while current.above != None
                current = current.above
            current.above =Node(item)

    def pop(self):
        pass

# helper methods
    def is_empty(self):
        if not self.base: 
            return True
        return False

    def size(self):
        pass

    def peek(self):
        pass
