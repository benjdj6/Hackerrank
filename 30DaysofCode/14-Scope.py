
def computeDifference(self):
    max_n = -1
    min_n = 101
    for e in self.__elements:
        if e > max_n:
            max_n = e
        if e < min_n:
            min_n = e
    self.maximumDifference = max_n - min_n
