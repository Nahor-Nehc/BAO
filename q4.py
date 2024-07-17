import statistics

def distance(a):
  """a is a list of dials and returns average distance to equilibrium"""
  # 1 - 1
  # 2 - 2
  # 3 - 2
  # 4 - 1
  # 0 - 0
  
  mean = statistics.mean(a)

  differences = [abs(i-mean) if abs(i-mean) < 3 else 5 - abs(i-mean) for i in a]
  
  return abs(statistics.mean(differences) - mean)
  

def min_dist(a):
  
    dists = {distance([a[x-2], a[x-1], a[x]]): x-2 for x in range(2, len(a))}
    
    return dists[min(dists.keys())]

def smoothing(a):
  """a is a list of data and returns list with the furthest value incremented/decremented towards the mean"""
  
  mean = statistics.mean(a)
  
  b = list(map(lambda x: abs(x - mean), a))
  print(b)
  
  c = b.index(max(b))
  
  a[c] = a[c] + 1 if b[c] < mean else a[c] - 1
  
  return a

def unplug(a):
  for i in range(2, len(a)):
    if a[i-2] == a[i-1] and a[i-1] == a[i]:
      for _ in range(3):
        a.pop(i-2)
      return a
  return a

inp = [2,3,0,0,1,2,0,3,4]
while True:
  print("====")
  index = min_dist(inp)
  print(index)
  inp[index: index + 3] = smoothing(inp[index: index + 3])
  print(inp)
  inp = unplug(inp)
  print(inp)
  
  if not inp: break