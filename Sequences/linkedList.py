class LinkedList:

    # The _Node class is used internally by LinkedList class . It is invisible
    # from the outside the class due to the two undescores that precede the class
    # name. Python mangles names so that they are not recognizable outside the class 
    # when two underscores precede a name but aren't followed by underscores at the end 
    # of the name(i.e  an operator name)

    class __Node:
        def __init__(self,item,next =None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setItem(self, item):
            self.item = item
        
        def setNext(self, next):
            self.next = next

    def __init__(self, contents=[]):
        # Here we keep a reference to the first node in the linked list 
        # and the last item in the linked list. The both point to a dummy
        # node to begin with.This dummy node will always be in the first
        # position in the list and will never contain an item. Its purpose
        # is to eliminate special cases in the code below.
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()
        raise IndexError("LinkedList Index out of range")

    def __setitem__(self, index,val):
        if index >0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            
            cursor.setItem(val)
            return
        raise IndexError("LinkedList assignment index out of range")

    def insert(self,index,item):
        cursor = self.first
        
        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
    
    def __add__(self, other):
        if type(self) !=type(other):
            raise TypeError("Concatenate undefined for" + str(type(self))+ " + "+ str(type(other)))

        result = LinkedList()
        cursor = self.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        cursor = other.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        return result
    
    def __contains__(self, item):
        cursor = self.first.getItem()
        while cursor and cursor != item:
            cursor = cursor.next().getItem()
        return cursor
    
    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems +=1
    
def main():
    lst =LinkedList()
    for i in range(100):
        lst.append(i)
    lst2 = LinkedList(lst)

    print(lst)
    print(lst2)

    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 failed")
    
if __name__ == "__main__":
    main()