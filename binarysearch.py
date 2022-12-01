# iterate using while loop until key is found
def result(l,low,high,key):
    while low<=high:     
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:    #if key is smaller select the lower sub-list
            high=mid-1
        elif l[mid]<key:    #if key is bigger select the higher sub-list
            low=mid+1
    return -1

#given list
l=[5,8,9,10,32,36,37,45]
low=0  #lower index
high=len(l)  #higher index
key=int(input("enter key:"))   #search element
res=result(l,low,high,key)   #menthod calling
if res==-1:
    print("key not found for first list")
else:
    print("element found at {} position for first list".format(res+1))
