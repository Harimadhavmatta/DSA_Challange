d='DULR'
x=[1,-1,0,0]
y=[0,0,-1,1]
def isvalid(x,y,maze,n):
    if x>=0 and y>=0 and x<n and y<n and maze[x][y]==1:
        return True
    return False
def solve(curr_x,curr_y,maze,n,result,current):
    if(curr_x==n-1 and curr_y==n-1):
        result.append(current)
        return
    
    maze[curr_x][curr_y]=0
    for i in range(4):
        next_x=curr_x+x[i]
        next_y=curr_y+y[i]
        if isvalid(next_x,next_y,maze,n):
            current=current+d[i]
            solve(next_x,next_y,maze,n,result,current)
            current=current[:-1]
    maze[curr_x][curr_y]=1
            
        
maze=[
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
n=len(maze)
result=[]
current=''
if maze[0][0]==1 and maze[n-1][n-1]==1:
    solve(0,0,maze,n,result,current)
if not result:
    print(-1)
else:
    print(" ".join(result))