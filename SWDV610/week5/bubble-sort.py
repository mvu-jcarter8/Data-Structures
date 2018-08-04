#define function with variable to insert list
def bubbleSort(list):
    #initialize variable to see if swaps were performed
    madeSwap = True
    #count items in list to see how many times it should run
    runCount = len(list)-1
    #while the runs needed is greater than 0 and a swap was performed run next loop
    while runCount > 0 and madeSwap:
        #set swap to false and it will get turned back on if the internal loop runs
        madeSwap = False
        #setup range loop the length of the runs needed
        for i in range(runCount):
            #check if item in list is greater than the next item
            if list[i]>list[i+1]:
                #a swap was made, set variable to true
                madeSwap = True
                #put item into temporary variable
                temp = list[i]
                #move second item to current position
                list[i] = list[i+1]
                #reinsert temporary item back at the second position
                list[i+1] = temp            
        #decrease the runs needed since the last item is now the greatest number
        runCount = runCount-1

list = [5,3,4,7,2,1,9,10,8]
bubbleSort(list)
;print(list)