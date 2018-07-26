#initialize recursive function
def findMax(list):
    if len(list) == 1:
        return list[0]
    else:
        maxVal = findMax(list[1:])
        return maxVal if maxVal > list[0] else list[0]

def findMin(list):
    if len(list) == 1:
        return list[0]
    else:
        minVal = findMin(list[1:])
        return minVal if minVal < list[0] else list[0]
    
list = [-5,-4,-20,50,100,2,5,2,7,8,10,59,923,0,-23]
print('Max:{}, Min:{}'.format(findMax(list),findMin(list)))