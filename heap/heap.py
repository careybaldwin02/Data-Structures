class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    # add the value to the array using append
    self.storage.append(value)
    # increase the size
    self.size += 1
    # use the bubble up function to position the new value in the correct node

  def delete(self):
    # store a reference to the first heap element
    # set the value of the first heap element to the value of the last heap element
    # pop from the heap's storage array to remove the last heap element
    # loop:
      # have the new first heap element check its two children using the formulas
      # if either of the element's children are larger, swap the heap value of the parent node with the value of the larger child's value vie their respective indices
    # continue loop until the element is in a spot where neither of its children are larder than it or it has reached a position where it has no children
    
    if self.size > 0:
      self.size -= 1
    return self.storage.pop()
 
  def get_max(self):
    # the maximum should always be the root element - first on the list
    max_val = self.storage[0]
    return max_val

  def get_size(self):

    pass

  def _bubble_up(self, index):
    # index is the index of the element that will be moving up the heap
    # keep bubbling the element at the given index up the heap until it reaches a valid spot
    while (index - 1) // 2 >= 0: # case where parent index exists, 0 would be root element
      #check if the element's parent value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap the values 
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
    # update the index of the parent's index so that we can keep moving up the heap
      index = (index - 1) // 2

  def _sift_down(self, index):
    # index is the index of the element that will be moving down the heap
    # keep moving element down the list until it reaches a valid place
    # check both child values 
      # plug index into both left and right child formulas and get values
      # check if one or both child values are of higher priority
      # swap chosen child value with candidate value

