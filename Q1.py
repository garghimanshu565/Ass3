import math
initial=[[2,0,3],[1,8,4],[7,6,5]]   #initial state
goal=[[1,2,3],[8,0,4],[7,6,5]]   #goal state
list=[]
p=1   #put p=1 for manhatton distance
# p=2 #put p=2 for Euclidean distance
for i in range(3):
    for j in range(3):
        a=initial[i][j]
        for k in range(3):
            for l in range(3):
                if(goal[k][l]==a):
                    #finding distance
                    list.append(math.pow((math.pow(abs(i-k),p)+math.pow(abs(j-l),p)),1.0/p))  
                    break
sum=0
for i in range(len(list)):
    sum=sum+list[i]    #summing the values of all elements to find distance

print(sum)



