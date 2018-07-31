
# coding: utf-8

# In[6]:


#missionaries and cannibles

move=[0,0,'L','R']   #boat moves from move[-2] to move[-1]
user=[0,0]              #input the no of cannibles and missonaries
leftb=['0'] #left bank
rightb=['m','m','m','c','c','c','0'] #right bank
temp=0
flag=0
while ((leftb.count('m')+leftb.count('c'))!=6):
    if (temp%2==0):
        
        print("move from left to right")
        user[0],user[1]=input().split()
        if (user[0] in leftb) and (user[1] in leftb):
            if user[0]!='0':      #if 0 then dont remove
                    rightb.append(user[0])
                    leftb.remove(user[0])

            if user[1]!='0':      #if 0 then dont remove
                    rightb.append(user[1])
                    leftb.remove(user[1])
        else:
            print("wrong move")
            flag=1
            break

        #check if cannibles are not more than missionaries
    
        if leftb.count('m')>1:
            if leftb.count('c')>leftb.count('m'):
                print("wrong move as missionaries were killed")
                flag=1
                break

                        
    else:
    
        print("move from right to left")
        user[0],user[1]=input().split()
        if (user[0] in rightb) and (user[1] in rightb):
            if user[0]!='0':      #if 0 then dont remove
                    leftb.append(user[0])
                    rightb.remove(user[0])

            if user[1]!='0':      #if 0 then dont remove
                    leftb.append(user[1])
                    rightb.remove(user[1])

        else:
            print("wrong move")
            flag=1
            break

        #check if cannibles are not more than missionaries
        if rightb.count('m')>1:
            if rightb.count('c')>rightb.count('m'):
                print("wrong move as missionaries were killed")
                flag=1
                break

    temp=temp+1

#remove all entries of 0
#leftb=[leftb.remove('0') for i in leftb if i=='0']
if flag==1:
    print("mission not accomplished")
else:
    print("mission accomplished ",leftb)
        
   

