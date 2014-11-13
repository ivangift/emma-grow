def solve(credit,list,item):
    for price_index in range(item):
        for price2_index in xrange(price_index+1,item):
            if list[price_index]+list[price2_index]==credit:
               return price_index,price2_index

def foo():
    i=1
    linenumber=0
    for line in open("small.txt"):
        linenumber=linenumber+1
        if linenumber==1:
           number=line
        elif linenumber==(3*i-1):
           credit=int(line)
        elif linenumber==(3*i):
           item=int(line)
        else:
           list=[int(x) for x in line.split()]
           (x,y)=solve(credit,list,item)
           print "Case#"+str(i),x+1,y+1
           i=i+1

foo()

