# Jerry Carter
# Maryville SWDV610
# August 23, 2018
# jcarter8@live.maryville.edu

import time

def header():
    print("File System search utility -- search for a string within a directory \nand included subdirectories and report back the location of the file \nand the total number of files found")
    print("\n -- Additionaly added speed test to compare glob versus custom algorithm --\n")
    
def searchCustom(searchVar):
    import os as os    
    #initialize search list based on all results from directory browsing
    results = list()
    #initialize search results file list
    matchList = list()
    matchCount = 0

    #get contents of directory
    for path,dirs,files in os.walk('.'):
        for name in files:
            results.append(os.path.join(path,name))
        for name in dirs:
            results.append(os.path.join(path,name))

    for item in results:
        if searchVar in item:
            matchCount = matchCount + 1
            print(item)
            #time.sleep(.1) #checking to see if timer is functioning properly
    print('Total number of results found: {}'.format(matchCount))

def searchGlob(searchVar):
    import glob
    results = glob.glob('**/*{}*'.format(searchVar), recursive=True)
    count = len(results)
    for i in results[0:count]:
        #dequeue the first entry in the list instead of default backwards setting
        print(results.pop(0))
        #time.sleep(.1) #checking to see if timer is functioning properly
    print('Total number of results found: {}'.format(count))

def timeIt(function):
    timestart = timer()
    function()
    timestop = timer()
    print(timestart - timestop)

def main():
    header()
    from timeit import default_timer as timer
    searchVar = input('Please enter your search phrase: ')

    #search with user function timed
    timestart = timer()
    searchCustom(searchVar)
    timestop = timer()
    searchTime = ((timestart - timestop)*-1000)
    print('Custom search time: {0:0.4f} milliseconds \n'.format(searchTime))

    #search with glob timed
    timestart = timer()
    searchGlob(searchVar)
    timestop = timer()
    globTime = ((timestart - timestop)*-1000)
    print('Glob search time: {0:0.4f} milliseconds \n'.format(globTime))

    if searchTime < globTime:
        winner = 'Custom search algorithm'
        winperc = globTime / searchTime
    else:
        winner = 'Glob search algorithm'
        winperc = searchTime / globTime
        
    print('And the winner is:\n')
    time.sleep(1)
    print('*********************')
    time.sleep(1)
    print('*********************')
    time.sleep(1)
    print('\n{}\n'.format(winner))
    time.sleep(1)
    print('*********************')
    time.sleep(1)
    print('*********************\n')
    time.sleep(1)          
    print('It was {:0.0f} times faster!'.format(winperc))

main()
