# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are similar in that they are collections of elements with no key attached (unlike a dictionary).  They are different, however, in that lists are mutable whereas tuples are not (you cannot sort and reverse them).  Tuples will work as keys in dictionaries because they are hashed by their contents, whereas lists are not.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets and lists are both collections of objects but a list is a mutable collection of mutable objects whereas a set is a mutable collection of immutable, unique objects.  A list can be useful for individual level data whereas a set would be useful for creating a database to search on.  
Sets do not preserve order, unlike lists and are implemented using hash tables, which means that searching them means looking checking whether an object is at the position set by its hash rather than looking through all of the values.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

The `lambda` is used to write an anonymous function (unlike the `def` method which creates a named one), which is used as an argument in higher order functions.  

An example for the `key` argument to `sorted` is to sort a list where the elements are tuples by a particular element of those tuples

list_tuples = [('b', 'P', 3), ('c', 'D', 2), ('d', 'B', 1),]  

sorted(list_tuples, key=lambda elem: elem[2])  

gives the following output:  

[('d', 'B', 1), ('c', 'D', 2), ('b', 'P', 3)]

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are ways of more simply creating lists from conditions (in order to forego using loops).  

An example is 

list1 = [1, 2, 3]  
new_list = [x - 2 for x in list1]  
new_list  
which results in  
[-1, 0, 1]  
 
To do this with map one would do the following:

list1 = [1, 2, 3]  
new_list = list(map(lambda x: x-2, list1))  
new_list  

`Filter` cuts down a list to the elements where a function returns `True`.  There is no equivalent to the above functions, however, one coud do something like 

list1 = [1, 2, 3]  
new_list = list(filter(lambda x: x>1, list1))   
new_list  

which would return  

[2, 3]  

List comprehensions are more readable and concise seem to be more widely used than `map` or `filter` but the latter two are more powerful.  

Set comprehension is similar to list comprehension.  An example that gives the same results as the list comprehension and `map` examples above is:

set1 = {x-2 for x in range (1,4)}  
set1

Dictionary comprehension to create a dictionary for a similar result is:  
dict1 = {x: x-2 for x in range(1,4)}  
dict1  


---


###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





