class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return i // 2
    
    def left_child(self, i):
        return 2 * i
    
    def right_child(self, i):
        return 2 * i + 1
    
    def insert(self, node):
        #add new node to end of array
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)
    
    def delete_min(self):
        #check if heap empty
        if not self.heap:
            return None
        #min is root
        min_value = self.heap[0]
        #remove last element
        last_value = self.heap.pop()
        if self.heap:
            #last element becomes root
            self.heap[0] = last_value
            #adjust heap
            self.heapify_down(0)
        return min_value
    
    def heapify_up(self, i):
        #compare the node to its parents and adjust heap if needed 
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]: 
            #value of the current element < parent's value then move current element up
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
            #terminate when current element reaches root (index 0) or its parent<=current
    
    def heapify_down(self, i):
        #obtain children and current node (root)
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        #check if left/right child exists in heap and if its value is smaller than the current smallest element
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        #check if root is the smallest
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)
    
    def heap_sort(self):
        sorted_list = []
        while self.heap:
            #add the deleted elements (min) to the list
            sorted_list.append(self.delete_min())
        return sorted_list
