'''https://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/ '''

list = [1,2,3,4,5]
newlist = list[:3]
newlist.reverse()
# print (newlist)
test = list[3:]
test.reverse()
print (newlist + test)



# list[:2].reverse()
# print (list)