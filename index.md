Lauren Ferrier

November 30, 2022

Foundations of Programming, Python

Assignment 07

[Git Hub](https://github.com/laf2012/IntroToProg-Python-Mod06)[Repository](https://github.com/laf2012/ITFnd100-Mod07)

[Git Hub Website](https://laf2012.github.io/ITFnd100-Mod07/)

# Managing Rabbits - A Python Script of Pickling & Error handling

# Introduction

This document details the steps taken to create a script for managing our user's love for all things rabbits with a rabbit management list! The theme with this script is similar to previous modules that implemented "todo" and home inventory lists with loops and lists, but this week's script has instead been designed to demonstrate pickling and error handling.

# Steps Taken for Assignment 07

1. This assignment was completed within [PyChar](https://www.jetbrains.com/pycharm/download/#section=windows)[m](https://www.jetbrains.com/pycharm/download/#section=windows)[(](https://www.jetbrains.com/pycharm/download/#section=windows)Jet Brains, 2022).

1. Within PyCharm, I opened the Lab7-1\_Starter.py that was provided with this week's course materials. Our module notes this week (\_MOD7PYTHONPROGRAMMINGNOTES.DOCX 2022, PG 14) contained an exercise that got us practicing pickling.
 ![](RackMultipart20221201-1-u2jf0j_html_74596d2dbfc6fe8f.png)

_Figure 1 Lab 7-1 served as the initial inspiration behind our eventual, completed script. Note the use of **import pickle** to signify what functions we will need to complete under **save\_data\_to\_file** and **read\_data\_from\_file** functions._

1. Our notes had previously provided us a further example on pickling functions that I reviewed to help me begin filling out the TODO portions of our started script above.
 ![](RackMultipart20221201-1-u2jf0j_html_7b2dddeb8249e20.png)

_Figure 2 Above we are presented with the ability to open a dat file that will store our eventual, appended binary output. To ensure that this data in indeed saved in binary, the **pickle.dump()** function is defined with the variables we want stored ( **lstCustomer** and **objFile** ). Since we then want to additionally read the stored data, we are also are implementing the **pickle.load()** function (\_MOD7PYTHONPROGRAMMINGNOTES.DOCX 2022, PG 13)_

1. However, to first fully understand the above functions, I wanted to further explore Pickling in more depth. I visited [AfterNerd](https://www.afternerd.com/blog/python-pickle/) (Karim, 2022). This website not only defined pickling in python, but also provided numerous examples in a tutorial format. A few concepts that were explored are as follows (and expanded upon with additional resources):
  1. Any object in Python can pickled for saving into memory, and pickling is the process of serializing or deserializing these objects. In more detailed terms, this is Python converting objects into character streams that contain all the info necessary to reconstruct the objects.
  2. Pickle is often opted for a variety of reasons: text files take more disk space and are not as scalable for schema purposes.
  3. Pickle is one of several serialization protocols available, with others being json or protocol buffers.
  4. Not everything can be pickled, but several topics we have explored so far in this class are compatible, such as: integers, floating-point numbers, strings, tuples, lists, dictionaries, functions, and classes ([Python Software Foundation](https://docs.python.org/3/library/pickle.html), 2022).
2. With the above in mind, I completed Lab 7-1. This will serve as a template for our eventual example of pickling in our Rabbit Management script!
 ![](RackMultipart20221201-1-u2jf0j_html_22305a99f15f1fe.png)

_Figure 3 Note the incorporation of the Presentation section of our script to grab our user's input for appending to our file._

1. However, I next want to explore how I can add structured error handling into my script. The idea behind this concept is that we can trap errors in our program using a try-except block of code to assist with how our program handles errors versus letting Python choose its default action (\_MOD7PYTHONPROGRAMMINGNOTES.DOCX 2022, PG 15). The need for this became apparent as I tested my developing Rabbit Management script, which I will detail further in our next few steps!


2. To get to our need for error handling and the trigger for exploring this concept more, I first continued forward with my vision for my Rabbit Management script, which is as follows: _a script that will take a user inputted ID and name of a rabbit, store it into memory via pickling, and then upon exiting our script, display back all our stored bunnies_. To streamline this, it made sense to first tackle the functions shown in Figure 3. To do this, I edited my functions to the below:
 ![](RackMultipart20221201-1-u2jf0j_html_9db7104408f82943.png)

_Figure 4 Note our edited two functions from Figure 3._

1. I then moved on to creating our presentation to the user that incorporated a loop for continual entry of bunnies or an option to exit our script.
 ![](RackMultipart20221201-1-u2jf0j_html_f4d08641039ab03d.png)

_Figure 5 Our user presentation that will collect the inputs of ID and name per rabbit via a while loop. These are the inputs that will eventually be pickled into storage via the functions we defined in figure 4._

1. Upon running the script created thus far, things seemed to be in working order, until the exit option was selected!
 ![](RackMultipart20221201-1-u2jf0j_html_3dc111773f91b8d4.png)

_Figure 6 Our script is not displaying all the rabbits stored in our file, just the first line. An expected error based off the note on **list\_of\_data = pickle.load(file**) from Figure 4. We are only loading one line at a time._

1. This is an indication that we need to go back and edit our functions, and an additional opportunity to begin error handling presented itself. Our issue above is that we are loading data into a list and then attempting to read from that point. What we need to do is establish a continuous loop that will read all our appended data before closing out and returning all our entries at once. However, this can be tricky if starting this script fresh with no text in your file, because then you may receive an EOFError ([Pansuriya](https://dev.to/rajpansuriya/eoferror-eof-when-reading-a-line-12fe#:~:text=In%20Python%2C%20an%20EOFError%20is,EOF)%20without%20reading%20any%20input.), 2022). To achieve a solution to this, I edited my script to the following:
 ![](RackMultipart20221201-1-u2jf0j_html_f840483401965c9d.png)

_Figure 7 My edited **read\_data\_from\_file** function with additional error handling for potential EOFErrors upon initial start of this loop. Assistance with formatting was provided with guidance from this week's module notes (\_MOD7PYTHONPROGRAMMINGNOTES.DOCX 2022, PG 15)._

1. From here, I wanted to tackle the presentation of my stored rabbits since they currently were displayed back in a less than friendly manner:
 ![](RackMultipart20221201-1-u2jf0j_html_45a0a79c9aafebef.png)

_Figure 8 Our current output of rabbits._

1. To organize the presentation of these rabbits, I created a new function to accompany my existing two.
 ![](RackMultipart20221201-1-u2jf0j_html_4ed39904d60f4486.png)

_Figure 9 A new function for better organizing the presentation of all our user inputted data._

1. To accompany the above function, I then edited the finale of my script with an accompanying print statement upon exiting the script.
 ![](RackMultipart20221201-1-u2jf0j_html_e3a3cfb69a412b33.png)

_Figure 10 Our new print statement for better review of our stored data._

1. This presents our rabbits in a much more organized manner!
 ![](RackMultipart20221201-1-u2jf0j_html_deabb760e3af83de.png)

_Figure 11 Our resulting list of bunnies from our above print statement in Figure 12._

1. However, I still want to incorporate one additional error handling example. Ideally because I want my user to only be permitted to input an integer value for any given Rabbit ID.
 ![](RackMultipart20221201-1-u2jf0j_html_6ac91cf3d123a52e.png)

_Figure 12 Above is a demonstration of Exception Handling that presents our user with a custom message if they try to input a value that is not an integer for their Rabbit ID_

1. We now have our script complete!
 ![](RackMultipart20221201-1-u2jf0j_html_63955f02ed9ec2af.png)

_Figure 9 Completed Assignment 07. As shown in PyCharm._

![](RackMultipart20221201-1-u2jf0j_html_4e2254e6986eb628.png)

_Figure 10 Completed Assignment 07, as shown in a command window._

![](RackMultipart20221201-1-u2jf0j_html_a75a8e4fbab98244.png)

_Figure 11 Resulting RabbitMamagement.dat from Assignment 07's executed script._

# Summary

Using our provided course materials, I created a script that permits a user to store an appending list of rabbits in binary while additionally introducing exception handling. While previous week's explored concepts used in this script such as loops and lists, Module 7 took this further by incorporating different methods of storing data and engaging with our users when it comes to interacting with our script.
