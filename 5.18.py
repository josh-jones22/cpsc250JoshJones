''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
def solve(a, b, c, d, e, f):
  #iterate x from -10 to 10
  for x in range(-10, 11):
    #iterate x from -10 to 10
    for y in range(-10, 11):
      #check that both string satisfy or not
      if (((x * a) + (y * b) == c) and ((x * d) + (y * e) == f)):
        return "x = " + str(x) + " , y = " + str(y)

  return "There is no solution"

print(solve(a, b, c, d, e, f))