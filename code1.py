def pairsum(list1, target):
    for i in range (len(list1)-1):
        for j in range(i+1, len(list1)):
            if list1[i]+list1[j]==target:
                return(list1[i], list1[j])
