import unittest
from MinHeap import MinHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.min_heap = MinHeap()

    def test_insert_and_delete_min(self):
        #creating a min heap
        self.min_heap.insert(5)
        self.min_heap.insert(3)
        self.min_heap.insert(7)
        self.min_heap.insert(1)
        self.min_heap.insert(9)

        #the min should be deleted, root = min
        self.assertEqual(1, self.min_heap.delete_min())
        self.assertEqual(3, self.min_heap.delete_min())
        self.assertEqual(5, self.min_heap.delete_min())
        self.assertEqual(7, self.min_heap.delete_min())
        self.assertEqual(9, self.min_heap.delete_min())
        self.assertIsNone(self.min_heap.delete_min())  
        #min heap should be empty now

    def test_heap_sort(self):
        #creating a min heap
        self.min_heap.insert(5)
        self.min_heap.insert(3)
        self.min_heap.insert(7)
        self.min_heap.insert(1)
        self.min_heap.insert(9)

        expected_sorted_list = [1, 3, 5, 7, 9]
        #sort heap
        sorted_list = self.min_heap.heap_sort()
        #check if it matches the expected list
        self.assertListEqual(expected_sorted_list, sorted_list)

if __name__ == "__main__":
    unittest.main()
