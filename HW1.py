import collections
def maketable(s1, s2):
    dict = {}
    i = 0
    while i<len(s1):
        temp = {s1[i] : s2[i]}
        dict.update(temp)
        i=i+1
    return dict
    pass
def trans(ttable, s):
    for c in s:
        if ttable.has_key(c):
            c=ttable.get(c)
    return s
    pass
def testtrans():
    ttable = makettable('abc', 'xyz')
    revttable = makettable('xyz', 'abc')
    tests = "Now I know my abc's"
    answer = "Now I know my xyz's"
    if trans(ttable, tests) != answer: return False
    if trans(revttable, trans(ttable, tests)) != "Now I know mb abc's": return False
    if trans(ttable,'') != '': return False
    if trans(makettable('',''), "abc") != 'abc': return False

    return True
    pass
def histo(s):
    dict = {}
    s=sorted(s)
    for c in s:
        if c in dict:
            dict[c]=dict.get(c,0)+1
        else:
            dict.update({c:1})
    return collections.OrderedDict(sorted(dict.items(), key=lambda t: t[1], reverse=True))
    pass
def testhisto(s):
    #test1 = 'implemented'

    print(histo(s))
testhisto('test stuff')

#dictionary = maketable("abcdefg", "gfedcba")
#print(dictionary)

#if testtrans:
#    print("hooray")
#else:
#    print(":(")
