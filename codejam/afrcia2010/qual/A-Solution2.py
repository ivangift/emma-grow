def solve(credit,item,list):
    dic={}
    for j in range(item):
        if credit-list[j] not in dic:
           dic[list[j]]=j
        else:
           return dic[credit-list[j]],j


def foo():
    f=open('/dev/stdin')
    cases=int(f.readline())
    for i in xrange(cases):
        credit=int(f.readline())
        item=int(f.readline())
        list=[int(x) for x in f.readline().split()]
        (x,y)=solve(credit,item,list)
        print "Case#"+str(i),x+1,y+1

foo()
