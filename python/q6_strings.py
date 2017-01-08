# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0



1.

def donuts(count):
    if count <10:
        return 'Number of donuts: %d' % count
    else:
        return 'Number of donuts: many'
2.  
    
def both_ends(s):
    if len(s)>1:
        return s[0:2]+s[-2:]
    else:
        return ''
3.  
    
def fix_start(s):
    temp = [s[0]]
    for letter in s[1:]:
        if letter == s[0]:
            temp.append('*'),
        else:
            temp.append(letter),
    return (''.join(temp))
4.  

def mix_up(a, b):
    return b[0:2] + a [2:] + ' ' + a[0:2] + b[2:]

5. 

def verbing(s):
    if len(s)<3:
        return s
    elif s[-3:] == 'ing':
        return s + 'ly'
    else:
        return s + 'ing'  


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
