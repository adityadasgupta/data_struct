class ArrayList():
    def __init__(self):
        self.data = []
    def add(self, value):
        self.data.append(value)  #using the methods of a list
    def __setitem__(self, idx, value):
        self.data[idx] = value
    def __getitem__(self,idx):
        return self.data[idx]
    def __delitem__(self,idx):
        for i in range(idx, len(self.data):
             self.data[i-1] = self.data[i]
    def size(self):
        return len(self.data)
        
    