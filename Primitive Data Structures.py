#   Primitive Data Structures
        ● Integers  = 1, 2, 3, ....
        ● Float     = 1.1, 2.5, 18.97, ... 
        ● Strings   = "Any WordS" 
        ● Boolean   = True Or False

#   Non-Primitive Data Structures
        A Collection is A Single "Variable" Used to Store multiple Values
● Attributes:
○
        ● Lists  = [] ordered and changeable. Duplicates OK
            MyList = []                                         # Empty List
            MyList = ["apple", "banana", "cherry"]              # List with three values
            
            ○ List Method's:
                MyList[1] = "blackcurrant"                      # Updating a List
                del.MyList[1]                                   # Delete Value from List
                list(s)                                         # Convert string to list      
                s.split()                                       # Split a string on a character parameter
                ''.join(L)                                      # List of characters into a string
                MyList.append(obj)                              # Appends object obj to list
                MyList.count(obj)                               # Returns count of how many times obj occurs in list
                MyList.extend(seq)                              # Appends the contents of seq to list
                MyList.insert(index, obj)                       # Inserts object obj into list at offset index
                MyList.pop(obj=list[-1])                        # Removes and returns last obj from list
                MyList.remove(obj)                              # Removes object obj from list
                MyList.reverse()                                # Reverses objects of list in place
                MyList.sort()                                   # Sorts objects of list 
                MyList.clear()                                  # Clear the List

            ○ List Operations
                print(MyList[::])                               # Printing a List and Using indexing MyList[Start i: End i: Step Type] 
                len(MyList)                                     # Output length of list
                ["Hi"] * 4                                      # Output = ["Hi", "Hi", "Hi", "Hi"]  
                [1, 2, 3] + [4, 5, 6]                           # Output = [1, 2, 3, 4, 5, 6]  
                print(3 in [1, 2, 3])                           # Output = True
                for x in [1, 2, 3]: print x                     # Output = 1 2 3

            ○ There is Also 2D List with lists in side of a list goes like this :
                Name_List = ["Mohamed", "Ahmed", "Mahmoud", "Mostafa"]
                Age_List  = [26, 58, 20, 30]
                City_List = ["Alex", "Dubai", "Tanta", "Cairo"]
                Info_List = [[Name_List], [Age_List], [City_List]]

                ○ OR
                
                TwoD_List = [["Mohamed", "Ahmed", "Mahmoud", "Mostafa"],
                           [26, 58, 20, 30],
                           ["Alex", "Dubai", "Tanta", "Cairo"]]
                
                print (TwoD_List[0][1])


        ● Tuples = () ordered and unchangeable. Duplicates OK. FASTER
                MyTuple = ("apple", "banana", "cherry")              # Create a Tuple
                MyTuple = tuple(("apple", "banana", "cherry"))       # Constructor Note the double round-brackets
                print(MyTuple)
                print(MyTuple[1])                                    # Print Value in position 1 
                del (MyTuple)                                        # Delete Tuple Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely

                ○ Tuple Object Methods:
                    cmp(MyTuple_1, MyTuple_2)                        # Compares two tuples elements, return 0 if true -1 if false.
                    len(MyTuple)                                     # Length of a given tuple.
                    max(MyTuple)                                     # Max value element of a given tuple.
                    min(MyTuple)                                     # Min value element of a given tuple.
                    tuple(MyList)                                    # Converts a given list into a tuple.                     

        ● Sets = {} unordered and immutable, but Add/Remove OK. NO duplicates
                MySet = {}                                    # Create Empty Set
                MySet.add("orange")                           # Add Value to Set
                MySet.update(["orange", "mango", "grapes"])   # Update Set
                Len(MySet)                                    # Length of the Set
                MySet.remove(obj)                             # Removes Object from Set
                MySet.pop()                                   # Removes and returns last Object from Set
                clear(MySet)                                  # Clear Set
                del() # Delete Value from Set
                set() # constructor

        ● Arrays = (One Type List) # Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
                MyArray = array('data_type', initial_values)    # Instial Structure
                MyArray.append(values)

        ● Dictionary  =  a collection of {key:value} pairs ordered and changeable. No duplicates
                x = MyDict.get("model")         # Accessing Items
                'John' in MyDict                # Test if key in MyDict
                MyDict["year"] = 2018           # Change Values
                MyDict['Sylvan'] = 'A'          # Add an entry 
                del(grades['Ana'])              # Delete entry

                ○ Dictionary Object Methods: 
                    MyDict.clear()                # Remove all elements of dictionary 
                    MyDict.dict.copy()            # Returns a copy of dictionary 
                    MyDict.dict.items()           # Returns List of dict (keys, values) Tuple pairs. 
                    MyDict.keys()                 # Returns a List of dict keys. 
                    MyDict.values()               # Return a List of dict values. 
                    MyDict_1.update(MyDict_2)     # Add dict_2 elements (key, value) to dict_1 
                    MyDict.popitem()              # Method removes the last inserted item (in versions before 3.7, a #random item is removed instead)
                    MyDict.value()                # Get an iterable that acts like a tuple of all keys
                    MyDict.key()                  # Get an iterable that acts like a tuple of all values





        • Files



        Function: Is a block of reusable Code

                def function_Name(Data): # Data is a parameter (Temporary data to the Function)
                        # Any Code for Example
                        print (f"The Data used by the Function {Data}")
                        pass
        
        Invoke A Function

                function_Name("Send Data To the Function")


        #class Test(obj):
# define attributes here

#self references to current instance

# you can change name of self for any other name

#Destroying Objects (Garbage Collection)


# Function: Is a block of reusable Code
# 1. This function using positional Argument (Parameter)
def function_Name(data, first_number, second_number): # Data is a parameter (Temporary data to the Function) you Can add as many as you want.
    # Any Code for Example
    print (f"The Data that you have send as a string > {data} & Numbers {first_number}, {second_number}")
    number = first_number + second_number
    return number # return: Is a statement that used to end a function and send a result back to the caller

        
# 2. Invoke A Function
function_Name("Send Data To the Function", 10,5)
print()
print(function_Name("Send Data To the Function", 10,5))

# Default Argument: A default value for certain parameters default is used when that argument is omitted
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

