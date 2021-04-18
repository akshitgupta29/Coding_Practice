def subarray (list):
    sub = [[]]
    for i in range(len(list)+1):
        for j in range(i+1, len(list)+1):
            #print ('index', i)
            res = list [i:j]
            sub.append(res)
    return sub

def contiguous_subarray(list):
    pass    

if __name__ == "__main__":
    list = [3,5,2,1,4]
    print (subarray(list))