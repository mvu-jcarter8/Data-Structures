def selectionSort(alist):
    #setup loop to run through the length of the list
    for fillslot in range(len(alist)-1,0,-1):
        #initialize variable to track position for max element
        positionOfMax=0
        #run loop to check item against all others in the list
        for location in range(1,fillslot+1):
            #check to see if element value is greater than the max element current found
            if alist[location]>alist[positionOfMax]:
                #if element is greater set the new position for the max element to the current slot
                positionOfMax = location
        #create variable to hold element with the smaller value
        temp = alist[fillslot]
        #set the next slot the max element value
        alist[fillslot] = alist[positionOfMax]
        #set the current slot to the smaller value
        alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
