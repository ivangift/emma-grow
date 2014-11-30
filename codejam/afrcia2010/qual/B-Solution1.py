def solve(list):
    list.reverse()
    return list

def foo():
    f=open('/dev/stdin')
    cases=int(f.readline())
    for i in xrange(cases):
        list=[word for word in f.readline().split()]
        solve(list)
        print "Case #"+str(i),' '.join(list)

foo()
