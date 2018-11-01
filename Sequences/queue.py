class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newItems = [] 
        for i in range(self.frontIdx, len(self.items)):
            newItems.append(self.items[i])

        self.items = newItems
        self.frontIdx = 0
    
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")

            # When queue is half full, compress it. This
            # achieves an amortized complexity of O(1) while
            # not letting the list continue to grow unchecked
        if self.frontIdx * 2  > len(self.items):
            self.__compress()
            
        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item
    
    def enqueue(self, item):
        self.items.append(item)
    
    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access the front of the queue")

        return self.items[self.frontIdx]
    
    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def clear(self):
        self.items = []
        self.frontIdx = 0

def main():
    q = Queue()
    items = list(range(10))
    items2 = [] 

    for k in items:
        q.enqueue(k)
    
    if q.front() == 0:
        print("Test 1 passed")
    else:
        print("Test 1 Failed")

    while not q.isEmpty():
        items2.append(q.dequeue())

    if items2 != items:
        print("Test 2 Failed")
    else:
        print("Test 2 passed")

    for k in items:
        q.enqueue(k)

    items2 = []

    while not q.isEmpty():
        items2.append(q.dequeue())

    if items2 != items:
        print("Test 3 Failed")
    else:
        print("Test 4 passed")
    
    try:
        q.dequeue()
        print("Test 4 Failed")
    
    except RuntimeError:
        print("Test 4 passed")
    except:
        print("Test 4 Failed")
    
    try:
        q.front()
        print("Test 5 failed")
    
    except RuntimeError:
        print("Test 5 passed")
    except:
        print("Test 5 Failed")
if __name__ == "__main__":
    main()