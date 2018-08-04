def insertionSort(alist):
    #start loop after index 0 since the first item doesn't need to check against itself 
    for index in range(1,len(alist)):
        #initialize variable to hold current value
        currentvalue = alist[index]
        #intitialize variable to hold current position
        position = index
        #start while loop to check if the current position is not at the beginning and
        #if the previous item is greater than the current value run the inset sequence
        while position>0 and alist[position-1]>currentvalue:
            #set the position to the previous slot in the list
            alist[position]=alist[position-1]
            #reduce the position count by one to verify the correct placement
            position = position-1
    
        #set the current position value to the current value found
        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
