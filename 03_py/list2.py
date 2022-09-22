def count_evens(nums):
  count = 0
  for e in nums:
    if e % 2 == 0:
      count+=1
  return count
  
# count_evens([2, 11, 9, 0]) → 2	
# count_evens([2]) → 1
# count_evens([2, 5, 12]) → 2	

def big_diff(nums):
  mi = nums[0]
  ma = nums[0]
  
  for e in nums:
    mi = min(e, mi)
    ma = max(e, ma)
    
  return (ma - mi)

def centered_average(nums):
  mi = nums[0]
  ma = nums[0]
  s = 0
  for e in nums:
    mi = min(e, mi)
    ma = max(e, ma)
    s += e
  return (s - mi - ma) / (len(nums) - 2)

def sum13(nums):
  if len(nums) == 0:
    return 0
  
  s = 0
  i = 0
  while i < len(nums):
    if nums[i] == 13:
      i += 2
    else :
      s += nums[i]
      i+=1
  return s

def sum67(nums):
  if len(nums) == 0:
    return 0
  
  i = 0
  s = 0
  while i < len(nums):
    if (nums[i] == 6):
      i+=1
      while (nums[i] != 7):
        i+=1
      i+=1
    else:
      s+= nums[i]
      i+=1
      
  return s

def has22(nums):
  i = 0 
  
  while (i < (len(nums) - 1)):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
    i+=1
    
  return False
