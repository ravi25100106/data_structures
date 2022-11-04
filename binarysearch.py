def result(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        elif l[mid]<key:
            low=mid+1
    return -1
l=[5,8,9,10,32,36,37,45]
low=0
high=len(l)
key=int(input("enter key:"))
res=result(l,low,high,key)
if res==-1:
    print("key not found for first list")
else:
    print("element found at {} position for first list".format(res+1))