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
6. 

def not_bad(s):
    if s.find('not')<s.find('bad'):
        return s[:s.find('not')] + 'good' + s[s.find('bad')+3:]
    else:
        return s
7.
    
def front_back(a, b):
    if len(a)%2 == 0 and  len(b)%2 == 0:
        return a[:len(a)/2]+b[:len(b)/2]+a[len(a)/2:]+b[len(b)/2:]
    elif len(a)%2 > 0 and  len(b)%2 == 0:
        return a[:len(a)/2 +1]+b[:len(b)/2]+a[len(a)/2+1:]+b[len(b)/2:]
    elif len(a)%2 == 0 and  len(b)%2 > 0:
        return a[:len(a)/2]+b[:len(b)/2+1]+a[len(a)/2:]+b[len(b)/2+1:]
    else:
        return a[:len(a)/2+1]+b[:len(b)/2+1]+a[len(a)/2+1:]+b[len(b)/2+1:]  
