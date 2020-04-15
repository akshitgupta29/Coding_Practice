list = [1,2,3,4]
sub = [[]]
for i in range(len(list)+1):
    for j in range(i+1, len(list)+1):
        #print ('index', i)
        res = list [i:j]
        sub.append(res)
print (sub)