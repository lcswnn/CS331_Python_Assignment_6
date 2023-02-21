#Assignment 6, 11/07/2022

# In this assignment, you are asked to implement the class BinaryHeap (which is a priority queue);
# and an on-site sorting algorithm heapsort.
# Note that, this is a max-heap; so it satisfies max-heap-property after each method.
# We use the design of a BinaryHeap that we discussed in Lecture 16 (move popped items to the tail of the list),
# or else it is not possible to implement heapsort without using \Theta(n) extra space.

class BinaryHeap:

    # Please implement each of the following methods in class BinaryHeap following the guide.
    # Here, I've only implemented the construction method and the dunder __repr__ method. Do not change them.

    def __init__(self, data = None):
        # The default self.data is an empty list.
        # We also allow users to input a list of data, and we use max_heapify to construct the list into a heap.
        # Note that, we only let "self.data" point to the input list;
        # so all the operations are applied to the input list directly.
        # Attribute "self.heapsize" is used to record the length of current heap.
        # At first, the whole list is the heap, so self.heapsize = len(data).
        # After some items being "popped out" (moved to be tail of the list), self.heapsize will be decreased.

        ####################    DO NOT CHANGE THIS   ####################
        if data is None:
            data = []
        self.data = data
        self.heapsize = len(data)
        if len(data) > 0:
            for i in range(len(self.data) // 2 - 1, -1, -1):
                BinaryHeap.max_heapify(self,i)


    def __len__(self):
        # This implements len(BinaryHeap).
        # Return the current number of items in the BinaryHeap.
        # Not all items in self.data are in the BinaryHeap,
        # so we want to return self.heapsize instead of len(self.data).
        return self.heapsize

    def empty(self):
        # Return whether the BinaryHeap is empty or not.
        # Note that, if an item has index larger than self.heapsize - 1, then it is not in the BinaryHeap anymore.
        return self.heapsize == 0

    def max(self):
        # Return the maximum item in the BinaryHeap without popping out any item.
        # Remind that, this is a max heap.
        return self.data[0]

    def left(self, i: int):
        # Here "i" is the index of an item in the BinaryHeap, return the index of this item's left child.
        # Do not check whether the index is valid or not (larger than heapsize - 1).
        return 2*i +1

    def right(self, i: int):
        # Here "i" is the index of an item in the BinaryHeap, return the index of this item's right child.
        # Do not check whether the index is valid or not (larger than heapsize - 1).
        return 2*i + 2

    def parent(self, i: int):
        # Here "i" is the index of an item in the BinaryHeap, return the index of this item's parent.
        return (i-1)//2

    def max_heapify(self, i):
        # max_heapify is used to float the item at index i down, so that the heap-property is fixed.
        # We assume that item at index i is the only item that needs to be fixed in the subtree
        # rooted at i when we call max_heapify(self, i), and the problem is that this item is too small.
        # Please follow pseudocode in Lecture 16 to implement this method, and do not return anything in this method.
        l = BinaryHeap.left(self,i)# index
        r = BinaryHeap.right(self,i)
        if  l < self.heapsize and self.data[l]>self.data[i]:
            largest = l
        else:
            largest = i
        if r<self.heapsize and self.data[r]>self.data[largest]:
            largest = r
        if largest is not i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            BinaryHeap.max_heapify(self,largest)

    def pop_max(self):
        assert not self.empty()
        # Pop out the maximum item in the BinaryHeap, then return this item.
        # After the maximum item is popped out, it won't be deleted from the list;
        # instead, it will be swapped to index heapsize-1, then we have heapsize reduced by 1.
        # Call max_heapify to fix the max-heap-property.
        # Please follow pseudocode in Lecture 16 to implement this method.
        max = self.data[0]
        self.data[0], self.data[self.heapsize-1] = self.data[self.heapsize-1], self.data[0]
        self.heapsize -= 1
        BinaryHeap.max_heapify(self, 0)
        return max

    def increase(self, i , item):
        assert self.data[i] <= item
        # Increase the self.data[i] to item.
        # After increasing, we need to check whether item is too large for index i,
        # if too large, keep swapping it up so that the max-heap-property is fixed.
        # Do not return anything in this method.
        # Please follow pseudocode in Lecture 15 to implement this method.
        self.data[i]= item
        while i>0 and self.data[i//2] < self.data[i]:
            self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
            i = i//2

    def add(self, item):
        # Add item to the next available spot in the BinaryHeap, then call increase() to fix max-heap-property.
        # Note that, the next available spot is self.data[self.heapsize].
        # If this index is valid, simply add item to this index;
        # If not, append item to the tail of self.data.
        # Do not return anything in this method.
        # Please follow pseudocode in Lecture 16 to implement this method.
        if self.heapsize < len(self.data):
            self.data[self.heapsize] = item
        else:
            self.data.append(item)
        self.heapsize+=1
        BinaryHeap.increase(self, self.heapsize-1, item)

    def __iter__(self):
        # This implements "for item in BinaryHeap"
        # Yield each item in the current BinaryHeap.
        # Note that, items with index greater than self.heapsize - 1 are not in the BinaryHeap.
        i=0
        while i < self.heapsize:
            yield self.data[i]
            i += 1

    def __repr__(self):
        # This method implements "print(BinaryHeap)"

        ####################    DO NOT CHANGE THIS  ####################
        return "[" + ", ".join(repr(item) for item in self) + "]"


# This is the method heapsort, it is an on-site sorting algorithm, which means it only uses O(1) extra space.
# We input list to a BinaryHeap, then call pop.max() n times, where n is the length of list.
# Do not return anything in the method.
# Please follow pseudocode in Lecture 16 to implement this method.
def heapsort(list):
    bh = BinaryHeap(list)
    n = len(list)
    for i in range(n):
        item = bh.pop_max()
        list[n-i-1] = item



########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################

bh1 = BinaryHeap()
for i in range(1,11):
    bh1.add(i)
print("We start with a BinaryHeap bh1, then add numbers 1 ~ 10 to bh1. We have bh1 =", bh1, ".")

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bh2 = BinaryHeap(list3)
print("Let bh2 be another BinaryHeap that's created with input list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; "
      "then bh2 =", bh2, ".")
print("Although bh1 and bh2 consist of the same set of numbers, "
      "we can see that those numbers are stored in different orders in these BinaryHeaps.")

for _ in range(5):
    bh1.pop_max()
    bh2.pop_max()
print("After calling pop_max in both BinaryHeaps for 5 time, bh1 =", bh1, ", and bh2 =", bh2, ".")
print("We can see that both BinaryHeaps work correctly and contain numbers 1 ~ 5 in them now.")

list1 = [6, 7, 8, 9, 10, 5, 4, 3, 2, 1]
heapsort(list1)
print("Let list1 = [6, 7, 8, 9, 10, 5, 4, 3, 2, 1]. Using heapsort to sort list1, we have list1 =", list1, ".")

list2 = [2, 4, 1, 4, 4, 3, 3, 2, 3, 4]
heapsort(list2)
print("Let list2 be a list with duplicate items, after heapsort list2 =", list2, ".")