import sys

N = int(input())
C = int(input())
K = int(input())
P = int(input())

# read grid
grid = [[-1 for x in range(N)] for y in range(N)]
for r in range(N):
    for c in range(N):
        grid[r][c] = int(input())

i = 0
moves = 0
numMoves = 20
N2 = (N-1)*(N-1)
print('Test Case - 1\n\n\n')
print(N)
print(C)
print(K)
print(P)
print(grid)
# print(numMoves)
# while moves < numMoves:

#   num=(i*8009+104729)%N2
#   r=num//(N-1)
#   c=num%(N-1)
#   i+=1

#   if grid[r][c]==0: continue

#   if i%2==1 and grid[r][c+1]!=0:
#     print(r,c,r,c+1)
#     moves+=1
#   elif i%2==0 and grid[r+1][c]!=0:
#     print(r,c,r+1,c)
#     moves+=1

sys.stdout.flush()
