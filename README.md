# Harvard's CS50P

## Notes by: 0mgABear (YY)

## Last Updated: 26 June 2024

## Week 0: Functions, Variables

- Bug : mistakes in programming

- use code to create a new file

- \ is an escape character, if you want to nest quotes.

- format string, f string
- print(f"{some variable}")

  - print(f{z:,}")
    - allows to format integers with commas (e.g. 1,000)
  - print(f"{z:.2f}")
    - rounding of decimal places within F-string

- running python by itself --> python interpreter
  - don't have to keep running python over and over again.
  - not necessarily ideal
- input: default is string (be mindful!)

- square brackets [] : something optional

- def : define. Making your own functions

  - arguments can take on a default value, assign using =
  - functions must exist by the time you are already using it
  - name main function main()
    - can next functions inside main, can have a top-dwn logical approach of coding

- scope : variable only exists in the context in which you define it

Data Types:
Str: string
Int: integer
Float : Number with decimal points, limited

## Week 1: Conditionals

- some built in syntax: > , >=, <, <=, ==, !=
- strip() removes spaces

- import operator!
- can make use of operator.(choice) for usage of python's operator module

## Week 2: Loops

- lists : another kind of data type
  - list syntax: []
- instead of hard-coding lists, use range(n)
- if you need a new variable just because the programming feature requries it (e.g counting / updating), but we don't care about the value, use an underscore!
  - for \_ in range(n)
  - minor improvement
  - can just iterate over the list:
    - for list_item in list:
  - len() : length
- strings are iterable loops: for char in string
  - useful to go through the string and do checking / whatever else.
- sets: built in data type (others being list, tuple and dictionary)

- while True: a way to introduce an infinite loop

  - perhaps useful if you want to keep prompting for a certain input
    - when you want user input to matches a certain expectation that you have
  - be careful! need a way to break out of the infinite loop.
  - continue, break : some keywords to stay and exit the infinite loop

- return: a "stronger" way to break out of a loop, with a return value

- dictonary: keys and values

  - two-dimensional
  - syntax: {}
  - can use the words (keys) to access the value
  - iterable as well

- None : special keyword in python

## Week 3: Exceptions

- SyntaxError : you need to solve it manually

  - most prominently typos?
  - must be fixed, other parts of your code won't catch it

- ValueError: some value is incorrect
- NameError: doing something with the name of a variable that you shouldn't be doing

  - maybe defined in the wrong place

- try: ... except (Error):

  - python's version of try-catch
  - anticipating errors
  - can just catch everything / all other errors
    - problem: might hide other issues with other parts of your code
    - bad practice / lazy to just catch everything

- pass : another way of catching errors

- raise: can raise exceptions yourself - to be elaborated on subsequently

## Week 4: Libraries

- libraries : files of code that other people have written that we can use in our own program OR code you've written to use in your other programs.
- one or more functions / features built in
- encourages reusability
- random library
  - not accessible by default, need to be loaded
- import
  - from
- sys: system
  - sys.argv - list of all the words typed in at the prompt
    - sys.argv[\_indexes]
  - sys.exit - exit prematurely (by design)
  - CLI: Productivity. Faster - can configure software. Allows things to get done more quickly
- IndexError
- slices : subset of a data structure

  - [\_start:end]
  - each number is optional

- packages : 3rd party libraries

  - can be installed for more functionality
  - PyPi
  - cowsay
    - ASCII art
  - pip (comes with python) - allows you to install packages
    - pip install ...

- APIs: application programming interface

  - usually refer to 3rd party services that can we can write code that write and talk to
  - MOSTLY on internet (but not all)

- requests : super popular library
  - JSON: Javascript Object Notation
  - JSON used as a language agnostic format for exchanging data between computers
  - completely text based format
- json : another python library

- making your own modules / packages:
  - from (filename) import (functionname)
  - if just blindly calling main() at the bottom of the file, as long as the file is loaded, main + all the stuff inside main is going to get called.
  - that will hold true even if you're just importing the file or EVEN just a function from that file alone.
  - do not unconditionally call main in any program.
  - method:
    if `__name__` == `__main_`:
    main()
  - `__name__` : special symbol in Python
    - special variable (automatically set by Python) to be "main"

## Week 5: Unit Tests

- testing your own code, using code of your own
- write a code to solve the problem + a little extra to test the code you wrote
- convention, for what ever function name you wrote, prefix it with a test\_(function name) for the test file
- always have multiple tests within your test file, just in case one of the tests is a lucky corner cases! e.g. 2 \* 2 (intended square function) is the same as 2 + 2 (if erroneously coded as "+").
- if fewer lines of code are needed for testing:

  - more likely to do it, less work
  - fewer opportunities for mistake!
  - also would be kind of funny if your test file code is longer than your actual function code

- keyword: assert
- to assert if something is true or not.
- if something is true, nothing is going to happen. No errors will appear.
- but if it's not true, then you will get an error.
- not super user-friendly
  - shows you file and lines number involved
  - shows you the assertion that failed
  - up to user to infer
- Assertion Error

  - catch error (recap): try...except
  - good to test for expected errors (e.g. TypeError arising from erroneous input)
    - when testing for errors, don't use assert
    - pytest.raises(ErrorTypeExpected): ...(code & input that would raie that error)

- avoid side effects in code if possible

- pytest: 3rd party program, can download and install
- automate the testing of your code, as long as you write the tests

  - pytest (instead of python/python3) test_file.py
  - instead of having 1 big test function, break it down into smaller categories
  - separating big test into multiple tests might yield more clues when something goes wrong
    - ALL test functions will be run! (even if one fails)
    - for testing different things (e.g user input), can be either same file or branch out into another file (compartmentalise)

- good to have multiple functions and split up the logic
- smaller chunks that are test-able

Unit Tests: typically tests for functions you have written.

- \_\_init\_\_.py
- package: multiple modules organised inside of a folder

## Week 6: File I/O

- open: to open a file. equivalent of double clicking on a file.
- open("filename", "w")
  - w: write
    - recreate every time (will overwrite)
  - a: append
    - simple appending (adding on at the back)
    - consider /n if needed
  - r : read
    - don't have to specify, it is the default behaviour
  - returns a file handle
- file.write(var_name)
- file.close()
  - could sometimes forget to close files
  - don't strictly need to, can take another approach
- with
  - context
- readlines() : special method - read lines and return as a list
- rstrip()
- sorted() : able to look at key

  - specify what key should be used

- CSV: comma separated values
  - columns
  - excel, numbers, spreadsheet
  - split on the ,
- CSV Library!

  - import csv
  - can store the column names in the csv itself
  - DictReader more flexible - can have more columns, won't necessarily break.

- Lambda functions:

  - defining something (a variable/ function) and then immediately using it, but never needing that function ever again
    - get rid of that variable / function
    - use lambda function - anonymous function, nameless!
    - syntax: lambda student: student['name']
    - Usage: lambda (parameter): (parameter)(index)
      - right side : return value
      - can take more than 1 parameter! separated by comma

- PIL : pillow library
  - image files
  - animated gif

## Week 7: Regular Expressions

- a.k.a regex (regexes)
- pattern
  - match user input (for example)
  - capability to define patterns to compare data that we are receiving from somewhere else OR to clean up data
- re library

  - capability to define , check for and replace patterns
  - re.search(pattern, string, flags=0)
  - symbols to represent patterns
    - . : any character except a new line
    - \* : 0 or more repetitions
    - \+ : 1 or more repetitions
    - ? : 0 or 1 repetitions
    - {m} : m repetitions
    - {m,n} : m - n repetitions
    - r: raw string
      - telling python not to interpret, treat it literally
      - (technically) only strictly necessary to use with \
        - but good practice to use raw string for all regex expressions
      - don't try to interpret \ in the usual way
      - similar in spirit to f-string formatting
    - ^ : matches start of the string (carrot symbol)
    - $ : matches end of the string or just before the newline at the end of the string
    - [] : set of characters
    - [^] : complementing the set (opposite)
      - the symbols inisde = the symbols you want to exclude
    - \- : use hyphen as a range
    - | : or
    - (...) : a group
      - everything in the () will be returned to you as a return value
      - can extract specific amounts of information from the user input
      - ok to have nested parentheses if they are each solving different problems
    - (?:...) : non-capturing version
  - re.match(pattern, string, flags=0)
    - don't have to specify carrot symbol at the beginning of your regex
    - by design will start matching from the start of the string for you
  - re.fullmatch(pattern, string, flags=0)
    - start and end of string
    - no need ^ or $
  - re.sub(pattern, repl, string, count=0, flags=0)
    - pattern: to look for
    - repl: replacement, what you want to replace it with
    - string: to pass in
  - use flags to configure it differently

    - some flags are:
      - re.IGNORECASE
      - re.MULTILINE
      - re.DOTALL

  - built in shortcuts
    - \w: word character
    - \d: decimal digit
    - \D: not a decimal digit
    - \s: whitespace characters
    - \S: not a whitespace character
    - \w: word character (including numbers and underscore)
    - \W: NOT a word character

- how does the computer / re.search going to search if something matches a pattern?

  - finite state machine
  - non-deterministic finite automaton
  - start state -> determine if it stays in the first stage or transition to the next stage
  - did it end up in an except state / final state: depicted as double circle
    - in the except state after finishing input = valid
    - if not in the except state when input is finished = invalid

- if you need to validate something that is common (e.g. email/url), find a library to do it instead. No need to reinvent the wheel.

  - typing yourself / constructing yourself might lead to more errors.

- := : if and only if you want to assign from right to left AND you want to ask a if/elif question.
  - walrus operator
  - new to python in recent years
  - can assign a value from right to left
  - AND ask a boolean question
- .replace(what you want to replace, what you want to replace it with)
- .removeprefix() - no need 2 arguments
- take incremental steps of implementing a regex expression rather than trying to solve it in one shot.

## Week 8: Object-Oriented Programming (OOP)

- different paradigms
- mostly functional programming
- java: by design object-oriented
- tuple : x, y

  - similar to list
  - immutable : values cannot be changed
  - just by using a comma

- Classes

  - everytime you use it , you're creating an object
  - create our own datatype
  - general purpose tool
  - blueprint / mould - give it a name
    - object is when you use that blueprint/mould to build specific things
    - object is the instantiation of the class (an instance)
  - invent your own datatype and give it a name
  - have attributes
    - specifically: instance variables
    - we can standardise what the attributes can be / what kind of values you can set them to
  - mutable but can be made immutable
  - passing in arguments into a Class:
    - standardising how you're passing in data
    - error / validity check the inputs
  - methods: classes come with methods/functions
    - allow to determine behaviour in a standar way
  - def \_\_init\_\_(self, ...args):
    - the arguments **can be** optional.
      - use it as `arg=None` to let it be optional.
    - convention: self (but you can call it anything you want).
    - dunder init / instance method
    - if you want to initialise the contents of an object from a class, you define this method
    - must have the self! if not where to put the variables?
      - if you want to remember the attributes / instance variables.
      - storing in self!
  - when you're calling a class: Class() - this is a constructor call
    - construct / instantiate a class object
    - everything created using the class will have the same structure
    - can pass in arguments -> can customise the contents of that object
    - analogy: you have houses built using same blueprint (mould), but painted differently (specifications)
    - when you call / instantiate a class, you use parentheses ().
      - suggests that a function somewhere is called / run.
      - the function that is run is the \_\_init\_\_ function within the Class.
  - def \_\_str\_\_ : special method
    - python will automatically call this function for you anytime some other function wants to see your object as a string.
    - can define this dunder str method yourself!
  - generally \_\_repr\_\_ more for devs.
  - can create our own methods - real power of Classes

- Difference: init vs constructors:
  - init : initialisation method, initialises the value
  - another python method: \_\_new\_\_
- self.variable : can be list / dictionary for multiple values
- Why classes over dictionaries?

  - can ensure correctness of data
  - error check
  - design more complicated software effectively

- ... : placeholder
- while checking for input argument validty , it's a somewhat extreme response to exit the entire programe due to invalid inputs.

  - might want to clean some stuff up, same some files
  - create your own error

- raise : raise an exception

  - can create your own exceptions
  - not wrong enough to quit the whole program but alert the programmer there's an error
  - exceptional (bad)
  - be more precise. don't have to raise a generic error. can treat all exceptions like a function
    - e.g. ValueError(message)
    - can create your own error!

- properties : more defense mechanisms put into place
  - to prevent other devs from messing things up
  - attribute with more control over
  - @property - technically a function
- decorators: functions that modify the behaviour of other functions.
- getter: function of a Class that gets some attribute
  - when you want to define a getter, just set @property
  - only 1 argument
- setter: function of a Class that sets some attribute
  - @function_name.setter
  - an assignment: `variable =` is enough to trigger python to use the setter function.
  - 2 arguments
- to prevent conflict / infinite recursion, inside your getter / setter functions, the variables cannot be the same name(s) as in your init function.

  - prefix the variables in your getter / setter function with an `_`
  - such prefixing not needed for your init function

- int, str: is actually a Class

- Class Methods
  - sometimes not necessary / sensible to associate a function with objects of a class, but rather with the class itself
  - sometimes you want certain functions to be associated with the class, no matter the objects / values
  - @classmethod : another decorator / function - not an instance method with access to self
    - no access to self but knows what class it is inside
    - no need to pass in self anymore, just pass in `cls`
    - why cls? conflict with the keyword class
  - also have @staticmethod
- When should you use a Class to represent something in your code?
  - very often when you're trying to represent some real world entity
- Up till now, writing functions inside of classes that are automatically passed a reference of self.
  - sometimes, don't need that
  - just need to know the Class, and might not be any objects of that Class.
  - use Class as a container for data and/or functionality.
- Class Variables: shared across all instances of the class.(can be int, str or list etc.)

  - the variable will be accessible to all of the functions within that class.

- Inheritance:
  - design Classes in a hierarchical fashion
  - have 1 class inherit from/borrow attribute/methods/functions from another class if they have those in common

## Week 9: Et Cetera
