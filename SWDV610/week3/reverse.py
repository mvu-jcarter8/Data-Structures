def reverse(seq, start, stop):
    #check to make sure the list is longer than 2 elements
    if start < stop - 1:
        #get first and last element and swap positions
        seq[start], seq[stop-1] = seq[stop-1], seq[start]
        #run the function again using the next items
        reverse(seq, start+1, stop-1)

def main():
    #initialize list
    seq = [1,2,3,4,5,6,7,8,9,10]
    #run reverse function
    reverse(seq, 0, len(seq))
    #print output
    print(seq)

main()