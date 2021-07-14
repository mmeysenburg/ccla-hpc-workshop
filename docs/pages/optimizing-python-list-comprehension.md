---
layout: page
title: Optimizing Python (List Comprehension)
subtitle: Don't build a list with a for loop
---

## Introduction

One of the fundamental data structures in Python is the list. Often,
we create lists based on existing lists, or based on some iterated
values. In many of these cases, it is natural to use a `for` loop to create
the list. 

For example, suppose we are studying the quality of a pseudo-random number
generator (PRNG). To do that, we require large quantities of numbers produced by 
the PRNG, which we will pass through a series of statistical tests to determine
if the PRNG produces numbers that are "random" enough. We could prepare for 
the statistical work by creating a large Python list of pseudo-random numbers.
The straightforward approach to this task is to create and empty list, and then 
use a `for` loop to populate the list, as shown in the following code: 

{% highlight python linenos %}
# Sample 1: Building a list with a for loop

# n contains number of values to create
import random
values = []
for i in range(n): # part a 
    values.append(random.random()) # part b
{% endhighlight %}

## Simple list comprehension

Python provides a mechanism for creating lists, called *list comprehension*, 
that can be used in many instances where we might normally use a `for` loop. 
List comprehension is significantly faster than the equivalent `for` loop 
code. There are several, successively more complicated ways to use list 
comprehension, but the efficiency-boosting advice of this page is: **if you
are using a loop to build a list, see if you can use list comprehension 
instead.**

{: .box-warning}
**Tip:** If possible, build lists with list comprehension instead of loops.

In the random-list-building code above, we have the `for` loop first 
(line 4, labeled as `part a`), and the expression producing each
number that is appended to the list second (in line 5, labeled as
`part b`). List comprehension turns the order of those two elements around, 
as shown here:

```python
[<expression> for <v1> in <seq1>]
```

Here, `<expression>` corresponds to `part b`, while `for <v1> in <seq1>`
corresponds to `part b`. Essentially, the body of the `for` loop is 
specified first, and the `for` loop information itself is specified
second. 

In our list comprehension syntax, `<expression>` may be any valid
Python expression. The angle brackets (`< >`) are not part of the 
expression; instead, they mean that `<expression>` is to be replaced by
some valid Python expression. Similarly, `<v1>` is the `for` loop 
variable, and `<seq1>` is the Python sequence to iterate over. 
The `<expression>` may depend somehow on the loop variable `<v1>`,
but that is not required. 

Using list comprehension, we can create a list of random values 
in a single line of Python code, rather than the three lines required
in the `for` loop version, *and* our code will be faster than the 
`for` loop version. Here is the equivalent code using list comprehension:

{% highlight python linenos %}
# Sample 2: building a similar list with comprehension

# n contains number of values to create
import random
values = [random.random() for i in range(n)]
{% endhighlight %}

Line 2 of this code does all the work. Here, `random.random()` is the
`<expression>`, a.k.a. `part b`, `i` is `<v1>`, and `range(n)` 
is `<seq1>`. Note that in this case, the expression `random.random()`
does not depend at all on the loop variable `i`. 

To illustrate the performance improvement obtained through list comprehension, 
we executed Sample 1 and Sample 2 for values of `n` ranging from 
1,000,000 to 100,000,000 in increments of 1,000,000, and recorded the runtimes
for each trial. 

{: .box-note}
**Note:** All performance figures in this workshop were obtained on
a Windows 10 PC with an Intel(R) Core(TM) i5-9600K CPU @ 3.70GHz,
with 32GB of RAM, in Python 3.6.9 running in an Ubuntu Windows
Subsystem for Linux environment. 

Here is a plot showing the runtimes from our trials. 

![Loop vs. comprehension](https://i.imgur.com/SFw3ChO.png)

It is clear from the plot that list comprehension is significantly faster
than creating the list via a `for` loop! In fact, for the largest list, 
the list comprehension version is nearly twice as fast as the version that
uses a `for` loop.

{: .box-warning}
**Tip:** If you participate in programming competitions, list comprehension
can be a great way to get all of the numbers on an input line in a single
list, with only one line of code: `nums = [int(x) for x in input().split()]`.

## List comprehension with an `if`

We can also use an `if` statement in list comprehension, to filter the elements
that appear in the new list. 

List comprehension syntax with an `if`:

```python
[<expression> for <v1> in <seq1> if <condition>]
```

{% highlight python linenos %}
# Sample 3: filtering words with list comprehension
with open('dictionary.txt', 'r') as inFile:
    dict = [word[:-1] for word in inFile]

# make a sublist of only words that start with 'Q'
Qs = [word for word in dict if word[:1] == 'Q']

print(Qs)
{% endhighlight %}

Sample output:

```
['Q', "Q'S", 'QA', 'QADDAFI', ... 'QUOTING', 'QWERTY', 'QWERTYS']
```

## List comprehension with multiple `for`s

List comprehension syntax with multiple `for`s:

```pyhthon
[<expression> for <v1> in <seq1> 
              for <v2> in <seq2>
              for <v3> in <seq3>
              ...
              if <condition>]
```

Sample code showing how list comprehension with multiple `for` statements
works:

{% highlight python linenos %}
letters = ['a', 'b', 'c', 'd']
digits = [1, 2, 3]

values = [(x, y) for x in letters for y in digits]

print(values)
{% endhighlight %}

Output of the preceding example: 

```
[('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3), ('d', 1), ('d', 2), ('d', 3)]
```

## Exercise

Exercise: the code shown below creates a large list of pseudo-random
numbers in [0, 100000), then uses a `for` loop to create a new list 
containing only the even values. Re-write this code to use list 
comprehension to create the `evenValues` list. 

{% highlight python linenos %}
# list creation
rawValues = [random.randrange(0, 100000) for i in range(100000000)]

# loop version
evenValues = []
for v in rawValues:
    if v % 2 == 0:
        evenValues.append(v)
{% endhighlight %}