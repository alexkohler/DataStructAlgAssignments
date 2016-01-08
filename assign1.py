def binarySearch(alist, target):
    low = 0
    high = len(alist)-1
    while low <= high:
                mid = (low+high)//2
                if alist[mid] > target:
                        high = mid-1
                elif alist[mid] < target:
                        low = mid+1
                #if our current array value wasn't higher/lower than the key, then it has no choice but to be the key itself.
                else:
                        return mid
    return -1


#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE	

#Read input
f = open("input.txt", "r")
inputlist = [int(x) for x in f.readline().split()] 
target, values = inputlist[0], inputlist[1:]
print(binarySearch(values, target))

