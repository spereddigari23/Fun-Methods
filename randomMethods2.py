#####   SOME MORE METHODS   #####

# 1. Given the root of a tree with an arbitrary number of children, return a list of the data values in Breadth-First Order
class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(root):
    if root==None:
        return []
    l=[]
    queue=[]
    if root.child_nodes is not None:
        for e in root.child_nodes:
            queue.append(e)
    l.append(root.data)
    while len(queue) > 0:
        c = queue.pop(0)
        l.append(c.data)
        if c.child_nodes is not None:
            for e in c.child_nodes:
                queue.append(e)
    return l

# 2. Given a non-negative number of seconds, convert it to human readable time.
def make_readable(x):
    t=[0,0,0]
    while x>=3600:
        t[0]+=1
        x-=3600   
    while x>=60:
        t[1]+=1
        x-=60  
    t[2]=x
    h=str(t[0])
    m=str(t[1])
    s=str(t[2])
    if len(h)==1:
        h="0"+h
    if len(m)==1:
        m="0"+m
    if len(s)==1:
        s="0"+s
    return h+":"+m+":"+s

# 3. Converts string delimited by dash or underscore to camel case.
import re
def to_camel_case(text):
    f=""
    if "-" in text or "_" in text:
        x=re.split(r'[-_]',text)
        f=x[0]
        for i in range(1,len(x)):
            v=x[i][0].upper()+x[i][1:].lower()
            f+=v
    return f

# 4. Given 2 lists, return a list lexographically of strings in list1 that are substrings of a string in list2.
def in_array(l1, l2):
    f=[]
    for e in l1:
        for r in l2:
            if e in r or e==r:
                f.append(e)
                break
    return sorted(set(f))

# 5. Given an integer, return it as a string in its expanded form.
def expanded_form(num):
    x=str(num)
    f=''
    le=len(x)
    for i in range(le):
        if i == le-1 and x[i]!='0':
            w=x[i]
            f=f+w
            return f
        elif x[i]!='0':
            w=x[i]
            for i in range(le-i-1):
                w+='0'
            f=f+w+" + "
    if f[len(f)-1]==' ':
        return f[:len(f)-3]
    return f

# 6. Given a list of ints (ns) and an int (t), return the indeces of the first two elements which add up to the int.
def two_sum(ns,t):
    for i in range(len(ns)):
        for w in range(i+1,len(ns)):
            if ns[i]+ns[w]==t:
                return [i,w]
    return []

# 7. Given 2 lists, return a list with all elements from list A not in list B, keeping the order.
def array_diff(a, b):
    f=[]
    for elem in a:
        if elem not in b:
            f.append(elem)
    return f

# 8. Given an array of glove colors, return the number of full pairs you can make.
def number_of_pairs(gloves):
    c=0
    d={}
    for g in gloves:
        if g not in d:
            d[g]=1
        else:
            d[g]+=1
    for e in d:
        x=d[e]
        if x>=2:
            if x%2==0:
                c+=(x/2)
            else:
                c+=(x//2)
    return c