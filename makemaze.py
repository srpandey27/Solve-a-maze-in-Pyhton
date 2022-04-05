
from random import shuffle

def shuffled(x):
    y = list(x)
    shuffle(y)
    return y

DIRECTIONS = (
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
)

def makeMaze(width, height, cellsize):
    cellsize1 = cellsize+1 # cellsize including one wall
    field_width = width*cellsize1+1
    field_height = height*cellsize1+1
    field = [0]*(field_width*field_height)
    stack = [(0, 0, shuffled(DIRECTIONS))]
    while stack:
        x, y, directions = stack[-1]
        dx, dy = directions.pop()
        # no other ways to go from here
        if not directions:
            stack.pop()
        # new cell
        nx = x+dx
        ny = y+dy
        # out of bounds
        if not (0 <= nx < width and 0 <= ny < height):
            continue
        # index of new cell in field
        fx = 1+nx*cellsize1
        fy = 1+ny*cellsize1
        fi = fx+fy*field_width
        # already visited
        if field[fi]:
            continue
        # tear down walls
        if dx > 0:
            a = -1
            b = field_width
        elif dx < 0:
            a = cellsize
            b = field_width
        elif dy > 0:
            a = -field_width
            b = 1
        else:
            a = cellsize*field_width
            b = 1
        for offset in range(cellsize):
            field[fi+a+b*offset] = 1
        # clear cell
        for y in range(0, cellsize):
            for x in range(0, cellsize):
                field[fi+x+y*field_width] = 1
        # visit cell
        stack.append([nx, ny, shuffled(DIRECTIONS)])
    return field

def createMaze(width,height,cellsize):
  fields = makeMaze(width, height, cellsize)
  cellsize1=cellsize+1
  w=width*cellsize1+1
  h=height*cellsize1+1
  maze=[]
  for i in range(h):
    row=[]
    for j in range(w):
      if fields[i*w+j]==0:
        row.append("#")
      else:
        row.append(" ")
    maze.append(row)
  maze[1][1]="S"
  maze[h-2][w-2]="E"
  return(maze)
