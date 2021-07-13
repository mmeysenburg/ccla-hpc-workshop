---
layout: page
title: Optimizing Python (Overview)
subtitle: Need to speed your code? Start here!
---

If you have running Python code that correctly solves your problem,
congratulations! That's most of the battle. If you need to make the
code do its job faster, then this page is the place to begin. 

Unless we take special steps to make it otherwise,
[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
is an _interpreted_ language, as opposed to languages like 
[Fortran](https://en.wikipedia.org/wiki/Fortran),
[C](https://en.wikipedia.org/wiki/C_(programming_language)),
or [C++](https://en.wikipedia.org/wiki/C%2B%2B),
which are _compiled_ languages. If you want to spend a few minutes, here is 
an approachable article on the [difference between interpreted languages and
compiled languages](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/). 

The upshot for us here is that interpreted languages generally run much more 
slowly than compiled languages. (Java is somewhere in between - Java code is 
compiled to _bytecode_, that is executed on a virtual machine that is running 
on the "bare metal" of your computer.) Accordingly, programs we write in Python may 
take much, much longer to execute for the same data than the equivalent program 
written in a compiled language like Fortran or C would. 

All is not lost! If we apply some simple optimization techniques to our code, we can
create Python code that is almost as fast as the compiled equivalent, with the 
added advantage that we can write in Python instead of one of those harder-to-learn
languages. 

Our biggest bang-for-the-buck, optimization-wise, is to focus on loops. We 
will take advantage of several Python tips and tricks to speed up our loops,
or to eliminate them entirely!

Next up: [Optimizing Python (List Comprehension)](../optimizing-python-list-comprehension/index.html)