Primitive Data Structures
       ● Integers: Whole numbers (e.g., 1, 2, 3).
       ● Float: Decimal numbers  (e.g., 1.1, 2.5, 18.97).
       ● Strings: Ordered sequence of characters  (e.g., "Hello", "Python").
       ● Boolean: Represents either = True or False.

Non-Primitive Data Structures
    Data structures used to store multiple values.      
        ● List = A collection is a single "variable" used to store multiple values.
                 Ordered and changeable. Duplicates are allowed.

                my_list = []                             # Empty List
                my_list = ["apple", "banana", "cherry"]  # List with three values

                ○ # List Methods
                my_list[1] = "obj"           # Update a List
                del my_list[1]               # Delete a value from List
                list(string)                 # Convert a string to a list
                string.split()               # Split a string on a character parameter
                "".join(string)              # Convert a list of characters into a string
                my_list.append(obj)          # Add an object to the end
                my_list.count(obj)           # Count occurrences of an object
                my_list.extend(seq)          # Add elements from another list
                my_list.insert(index, obj)   # Insert an object at a specific index
                my_list.pop(obj=my_list[-1]) # Remove and return the last object
                my_list.remove(obj)          # Remove the first occurrence of an object
                my_list.reverse()            # Reverse the order of objects
                my_list.sort()               # Sort the objects in the list
                my_list.clear()              # Clear the list Removing all objects

                ○ # List Operations
                print(my_list[::])           # Print the entire list
                print(my_list)               # Print the entire list
                len(my_list)                 # Output the length of the list
                ["Hi"] * 4                   # Output = ["Hi", "Hi", "Hi", "Hi"]
                [1, 2, 3] + [4, 5, 6]        # Output = [1, 2, 3, 4, 5, 6] "Concatenate two lists"
                print(3 in [1, 2, 3])        # Output = True "Check if an element exists in the list"
                for x in [1, 2, 3]:          # Iterate over the list
                        print(x)             # Output = 1 2 3

                ○ # 2D List
                name_list = ["Mohamed", "Ahmed", "Mahmoud", "Mostafa"]
                age_list = [26, 58, 20, 30]
                city_list = ["Alex", "Dubai", "Tanta", "Cairo"]
                info_list = [name_list, age_list, city_list]

                ○ # OR

                2d_list = [["Mohamed", "Ahmed", "Mahmoud", "Mostafa"],
                           [26, 58, 20, 30],
                           ["Alex", "Dubai", "Tanta", "Cairo"]]

                print(2d_list[0][1])            # Output = "Ahmed"

        ● Tuples = Ordered and unchangeable. Duplicates are allowed.

                my_tuple = ("apple", "banana", "cherry")         # Create a tuple
                my_tuple = tuple(("apple", "banana", "cherry"))  # Constructor (Note the double round-brackets)
                print(my_tuple)                                  # Print The tuple
                print(my_tuple[1])                               # Print value at position 1
                tuple(my_list)                                   # Convert a list into a tuple
                del my_tuple                                     # Delete the tuple

                ○ # Tuple Object Methods
                cmp(my_tuple_1, my_tuple_2)  # Compare two tuples, return 0 if true, -1 if false
                len(my_tuple)                # Length of the tuple
                max(my_tuple)                # Maximum value element of the tuple
                min(my_tuple)                # Minimum value element of the tuple

        
        ● Sets = Unordered and mutable. Add/Remove operations are allowed. No duplicates.

                my_set = set()                                # Create an empty set
                my_set.add("orange")                          # Add a value to the set
                my_set.update(["orange", "mango", "grapes"])  # Add multiple values
                len(my_set)                                   # Length of the set
                my_set.remove(obj)                            # Remove an object from the set
                my_set.pop()                                  # Remove and return an arbitrary object from the set
                my_set.clear()                                # Clear the set
                del my_set                                    # Delete the set

        ● Dictionary = A collection of key-value pairs, ordered and changeable. No duplicates.

                my_dict = {"key1": value1, "key2": value2}  # Create a dictionary
                x = my_dict.get("model")                    # Access a value using a key
               "John" in my_dict                           # Test if a key is in the dictionary
                my_dict["year"] = 2018                      # Change values
                my_dict["Sylvan"] = "A"                     # Add an entry
                del my_dict["Ana"]                          # Delete an entry

                ○ # Dictionary Object Methods
                my_dict.clear()             # Remove all elements from the dictionary
                my_dict.copy()              # Return a copy of the dictionary
                my_dict.items()             # Return a list of (key, value) tuple pairs
                my_dict.keys()              # Return a list of dictionary keys
                my_dict.values()            # Return a list of dictionary values
                my_dict1.update(my_dict2)   # Merge my_dict2 into my_dict1
                my_dict.popitem()           # Remove and return the last inserted item
                my_dict.values()            # Get an iterable that acts like a tuple of all keys
                my_dict.keys()              # Get an iterable that acts like a tuple of all values

        ● Arrays = One type list. 
                 Note: Python does not have built-in support for arrays, but Python Lists can be used instead.

                from array import array
                OR
                Using Numpy Array

                my_array = array('data_type', initial_values)  # Initialize an array
                my_array.append(values)                        # Append values to the array


Files

import os
# Files Detection
path = 'C:\\Users\\...'
if os.path.exists(path):                    # Check if the path exist
        print ("That Location exists.")
        if os.path.isfile(path):            # Check is this is a file
               print ('This is file')
        elif os.path.isdir(path):           # Check if the directory exist
               print ('this is directory')
else:
       print ("The location does not exist!")
# Files Read
with open ('C:\\the\\file\\path') as file: # with Open will auto close the file
       print (file.read)
print(file.close)
# Write Files
text = (' text to put in the file ')
with open ('file name.txt', 'w') as file: # w for Write , a for Append, x for Create and r for Read (default)
        file.write(text)       
# Delete File
os.remove('file name.txt')
os.rmdir("foldername")


Exception
# Exception = events detected during execution that interrupt the flow of a program.
try:
        numerator = int(input("Enter a number to divide: " ))
        denominator = int(input('Enter a number to divide by: '))
        result = numerator / denominator
except ZeroDivisionError as e:
        print (e)
        print ("You can't divide by zero! idiot!")
except ValueError as e:
        print (e)
        print ("Enter only numbers plz")
except Exception as e:
        print (e)
        print("something went wrong :(")
else:
        print (result)
finally:
        print ("This will always execute")


Function
# Function: Is a block of reusable Code
# There is 4 types of functions Argument
# 1. Positional Argument, 2. Default Argument, 3. Keyword Arguments, 4. Arbitrary Arguments

# 1. This function using positional Argument (Parameter)
def function_Name(data, first_number, second_number): # Data is a parameter (Temporary data to the Function) you Can add as many as you want.
    # Any Code for Example
    print (f"The Data that you have send as a string > {data} & Numbers {first_number}, {second_number}")
    number = first_number + second_number
    return number # return: Is a statement that used to end a function and send a result back to the caller
        
# Invoke A Function Or Call A Function

function_Name("Send Data To the Function", 10,5)
print()
print(function_Name("Send Data To the Function", 10,5))

# 2. Default Argument: A default value for certain parameters default is used when that argument is omitted
# Any Positional Argument come first before Any Default Argument
def net_price (price, discount = 0 , tax = 0.05): # We assign a default value so we don't have to enter this parameter ever if we don't want.
    return price * (1- discount) * (1 + tax)

print(net_price(500, 0.1)) 

# 3. Keyword Arguments: an argument preceded by an helps with readability order of arguments doesn't
print(net_price(discount=0.2, tax=0.06, price=500)) 

# 4. Arbitrary Arguments
# *args = allows you to pass multiple allows you to pass multiple
# **kwargs = unpacking operator non-key arguments keyword - arguments
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,5,12,50))

def print_address(**kwargs): # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print(print_address(street   ="12" ,
                    apartment="5" ,
                    district ="elshatby", 
                    city     ="Alex", 
                    country  ="Egypt") )

