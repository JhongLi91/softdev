
'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
diff21(0) → 21	
diff21(1) → 20	
diff21(2) → 19	
diff21(-1) → 22	
DISCO: Learned something cool here. The abs function in Python as it is in Java. 
abs(a-b) gives you the absolute value of the difference between a-b. Swag. 
'''

def diff21(n):
  if n > 21:
    return abs(21-n) * 2  #found absolute difference then multiplied by 2 since n is over 21
  
  else:
    return abs(21-n) #found absolute difference
    
  '''
Front = first 3 chars of the string
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'	
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'	
front3('abcXYZ') → 'abcabcabc'	
DISCO: You can copy/repeat strings just by using the * sign. 
'''

def front3(str):
  if (len(str) < 3): #tests if length is less than 3
    return str * 3 #if so, just copies the entire str 3 times
  front = str[0:3] #takes the first 3 chars
  return front * 3 #copies front 3 times
