
![jpg](/docs/Sandbox_Logo.jpg)
# Branching and Operators

Branching is an essential part of most programs. Our program flow thus far have been linear, running one command after another until we have no lines of Python left to run. Let's say we wanted offer our users a choice between buying a hamburger or a cheeseburger. No matter what our user responds we are going to end up running both the hamburger code *and* the cheeseburger code. Our user is going to be very confused when they are forced to pay for and eat both a hamburger and a cheeseburger. For example:

```Python
# Ask the user what they want.
burger = input("Would you like a cheeseburger or a hamburger?")

# We are okay so far, we can use their response to answer.
# But it isn't a great solution, what if they had typed in sushi??
print("One {} coming up!".format(choice))

# But now we have to charge them for something
# and cook them something.
order_hamburger()

# Wait but did they order that?
# Better just order a hamburger, just to be safe.
order_cheeseburger()

print("Thanks for your order!")
# Now Im in a bunch of trouble!!
# I cost the customer money and wasted food!
```

There is a couple of things to note about the code above:
1. The lines that start with `#` are **Comments**, Python ignores anything that has a `#` before it. It gives us programmers a way to communicate our ideas and how our program work!
2. The `order_hamburger()` and `order_cheeseburger()` are functions, just like the built-in functions like the ones we have seen before except they are *not* (as nice as that would be) built-in. So if they are not built-in, where are they coming from? They would have been defined somewhere else in the program, maybe by YOU. Right now they are just being use to express an idea.

Ok, so obvously my code is not ready for real use yet but lets see if we can get it there.

## Operators and Comparison

We have seen several operators so far:

| Operator | Name |
|----------|------|
| + | Addition |
| - | Subtraction |
| *  | Multiplication |
| /  | Division |
| =  | Assignment |

But we have a few more to learn!

### Comparison Operators
| Operator | Description | Example |
|---|---|---|
| == | Equals (True if both sides are equal) | x == 5 |
| != | Not Equal (True if both sides are **NOT** equal | x != y |
| < | Less Than | x < 10 |
| > | Greater Than | z > 0 |
| <= | Less Than Or Equal To | a <= b |
| >= | Greater Than Or Equal To | c >= d |

### Logical Operators
| Operator | Description | Example | True if: |
|---|---|---|---|
| and | True if both sides are True | x > 0 and x < 10 | x is between 0 and 10 |
| or | True if one of the sides is True | x == y or z == w | x and y are equal OR z and w are equal |
| not | Reverse a bool, True if bool was False | not(x == x or 5 == 10) | Never |

There are more operators but they are less used. We may talk about a few later, but on we go!

Using Comparison and Logical Operators we can evaluate complex comparisons to either `True` or `False`!

### Challenge:
Evaluate the following if `x = 5; y = 10; z = -15`:
1. x == 5
2. y == 8 or z == -15
3. x == 5 and y < 55 and z >= z
4. x == 1 or not(y == 10 and x < 0)
5. not(not(x > 10) and not(y > x and y > z))

## Branching - IF
Okay, with comparisons under our belts we can start branching! In Computer Science, branching is making a choice to run certain code depending on what *conditions* have been met.

Our primary tool for branching in Python is the `if` statement. The `if` statement runs a block of code only if a certain condition is `True`. For example:


```python
x = 15
y = 0
# Check if x is bigger than 10
if x > 10:
    print("X is a big number")
    # Then if it is bigger than 10, check if it is smaller then 20.
    if x < 20:
        print("But not as big as 20!")

# Check if y is bigger than 10
if y > 10:
    print("Y is a big number")
    print("Let's make Y smaller")
    y = -1
print("All Done")
```

    X is a big number
    But not as big as 20!
    All Done


Notice in the code above, the first and second branches was run because the comparison eveluates to `True`. However the third was not run, because its comparison evaluates to `False`.

#### IMPORTANT
`if` statements run (or don't run) **blocks** of code. A block of code in Python is written differently than in most languages. A **block** starts after the colon `:` at the end of the if statement and any lines of code that we want to put in the block **must** be intented by **4 spaces** past the beginning of the block above it. To exit the block simply reset your indentation back **4 spaces**.

So let's improve our hamburger program from before:


```python
burger = input("Would you like a hamburger or cheeseburger?")

if burger == "Hamburger":
    order_hamburger()
if cheeseburger == "Cheeseburger":
    order_cheeseburger()
    
print("Thanks for your order!")
```

## Branching - ELIF, ElSE

Great! So now we won't end up charging them for items that they did't order. But there is still a few problems:
1. If they ordered a hamburger then we don't need to check to see if they ordered a cheeseburger, that just wastes time!
2. What if they did't ask for either of them.

This is where *ELSE If* and *ELSE* statements come it. They work almost the same as if statements; but they are only run when the `if` statement is not run. Let's see an example:


```python
import random

x = random.randint(0,10)

if x > 5:
    print("X is larger than 5")
else:
    print("X is smaller than or equal to 5")
```

    X is larger than 5


This is our first look at the random module. Importing `random` module allows us to use new functions and classes just like the `math` module does. It allows us to call the `randint()` function which gives us a random Integer between the two arguments we give the function. In this case it picks a random number from the set {0,1,2,3,4,5,6,7,8,9,10}.
We don't know what number it picked but we know that it was larger than 5. Let's run it again. Because the `if` statement *is* run, the `else` statement is not run. Let's run our program again.


```python
import random

x = random.randint(0,10)

if x > 5:
    print("X is larger than 5")
else:
    print("X is smaller than or equal to 5")
```

    X is smaller than or equal to 5


This time the `if` statement does *not* run so the `else` statement is run. We also have `elif` (else if) statements. Else if statements work similar to else statements except they only run `if` their contition is True. Take a look at the program-flow diagram below.

![if.png](if.jpg)

`elif` blocks are always placed after the `if` statement and before the (optional) `else` statement. We can add as many `elif` statements as we like so our branching structures can get quite a bit more complex. Let's see this in action:


```python
grade = 88

if grade > 90:
    print("Grade: A")
elif grade > 80:
    print("Grade: B")
elif grade > 70:
    print("Grade: C")
elif grade > 60:
    print("Grade: D")
else:
    print("Grade: F")
```

    Grade: B


### Disclaimer
`if` statements are very useful and will certainly be a part of almost all of our programs, however they can be overused. Be careful to avoid huge nested `if` statements (`if` statements in `if` statements) as it can make a program very hard to understand, to change, and to debug. We will see other programming patterns later that can help avoid these huge structures.
