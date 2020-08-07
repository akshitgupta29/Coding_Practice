class Difference:

    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = abs(self.__elements[0] - self.__elements[1])

        # Add your code here
        for i in range(len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                diff = abs(self.__elements[i] - self.__elements[j])
                if diff > self.maximumDifference:
                    self.maximumDifference = diff
        return self.maximumDifference

class Difference_n:
    def __init__(self,a) -> None:
        self.__elements = a
    

# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
