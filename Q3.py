import sys
import copy
curr_min = sys.maxsize
q=[]
visited=[]
 
def find_pos(s):
  for i in range(len(s)):
    for j in range(len(s[0])):
          if s[i][j]==0:
            return([i,j])

def up(s,pos):
  i=pos[0]
  j=pos[1]
  if i>0:
    temp=copy.deepcopy(s)
    temp[i][j]=temp[i-1][j]
    temp[i-1][j]=0
    return(temp)
  else:
    return(s)

def down(s,pos):
   i=pos[0]
   j=pos[1]
   if i<2:
    temp=copy.deepcopy(s)
    temp[i][j]=temp[i+1][j]
    temp[i+1][j]=0
    return(temp)
   else:
     return(s)

def left(s,pos):
   i=pos[0]
   j=pos[1]
   if j>0:
    temp=copy.deepcopy(s)
    temp[i][j]=temp[i][j-1]
    temp[i][j-1]=0
    return(temp)
   else:
     return(s)

def right(s,pos):
   i=pos[0]
   j=pos[1]
   if j<2:
    temp=copy.deepcopy(s)
    temp[i][j]=temp[i][j+1]
    temp[i][j+1]=0
    return(temp)
   else:
     return(s)     

def enqueue(s):
  global q
  q=q+[s]

def heuristic(s,g):
  d=0
  for i in range(len(s)):
    for j in range(len(s[0])):
      if s[i][j]!=g[i][j]:
        d+=1
  return d      

def dequeue(g):
  h=[]
  global q
  global visited 
  global curr_min
  for i in range(len(q)):
    h=h+[heuristic(q[i],g)]
  if min(h) < curr_min:
    curr_min=min(h)
    index=h.index(min(h))
    visited=visited+[q[index]]
    elem = q[index]
    q.clear()
    return elem  
  else:
    print("Optimal solution found and intermediate states are ")
    print(visited)
    return 1000
  
  

def search(s,g):
  curr_state = copy.deepcopy(s)
  if s==g:
    return
  global visited
  while(1):
    pos=find_pos(curr_state)
    new=up(curr_state,pos)
    if new!=curr_state:
      if new==g:
        print("Goal state found and intermediate states are ")
        print(visited+[g])
        return
      else:
        if(new not in visited):
          enqueue(new)
    new=down(curr_state,pos)
    if new!=curr_state:
      if new==g:
        print("Goal state found and intermediate states are ")
        print(visited+[g])
        return
      else:
        if(new not in visited):
          enqueue(new)          
    new=right(curr_state,pos)
    if new!=curr_state:
      if new==g:
        print("Goal state found and intermediate states are ")
        print(visited+[g])
        return
      else:
        if(new not in visited):
          enqueue(new)
    new=left(curr_state,pos)
    if new!=curr_state:
      if new==g:
        print("Goal state found and intermediate states are ")
        print(visited+[g])
        return
      else:
        if(new not in visited):
          enqueue(new)
    if len(q)>0:
      current_state=dequeue(g)
      if(current_state==1000):
        break
    else:
      print("Not found")
      return

def main():
  s=[[2,0,3],[1,8,4],[7,6,5]]
  g=[[1,2,3],[8,0,4],[7,6,5]]
  global q
  global visited
  q=q+[s]
  visited=visited+[s]
  search(s,g)

if __name__=="__main__":
  main()