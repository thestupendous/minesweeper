m,n  = 5,5              # m,n are dimensions of the board
p = 2                   # p is the number of mines to be placed


def printm(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], ' ',end='')
        print()

play_board= []
for i in range(m):
    b = [ 0 for x in range(n) ]
    play_board.append(b)

#setting mines
mines = []
for i in range(p):
    x,y = map(int,input().split())
    mines.append((x,y))

print(mines)
printm(play_board)

#------------updating-play_board-for-every-move-----------

def move(x,y,play_board,proxi_mat,mines):  #returns touple (over,won)
    m,n = len(proxi_mat), len(proxi_mat[0])
    p = len(mines)
    if proxi_mat[x][y] > 0:
        play_board[x][y]=proxi_mat[x][y]
        return (False,False)
    if proxi_mat[x][y] == 0:
        #do bfs untill keep hitting 0's
        visited=[]
        queue=[(x,y)]
        while len(queue) != 0:


        



#------------create-the-proximity-matrix-------------------

proxi_mat = []
#initialise proximity matrix with zeroes
for i in range(m):
    b = [ 0 for x in range(n) ]
    proxi_mat.append(b)

#setting mines location with -1
for mine in mines:
    x,y = mine[0],mine[1]
    proxi_mat[x][y] = -1

#printm(proxi_mat)

#checking if coordinate exists in board
def ex(x,y,m,n):
    if x<0 or y<0 :
        return False
    if x>=m or y>=n :
        return False
    return True

#function to actually set up the proximity matrix
def process_mines(proxi_mat,mines):
    for mine in mines:
        #print(mine[0],mine[1])
        m,n = len(proxi_mat),len(proxi_mat[0])
        x,y = int(mine[0]),int(mine[1])
#        print('for mine ',mine,x,y)
#        print(type(mine),type(x),type(y))
        if ex(x-1,y-1,m,n) and proxi_mat[x-1][y-1]!=-1 :
            proxi_mat[x-1][y-1]+=1

        if ex(x-1,y,m,n) and proxi_mat[x-1][y] != -1:
            proxi_mat[x-1][y]+=1

        if ex(x-1,y+1,m,n) and proxi_mat[x-1][y+1] != -1:
            proxi_mat[x-1][y+1]+=1

        if ex(x,y-1,m,n) and proxi_mat[x][y-1] != -1:
            proxi_mat[x][y-1]+=1

        if ex(x,y+1,m,n) and proxi_mat[x][y+1] != -1:
            proxi_mat[x][y+1]+=1

        if ex(x+1,y-1,m,n) and proxi_mat[x+1][y-1] != -1:
            proxi_mat[x+1][y-1]+=1

        if ex(x+1,y,m,n) and proxi_mat[x+1][y] != -1:
            proxi_mat[x+1][y]+=1

        if ex(x+1,y+1,m,n) and proxi_mat[x+1][y+1] != -1:
            proxi_mat[x+1][y+1]+=1

process_mines(proxi_mat,mines)
#printm(proxi_mat)


#------------------------------------------------------------------------

over=False
won=False
while not over:
    x,y = map(int,input().split())
    if (x,y) in mines:  #case when user is stepped on a mine
        break
    over,won=move(x,y,play_board,proxi_mat,mines)
    if over:
        break
        
if !won :
    print("game over!!  Try Again")

