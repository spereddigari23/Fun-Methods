#####   JUST A COUPLE OF RANDOM METHODS   #####

# 1. Function that takes string and returns a character not repeated.
def first_non_repeating_letter(s):
    for i in range(len(s)):
        w=s[i]
        c=s[i].lower()
        if c not in s[i+1:].lower() and c not in s[:i].lower():
            return w
    return ''

# 2. Function that takes a string of parenthases and determines if logical.
def valid_parentheses(string):
    o=0
    cl=0
    t=0
    for c in string:
        if cl > o:
            return False
        if c=='(':
            o+=1
        elif c==')':
            cl+=1
    if o != cl:
        return False
    return True

# 3. Takes a string with a number at the end and returns it with the number incremented.
def increment_string(s):
    for i in range(len(s)):
         if s[i:].isnumeric()==True:
                f=s[:i]+str(int(s[i:])+1)
                p=len(s)-len(f)
                r=""
                if p>0:
                    while p>0:
                        r+="0"
                        p-=1
                return s[:i]+r+str(int(s[i:])+1)
    return s+"1"

# 4. Substitution cypher function that replaces each letter with 13th letter after.
def rotate13(encodeme):
    a=list('abcdefghijklmnopqrstuvwxyz')
    s=''
    for c in encodeme:
        if c==' ':
            s+=' '
        elif c.lower() not in a:
            s+=c
        else:
            v=c.lower()
            i=a.index(v)
            n=i+13
            if n>25:
                n-=26
            if c.islower():
                s=s+a[n].lower()
            elif c.isupper():
                s=s+a[n].upper()
    return s

# 5. Given two strings, returns true if a portion of the first can be scrambled to match the second.
def scramble(s1, s2):
    d={}
    for c in s1:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    w={}
    for c in s2:
        if c not in w:
            w[c]=1
        else:
            w[c]+=1
    for e in w:
        if e not in d:
            return False
        else:
            if d[e]<w[e]:
                return False
    return True

def scramble_2(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

# 6. Takes a string, returns with a hashtag at front, all first letters capitalized; if the result is >140 chars->False
def generate_hashtag(s):
    if s=='':
        return False
    f="#"
    x=s.split(" ")
    for e in x:
        if e!='':
            f+=e[0].upper()+e[1:].lower()
    if len(f)>140:
        return False
    return f

# 7. Pig Latin Translator, moves the first letter of every word to end +'ay'
def pig_it(text):
    f=""
    x=text.split(" ")
    ww=list('!?.')
    for e in x:
        if len(e)!=1:
            c=e[0]
            string=e[1:]+c+"ay"
            f+=string+" "
        else:
            if e not in ww:
                stri=e+"ay"
                f+=stri+" "
            else:
                f+=e+" "
    return f.rstrip()

# 8. Function that takes word and a list of words and returns a list of anagrams from the given list.
def anagrams(word, words):
    l=[]
    w={}
    for c in word:
        if c not in w:
            w[c]=1
        else:
            w[c]+=1
    for e in words:
        d={}
        for c in e:
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
        if w==d:
            l.append(e)
    return l

# 9. Computes the Mean Squared Error of two integer lists.
def solution(a,b):
    x=0
    for i in range(len(a)):
        x+=pow(b[i]-a[i],2)
    return x/len(a)

# 10. Takes a list of ints and moves zeroes to the end while preserving list order.
def move_zeros(a):
    f=[]
    for e in a:
        if e!=0:
            f.append(e)
    x=len(a)-len(f)
    for i in range(x):
        f.append(0)
    return f

# 11. Takes a number n and returns the sum of n square perimeters where each side is a fibonacci number.
def perimeter(n):
    o=1
    t=1
    tot=1
    for i in range(n):
        tot+=(o)
        o+=t
        t=o-t
    return tot*4