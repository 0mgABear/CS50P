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

## Week 7: Regular Expressions

## Week 8: Object-Oriented Programming (OOP)

## Week 9: Et Cetera
