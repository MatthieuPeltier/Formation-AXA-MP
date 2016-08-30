
# coding: utf-8

# In[14]:

#Exo A

def donuts(count):
    return ('Number of donuts: ' +str(count) if (count<10) else 'Number of donuts: many')


# In[17]:

def both_ends(s):
    return (s[:2] + s[-2:] if len(s)>1 else '')


# In[25]:

def fix_start(s):
    s1=s[:1]
    s2=s[1:]
    return (s1 + s2.replace(s1,'*'))


# In[35]:

def mix_up(a, b):
    return b[:2] + a[2:] +' ' + a[:2] + b[2:]


# In[36]:

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# In[37]:

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# In[38]:

main()


# In[40]:

def verbing(s):
    if len(s)>2:
        if (s[-3:]=='ing'):
            s= s + 'ly' 
        else:
            s= s + 'ing'
    return s


# In[54]:

def not_bad(s):
    
    if ('not' in s and 'bad' in s):
        n=s.index('not')
        b=s.index('bad')
        if (n<b):
            s=s[:n] + 'good' + s[b+3:]
    return s


# In[69]:

def front_back(a, b):
    l_a=len(a)
    #print(l_a)
    l_b=len(b)
    #print(l_b)
    droite_a=int(l_a/2)
    #print(droite_a)
    droite_b=int(l_b/2)
    #print(droite_b)
    return a[:(l_a-droite_a)] + b[:(l_b-droite_b)] + a[-droite_a:] + b[-droite_b:]


# In[70]:

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# In[71]:

main()


# In[ ]:



