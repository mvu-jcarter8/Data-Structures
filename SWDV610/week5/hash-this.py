class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def hashkey(self,astring):
        sum = 0
        for pos in range(len(astring)):
            #applied ordinal value times the number of the item position, aka plus 3 method
            sum = sum + ord(astring[pos])
        return sum%self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        
        #if slot is empty, set slot and data with provided attributes
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        #if slot is filled, overwrite with new data
        else:
            if self.slots[hashvalue] == key:
                #self.data[hashvalue] = data                
                
                #create list from old data plus new data
                oldvalue = self.get(hashvalue)
                valuelist = (data, oldvalue)
                
                self.data[hashvalue] = valuelist
           
           #if slot does not match key value, move to next slot and repeat
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                #after finding correct key value slot insert data
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                #recursive function to move to next slot
                else:
                    self.data[nextslot]=data

    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        
        data = None
        stop = False
        found = False
        position = startslot
        #sort through slots to find key
        while self.slots[position] != None and not found and not stop:
            #if key is found return the data found
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            #else if it is not found, check in the next slot
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
            
#initiate list to process
h=HashTable()
list = ('red','yellow','green','orange','blue','purple','magenta','cyan','white','black' )
#print('{} Values to insert: {}'.format(len(list),list))

#runCount = -1
for item in list:
    key = h.hashkey(item)
    print(h.hashkey(item), item)
    h[key]=item

print("\nHash slots: {}".format(h.slots))
print("Hash data: {}".format(h.data))
