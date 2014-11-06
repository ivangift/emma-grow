i=1
linenumber=0
for line in open("small.txt"):
    linenumber=linenumber+1
    if linenumber==1:
       number=line
    elif linenumber==(3*i-1):
       credit=int(line)
    elif linenumber==(3*i):
       item=line
    else:
       list=[int(x) for x in line.split(' ')]
       for price_index in range(int(item)):
           list2=list[price_index+1:]
           for price2_index in range(int(item)-(price_index+1)):
               if list[price_index]+list2[price2_index]==credit:
                  print "Case#"+str(i),price_index+1,price_index+price2_index+2
           price2=None
       i=i+1

