
# coding: utf-8

# In[25]:

#Exo A

def match_ends(words):
    i=0
    for word in words:
        l=len(word)
        if l>=2:
            if word[-1:]==word[:1]:
                i+=1
    return i
    


# In[39]:

#Exo B

def front_x(words):
    li_x=[]
    li=[]
    for word in words:
        if word[:1]=='x':
            li_x.append(word)
        else:
            li.append(word)
    li_x.sort()
    li.sort()
    li_x.extend(li)
    return li_x


# In[56]:

#Exo C

def sort_last(tuples):
    tuples.sort(key=lambda x: x[-1])
    return tuples


# In[44]:

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# In[45]:

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


# In[46]:

main()


# In[58]:

#Exo D

def remove_adjacent(nums):
    x=''
    nums_bis=[]
    for num in nums:
        if num!=x:
            nums_bis.append(num)
            x=num
    return nums_bis


# In[80]:

#Exo E

def linear_merge(list1, list2):
    merge=[]
    l2=list2[0]
    while (list1!=[] and list2!=[]):
        l1=list1[0]
        l2=list2[0]
        if l1<l2:
            merge.append(l1)
            list1=list1[1:]
        else:
            merge.append(l2)
            list2=list2[1:]
    merge.extend(list1)
    merge.extend(list2)    
    return merge


# In[81]:

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])


# In[82]:

main()

