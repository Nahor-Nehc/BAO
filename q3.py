
def a(n, k):
  def inner(n, k):
    # base cases

    if n == 2:
      if k == 1:
        return [1,]
      elif k == 2:
        return [1, 1]
    
    if n == 3:
      if k == 1:
        return [1,]
      if k == 2:
        return [1,1]
      if k == 3:
        return [1,0,1]
      if k == 4:
        return [1,1,1,1]
    
    p = k % (2 ** (n-2))
    b = k // (2 ** (n-2))
    
    if p == 0:
      p = n
      b = 0
    t = inner((n-1), p)
    
    if b == 0:
      return t
    
    elif b  == 1:
      zeroes = 2 ** (n-2) - p
      return t + [0 for _ in range(zeroes)] + t
  
  while k < 2 ** (n-2):
    n -= 1
  print(n, k)
  return inner(n, k)

n = int(input(""))
k = int(input(""))

binary = int("0b" + "".join(map(str, a(n, k))), base = 2)
print(binary)