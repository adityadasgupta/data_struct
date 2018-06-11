#this hashtable API will deal with collisions by using linked-lists

class Hashtable:
    class Node(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __init__(self, bucket = 1000):      #list size is 1000 by default
        self.data = [None] * bucket
    
    def __getitem__(self, key):
        idx = hash(key)%len(self.data)      #the hashed index

        n = self.data[idx]
        while n:
            if n.key == key:
                return n.value
            n = n.next                      #traversing through the linked-list
        raise KeyError                      #the key may not exist in the list

    def __setitem__(self, key, value):
        idx = hash(key)%len(self.data)

        n = self.data[idx]
        while n:
            if n.key = key:
                n.val = value
                return
            n = n.next
    
    def __contains__(self, key):
        try :
            _ = self[key]
            return True
        except:
            return False