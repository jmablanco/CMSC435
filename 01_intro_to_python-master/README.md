# Introduction to Python
This assignment is meant to introduce you to a number of 
concepts in the Python programming language that will be necessary for 
assignments, projects, and exams.

In order to make full use of functionality that already exists in 
the Python programming language it is **strongly recommended** 
to peruse/familiarize oneself with a few resources:

## Basic Syntax
From [Python Basics](https://www.pythoncheatsheet.org/#Python-Basics) the
following sections would be very useful to become familiar with:

1. Python Basics
2. Flow Control
3. Functions
4. Lists
5. Dictionaries
6. Comprehensions
7. Manipulating Strings
8. String Formatting
9. Ternary Conditional Operator

A useful cheat-sheet that contains information on all this and more 
can be found [here](https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf).

## Types in Python
Python is a weakly-typed language which gives a great amount of inherent 
flexibility, but makes it difficult for collaborating programmers to understand
what a function and/or class was intended to actually do. Some time ago, 
the construct of **type hints** were introduced into Python. 

These type hints allow developers to more clearly relay the intention of 
a function by enumerating the expected input and output types. 
Not using the appropriate type does not prevent running a Python program, 
but most IDEs will show errors. This is very simple to use in practice. An 
example can be found below.

```Python
# x should be of type int and square() should return an int
def square(x: int): -> int
    return x*x
```