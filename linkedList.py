#singly linked lists
class LinkedList:       
    class Node(self, val, next=None):
        self.val = val 
        self.next = next
    def __init__(self):
        self.head = None
        self.count = 0
    def append(value):
        if len(self)==0 :
            self.head = LinkedList.Node(value, self.head)
            self.count += 1
        else :
            n = self.head
            while n:
                n = n.next      #to go to the end of the linked-list
            n.next = LinkedList.Node(value)
    def __len__(self):
        return self.count
    def __iter__(self):     #to use keywords such as 'in'
        n = self.head
        while n:
            yield n.val
            n = n.next
    def remove(idx):        #removing value at index
        #c = 0
        n = self.head
        for i in range(idx):
            n = n.next
        n.next = n.next.next       #removing the element between n and n.next.next
        
