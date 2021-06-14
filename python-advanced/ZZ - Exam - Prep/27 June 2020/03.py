def list_manipulator(nums, *args):
    from collections import deque

    nums = deque(nums)

    if args[0] == 'add':
        new_nums = args[2:]
        if args[1] == 'beginning':
            for n in reversed(new_nums):
                nums.appendleft(n)
        elif args[1] == 'end':
            for n in new_nums:
                nums.append(n)
    elif args[0] == 'remove':
        if len(args) > 2:
            nums_to_remove = int(args[2])
        else:
            nums_to_remove = 1
        if args[1] == 'beginning':
            for n in range(nums_to_remove):
                nums.popleft()
        elif args[1] == 'end':
            for n in range(nums_to_remove):
                nums.pop()

    return list(nums)

import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(list_manipulator([1,2,3], "remove", "end"), [1, 2])                   
        self.assertEqual(list_manipulator([1,2,3], "remove", "beginning"), [2, 3])             
        self.assertEqual(list_manipulator([1,2,3], "add", "beginning", 20), [20, 1, 2, 3])            
        self.assertEqual(list_manipulator([1,2,3], "add", "end", 30), [1, 2, 3, 30])                  
        self.assertEqual(list_manipulator([1,2,3], "remove", "end", 2), [1])                
        self.assertEqual(list_manipulator([1,2,3], "remove", "beginning", 2), [3])          
        self.assertEqual(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40), [20, 30, 40, 1, 2, 3])    
        self.assertEqual(list_manipulator([1,2,3], "add", "end", 30, 40, 50), [1, 2, 3, 30, 40, 50])          

if __name__ == "__main__":
    unittest.main()