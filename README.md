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
- strings are iterable loops: for char in string
  - useful to go through the string and do checking / whatever else.
- sets: built in data type (others being list, tuple and dictionary)

- while True: a way to introduce an infinite loop
  - perhaps useful if you want to keep prompting for a certain input
  - be careful! need a way to break out of the infinite loop.

## Week 3: Exceptions

## Week 4: Libraries

## Week 5: Unit Tests

## Week 6: File I/O

## Week 7: Regular Expressions

## Week 8: Object-Oriented Programming (OOP)

## Week 9: Et Cetera
