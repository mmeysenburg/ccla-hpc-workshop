---
layout: page
title: Optimizing Python (Using Built-Ins)
subtitle: Don't re-invent the wheel
---

<!---
-------------------------------------------------------------------------------
Introduction section
-------------------------------------------------------------------------------
-->
## Introduction

First and foremost when we are trying to make our Python code run faster, we should 
focus on taking advantage of code that is already written for us. The base Python
language has a wide variety of [built-in functions](https://docs.python.org/3/library/functions.html), 
ranging from determine an absolute value with the `abs()` function to iterating
through several lists at the same time with the `zip()` function. Generally speaking,
these built-in functions are implemented at a lower level in compiled C code, and are 
significantly faster than doing the equivalent task ourselves in Python.

## First example: finding min / max

A frequent task faced by programmers is to find the minimum and maximum elements
in a list. And, it is easy enough to write Python code to complete the task, as 
shown here in Sample 1. 

<!---
-------------------------------------------------------------------------------
Sample 1 - finding min / max of a list, with Python code
-------------------------------------------------------------------------------
-->
{% highlight python linenos %}
# assume values is a list containing floats
# in [0, 1)
minimum = 2.0
maximum = -2.0
for v in values:
    if v < minimum:
        minimum = v
    if v > maximum:
        maximum = v 
{% endhighlight %}

Sample 1 starts by initializing the variables `minimum` and `maximum` to values that
are, respectively, larger than or smaller than any element in the list could
be. Then, the code uses a `for` loop to iterate through all of the values
in the `values` list. For each value, we use an `if` statement to see if it
is smaller than the current value for `minimum`. If that is the case, we have
a new minimum value, so we update the value of `minimum`. A similar `if` statement
keeps track of the current maximum value in the variable `maximum`. After the 
loop is complete, we have examined each value in the list, and therefore
the values of `minimum` and `maximum` will be correct. 

As simple as this code is, Python has two built-in functions, `min()` and 
`max()`, that perform the same function. Sample 2 shows code that finds our
minimum and maximum values with these built-in functions instead of our
"homemade" solution in Sample 1. 

<!---
-------------------------------------------------------------------------------
Sample 2 - finding min / max of a list, with built-ins
-------------------------------------------------------------------------------
-->
{% highlight python linenos %}
mininum = min(values)
maximum = max(values)
{% endhighlight %}

The first, most obvious benefit of using the built-in `max()` and `min()` functions
is that doing so requires less typing on our part, while the code is still straightforward
and easy-to-read.

The bigger benefit, from our point of view here, is that Sample 2 is significantly
faster in execution than Sample 1, as shown in this plot:

![Native Python vs. built-in min / max](../../assets/img/built-in.png)

We can see that the speedup caused by using the built-in `min()` and `max()` functions
is roughly four, meaning that Sample 2 is approximately four times faster than the 
native Python version shown in Sample 1. To make this even more interesting, consider that
the loop in Sample 1 goes through the list only one time, while the built-in functions
in Sample 2 iterate through the list twice: once for `min()` and once again for `max()`. 
The low-level code for these built-in functions is fast enough that iterating through
the list twice to accomplish the task is still four times faster than the native Python
version. 

So, it makes good sense to keep the 70 or so Python built-in functions close at hand, mentally,
when we write code. If we can utilize these functions in our code, not only will we 
have less code to write, our code will almost certainly be faster if we use built-ins
than if we accomplish the same task with native Python code. 

## Second example: matrix multiplication

Python is known for its ease of use and for the numerous *modules* that can be
imported for just about any problem domain, as this tongue-in-cheek 
[xkcd](https://xkcd.com/) comic illustrates:

![Xkcd Python comic](https://imgs.xkcd.com/comics/python.png)

The standard distribution of Python alone contains over 200 modules, and there are
something like 137,000 other modules available to be installed and used by 
Python programmers. We cannot vouch for the quality of all 137,000 modules, 
but the odds are pretty good that there is a module already written to do some or
all of the problem you are trying to solve. Many of these modules have the extra 
benefit of being implemented in low-level C code, meaning that they are very
fast in their operation, just as we saw for the built-in `min()` and `max()`
functions. 

Here we will consider a somewhat extreme example, while also taking the opportunity
to introduce the widely used [NumPy](https://numpy.org/) scientific computing 
package. The problem we will solve is matrix multiplication, which is a very common
task in scientific computing.

If matrix A has *m* rows and *n* columns, 

![Matrix A](../../assets/img/matrix-A.png)

and matrix B has *n* rows and *p* columns,

![Matrix B](../../assets/img/matrix-B.png)

Then the matrix product *C = AB* is a new matrix of *m* rows and *p* columns where
for *i = 1..m* and *j = 1..n*,

![Matrix element](../../assets/img/matrix-element.png)

*C* as a whole looks like this:

![Matrix C](../../assets/img/matrix-C.png)

This is a very common computation, and relatively straightforward to implement, as
shown in the native Python code in Sample 3. Here, to simplify things slightly, we
are considering the multiplication of two square, *n * n* matrices. *A* and *B*
have already been constructed and filled with random values, and space for the
result matrix *C* has already been allocated. All three matrices are NumPy 
arrays, rather than Python lists of lists. 

<!---
-------------------------------------------------------------------------------
Sample 3 -- matrix multiplication in native Python
-------------------------------------------------------------------------------
-->
{% highlight python linenos %}
for i in range(n):
    for j in range(n):
        for k in range(n):
            Cn[i][j] += A[i][k] * B[k][j]
{% endhighlight %}

If you have studied computer science, particularly in the analysis of algorithms area,
the thrice-nested loops in Sample 3 probably give you pause. Since each loop 
iterates *n* times, the overall *time complexity* of this algorithm is on the order
of *n<sup>3</sup>*, which is not good. Computationally, matrix multiplication is 
expensive, and running the code from Sample 3 bears this out. On our test system,
multiplying two 1000 by 1000 matrices took, on average, approximately ???? seconds
to complete. 

We cannot do much to decrease the *n<sup>3</sup>* time complexity of matrix multiplication,
but we *can* execute our matrix multiplication using the highly optimized code
provided by the NumPy library. Sample 4 performs the same multiplication using the 
NumPy `matmul()` function. 

<!---
-------------------------------------------------------------------------------
Sample 4 -- matrix multiplication using NumPy
-------------------------------------------------------------------------------
-->
{% highlight python linenos %}
Cny = np.matmul(A, B)
{% endhighlight %}

Again, the first thing that jumps out at a reader of the code is that it is 
certainly much shorter and simpler than the native Python code above. And, if we
are honest, the experts that support NumPy are probably less likely to introduce
errors into their code than we would be if we were forced to come up with 
Sample 3 on our own.

The real difference between Sample 3 and Sample 4 becomes apparent when we compare
the run times, as shown on this plot:
