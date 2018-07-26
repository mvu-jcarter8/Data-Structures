#initialize recursive function
def findMax(list):
    #check if list is longer than 1 item, or output that item
    if len(list) == 1:
        return list[0]
    else:
        #get the maximum value in the list except for the first item
        maxVal = findMax(list[1:])
        #compare maxVal with first item to see which is greater
        return maxVal if maxVal > list[0] else list[0]

def findMin(list):
    #check if list is longer than 1 item, or output that item
    if len(list) == 1:
        return list[0]
    else:
        #get the minimum value in the list except for the first item
        minVal = findMin(list[1:])
        #compare the minimum value with the first item to see which is least
        return minVal if minVal < list[0] else list[0]

def main():
    #initialize list
    list = [-5,-4,-20,50,100,2,5,7,8,10,59,923,0,-23]
    #display the output from each function formatted with text
    print('Min:{}, Max:{}'.format(findMin(list),findMax(list)))

main()