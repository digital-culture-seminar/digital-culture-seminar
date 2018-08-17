# Jupyter Notebook Binder
Let's start programming!

Before we write our first Python program,
we need to install Python.
While you could install Python on your computer
with a [binary installer](https://www.python.org/downloads/),
using [pip](https://pypi.org/project/pip/),
or using the [Anaconda distribution](https://www.anaconda.com/download/),
in this tutorial
we will use a Docker container with Python.
Containers are isolated, virtualized operating systems.
The container for this course
has the Ubuntu Linux operating system
with Python 2.7 and Jupyter installed.
It is a safe, temporary development environment
that you can connect to via the web.
Open the container here
https://mybinder.org/v2/gh/baharmon/digital-culture-seminar/master,
then open the first Jupyter notebook `hello-world.ipynb`,
and follow the directions there to start programming!

# Python scripting

## Hello World!
Let's start programming in Python!
We will start with a very simple snippet of Python code.
Write a **print statement** that will output the text "Hello World!"
```python
print "Hello World!"
```

Now let's introduce ourselves.
What is your name?
Let's save it as a variable before printing it.
First we create a new variable called `myName`
and then assign it a value with a text **string**.
Type your name with double quotes around it.
```python
myName = "Anonymous"
print myName
```

Let's be more polite and introduce ourselves properly.
Use the plus sign to concatenate the string
"Hello World, my name is " with the variable myName.
```python
print "Hello World, my name is " + myName + "."
```

Now we will use the **string formatting** method
to insert a variable into a string.
```python
print "Hello {name}, this is the World!".format(name=myName)
```
