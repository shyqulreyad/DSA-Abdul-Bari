class _Node:
    __slots__ = '_element', '_next' # streamline memory usage
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def addlast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size +=1
        
    def display(self):
        p = self._head
        
        while p:
            print(p._element,end='<-->')
            p = p._next
        print()
            
l = LinkedList()
l.addlast(7)
l.addlast(4)
l.addlast(12)
l.addlast(19)
l.addlast(33)
l.addlast(54)
l.addlast('www')
l.addlast('test number')
l.addlast('2345esgr')
l.addlast('test number')
l.addlast('2345esgr')
l.display()