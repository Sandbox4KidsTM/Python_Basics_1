
 ![jpg](/docs/Sandbox_Logo.jpg)
# Python Basic Types & User Interaction

This lession is intended as your very first introduction to Python.

Python is a great choice for a first programming language. This general purpose language is **flexible**, **powerful** and **robust**.

Lets see how to help Python say "Hello!".


```python
print("Hello, World!")
```

    Hello, World!


As simple as it seems there is a bit of action happening in the code above. 

The `print` statement is a built-in **function** (we will talk about functions later on) and can be used in any Python programming, no strings attached!
You can prbably guess what it does, the `print()` function *prints* some output for the user to read!

Whenever we want to use a function, whether it is built-in, from a library, or even one of our own; we always follow the function name with a pair of parethesis, `()`.

Inside those parethesis we can insert **arguments**, sometimes called **parameters**. **Arguments** are data that we give to the function, and the function then decides what to do with the data. For example, the `print()` function does not know what to print unless we tell it what we want it to print. In our case `"Hello, World!"`. So `"Hello, World!"` is the only argument given to the `print` function.

There is a slight difference between the two but in certain languages they become interchangable. We will stick to arguments for now.

The `"Hello, World!"` is a **String**, a collection of characters, that Python knows not to try and interpret as Python code. This is how we represent text in Python. Creating a new string for our program to use is very easy, we just wrap the text in "double qotes". `"I am a string in Python."`

WOW! That was a lot for one little line of code. Lets take a step back and take a look at the basic types that form the foundations for our Python programs.

## Basic Types

The basic types are the key foundation for all the programs we will write in Python. They are what everything else is build on top of! We have already had a little exposure to 2 of them so lets dive on in.

### Integers

The Integers are one of three Basic types in Python that hold numbers. To put it simply, Integers hold numbers that don't have any decimal value. For example, `1, 4, -8, 16, 10400` and `0` are all integers. The Integers all have the basic arithmetic operations defined for them:


```python
4 + 6
```




    10




```python
5 - 18
```




    -13




```python
4 * 16
```




    64




```python
32 / 8
```




    4.0



Woah! Take a look at that last one. By default, when Python interprets a division problem it gives back our next data type:

### Floating-Point Numbers

Floating-Point Numbers or Floats are the way we represent decimals in Python. There is quite a lot going on behind the scenes to make this data type work but for use they are used almost exacly like Integers:


```python
2.5 + 6.3
```




    8.8




```python
24.7 - 13.7
```




    11.0




```python
4.5 * 2.5
```




    11.25




```python
12.5 / 0.5
```




    25.0



There is one other numeric data type called the *Complex* Numbers but we won't address them now.

### Booleans

Our next basic data type is the boolean, and while it may seem simple, they are extremely powerful. A boolean is either `True` or it is `False`. We will see later how powerful this can be and will learn how to solve complex problems using these simple little data types.

### Strings

Strings (`str`) are a data type we have seen before, remember `"Hello, World!"`? Like with Floats, Strings have quite a bit more than meets the eye working in the background to keep everything running smoothly. We will study them in quite a bit of depth later in the class. For now all we need is remember is that they are a collection of characters that is used to represent text. Python has the capibility to display other things inside of Strings, for example symbols: λ. 


```python
print("\u03BB")
```

    λ


But we won't worry too much about that right now.

### Built-In Functions
And finally we have the built in functions, while not really data types they are a foundational part of Python and it is worth introducing you to a few of them.

You have already seen `print()`:


```python
print("Welcome to Sandbox!")
```

    Welcome to Sandbox!


Next we have `input()`, which takes a String as an argument, prints it out, waits for the user to enter some text, and gives that text back to the programmer. For example:


```python
input("What is your favorite color? ")
```

    What is your favorite color?  Green





    'Green'



`type()` allows us to check what basic type an object is:


```python
type(15)
```




    int




```python
type(45.2)
```




    float




```python
type(True)
```




    bool




```python
type("Hello, All!")
```




    str



We also have a few sets of math related built-ins like: `abs()`, `pow()`, and `round()`. Very useful!

`abs()` stands for absolute value, and returns the distance from the number given to 0:


```python
abs(5)
```




    5




```python
abs(-9)
```




    9



`pow()` lets us raise numbers to a given power, for example 3 squared:


```python
pow(3,2)
```




    9



Or 4 cubed:


```python
pow(4,3)
```




    64



`round()` does exactly what you might expect it too, it rounds a float into an integer:


```python
round(4.5)
```




    4




```python
round(8.8)
```




    9




```python
round(1.3)
```




    1



And lastly we have the casting functions, they are built-in functions that allow us to convert one basic type to another. Kind of like the `round()` function does. 

`str()` turns any of the basic types into a string, for example:


```python
str(True)
```




    'True'




```python
str(4.3)
```




    '4.3'




```python
str(15)
```




    '15'



`int()` can turn a float or string into a number:


```python
int(15.8)
```




    15




```python
int(12.3)
```




    12




```python
int("20")
```




    20



Booleans and Floats have similar casting functions (`bool()` and `float()`) that work in the same way.

### Challenges: 
1. Solve multistep math problems using Python. (Illustrates the need for variables as well as gives practice)
2. Use print and input statements to interface with a user.
3. There are many more built-in functions, have the students look them up [here](https://docs.python.org/3/library/functions.html).
