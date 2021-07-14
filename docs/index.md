---
layout: home
title: Doane CCLA HPC Workshop
subtitle: Do you want to go faster? 
---

This site contains resources to help you write code that runs more
quickly. 

In the pages that follow, we will often refer to *speedup* as a way
to compare our optimized code with its original, slower counterpart.
Speedup is a measure of how well we have improved the runtime of our code. If 
T<sub>0</sub> is the time taken by the original code, and T<sub>1</sub> is the
time taken by the improved code, then speedup is defined as 

![Speedup](../../assets/img/speedup.png)

A speedup of 2 would mean that our optimized code is twice as fast as 
the original, while any value under 1 would mean that we actually 
made our code slower!

All performance figures in this workshop were obtained on
a Windows 10 PC with an Intel&reg; Core&trade; i5-9600K CPU @ 3.70GHz
and 32GB of RAM, in Python 3.6.9 running in an Ubuntu Windows
Subsystem for Linux environment. 


[Optimizing Python](pages/optimizing-python-overview/index.html)