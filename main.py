''' The goal of this program is to use recursion to solve a maze'''

from makemaze import createMaze
import random


def getDirs(maze,r,c):
  #the function determines our next 
  dirs=[]
  R = '\033[31m' # red
  X = '\033[0m'
  ''' checking whether we have reached a dead end or not with the help of a list called run_through'''
  run_through=[" ","*","E","S",R +"*"+X]  
  if (maze[r-1][c] in run_through)==True:
    dirs.append("U")   
  if (maze[r+1][c] in run_through)==True:
    dirs.append("D")
  if (maze[r][c-1] in run_through)==True:
    dirs.append("L")
  if (maze[r][c+1] in run_through)==True:
    dirs.append("R")
  #the if conditions tested whether we had reached a dead end and then accordingly added the direction to the list named dirs
  return dirs


def goDir(dir,r,c):
  "given U, R. D, L, this function returns the coordinates for that cell"
  if dir=="U":
    return r-1,c
  elif dir=="R":
    return r,c+1
  elif dir=="D":
    return r+1,c
  elif dir=="L":
    return r,c-1
  else:
    print("goDir error:",dir)
  return r,c

def printMaze(maze):
  "Print out a maze"
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      print(maze[i][j],end="")
    print()

def isOpen(maze,r,c):
  "return true if r,c is open (space)"
  if maze[r][c]==" ":
    return True
  return False

def isEnd(maze,r,c):
  "return true if r,c is the end (E)"
  if maze[r][c]=="E":
    return True
  return False 

def DFS(maze,r,c):
  R = '\033[31m' # red
  X = '\033[0m' # reset 
  if maze[r][c]== "E": #checks if the maze is solved
    print("Congratulations on your triumph!")
    return True
  if maze[r][c]!= "#": #if we have not hit a wall, then mark the space as a dot and follow the instructions below.
    maze[r][c]="." #marks the position
    dirs = getDirs(maze, r, c)
  for count in dirs: 
    newr,newc=goDir(count, r,c) 
    if DFS(maze, newr, newc):
        list.append([newr,newc])  #adds the right pathways to take to a list which we later loop through and print the maze
        return True
  return False

list=[]
R = '\033[31m' # red
X = '\033[0m' # reset 
maze=createMaze(6,6,1)
printMaze(maze)
DFS(maze,1,1)
for counter in list:
  maze[counter[0]][counter[1]]=R+"."+X   #marks the position we are following as "."
maze[1][1]=R+"."+X
printMaze(maze)  #prints the final solution