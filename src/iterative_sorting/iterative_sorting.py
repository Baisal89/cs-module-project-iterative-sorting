# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # establishes first index
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] <= arr[smallest_index]:
                smallest_index = j
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]



        # TO-DO: swap
        # Your code here

    return arr

#list = [1,4,6,3,7,0,9,8]
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                swapped = True
    



    return arr




# STRETCH: implement the Count Sort function below
# The maximum was arg was so we could specify the max value
# The total range if data we'll be sorting sits between 0 and maximum
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    # if maximum is not fiven, we will take the max value from the input array
    if maximum == -1:
        maximum = max(arr)

    # make bunch if buckets
    buckets = [0 for _ in range(maximum+1)]        

    for x in arr:
        if x < 0:
            return  "Error, negative numbers not allowed"
        buckets[x] +=1

    # we have the counts of every  value in our input array
    # loop through our buckets, starting at the smallest index
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1

[1,1,2,4,5,6,2,4,5]

