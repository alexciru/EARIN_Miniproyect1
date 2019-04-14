class PriorityQueue:
    def __init__(self):
        self.elements = {}
        
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        self.elements.setdefault(priority, []).append(item)
    
    def get(self):
        if not self.empty():
            min_key = min(self.elements, key=self.elements.get)
            value_list = self.elements[min_key]
            value = value_list.pop(0)
            return value
        return None

    def print(self):
        print("priority queue:") + print(self.elements)