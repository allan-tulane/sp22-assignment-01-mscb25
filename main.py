"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x

    else:
      return (foo(x-2) + foo(x-1))
    pass


def longest_run(mylist, key):
  seq_count = 0
  seq_holder = 0
  for item in mylist:
    if item == key:
      seq_count += 1
    else:
      if seq_count > seq_holder:
        seq_holder = seq_count
      else:
        pass
      seq_count = 0
  
  return max(seq_count, seq_holder)
  
  


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):

  left = 0
  right = len(mylist) - 1
  
  mid = (left + right) // 2
  longest_seq = 0
  
  if mylist[mid] == key:
    while mylist[left] == key and left >= 0:
      left -= 1
    while mylist[right] == key and mid <= right:
      right += 1

    longest_seq = left + right + 1

  longest_onleft = longest_run_recursive(mylist[0:mid], key).longest_size
  longest_onright = longest_run_recursive(mylist[mid + 1:], key).longest_size

  ultimate_longest = max(longest_onleft, longest_onright, longest_seq)

  final_seq = Result(ultimate_longest, longest_onleft, longest_onright, (num == key for num in mylist))

  return final_seq
    
    

  
  
  #for item in mylist:
   #   if item == key:
    #    return self.longest_size
     # else:
      #  return longest_run_recursive(item-1)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


