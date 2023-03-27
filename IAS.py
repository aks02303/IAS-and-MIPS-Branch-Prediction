opcode={"LOAD MQ":"00001010","STOR M(X)":"00100001","LOAD M(X)":"00000001","ADD M(X)":"00000101","SUB M(X)":"00000110","MUL M(X)":"00001011","DIV M(X)":"00001101", "JUMP M(X,0:19)":"00001101","JUMP M(X,20:39)":"00001110","LOAD MQ M(X)":"00001001"}
#Load MQ STOR M(X)  LOAD M(X) ADD M(X)
inst=[]      #This list is used to store all the instructions and then add it to memory                 #Above is the dictionary of opcode and operations
def ALU(opr,data,locasn):#This is the ALU Function is basically get three input operation to perform ,data to do operatioin and location for STOR to strore in memory
    global accumulator  #This is accumulator 
    global MQ   #This is MQ register
    if(opr=="LOAD"):#For the LOAD Operation
        accumulator=data
    elif(opr=="ADD"):#For add OPeration
        accumulator+=data
    elif(opr=="STOR"):#For store operation to store data in the specifiedd memory location
        memory[locasn]=accumulator
        print("This is the memory after operation :",memory)
    elif(opr=="LOADMQM(X)"):#This is the LOAD MQ M(X) operation 
        MQ=data
    elif(opr=="LOADMQ"):#This is for LOAD MQ operation
        accumulator=MQ
    elif(opr=="MUL"):#This is for MUL operation
        MQ*=data
    elif(opr=="DIV"):
        MQ=MQ/data
    elif(opr=="SUB"):
        accumulator-=data
f=0
print("This is the IAS Assembler")
print("First Input all the data that have to  be in the memory for operations\n")
print("Input format for data\n")
print("location data")
print("type start to input the instructions")
print("Input format of Instruction\n")
print("location LeftInstruction RightInstruction")
print("Type END to end the instruction input")
print("Type NOF if no right instruction")
count_data=0#No use of this variable
locations=[]#Location 
operation=[]#No used of this list
#This  is the Assembler part of the program here instructions are stored in the memory

#Example of input format
# 0 12
# 1 12
# start
# 2 LOAD M(0) ADD M(1)
# 3 STOR M(4) NOF

#For STOR M(X) here in place of X we need to input the value the memory location in which you want store the computed result

# This is the inputs
# 0 10
# 1 9
# 2 8
# 3 7
# 4 6
# 5 5
# 6 4
# 7 3
# 8 2
# 9 1
# 30 11
# 31 12
# 32 13
# 33 14
# 34 15
# 35 16
# 36 17
# 37 18
# 38 19
# start
# 10 LOAD MQ,M(0) MUL M(1)
# 11 MUL M(2) MUL M(3)
# 12 MUL M(4) MUL M(5)
# 13 MUL M(6) MUL M(7)
# 14 MUL M(8) MUL M(9)
# 11 MUL M(31) MUL M(32)
# 12 MUL M(33) MUL M(34)
# 13 MUL M(35) MUL M(36)
# 14 MUL M(37) MUL M(38)
# 15 LOAD MQ STOR M(41)
# 16 LOAD M(0) ADD M(1)
# 17 ADD M(2) ADD M(3)
# 18 ADD M(4) ADD M(5)
# 19 ADD M(6) ADD M(7)
# 20 ADD M(8) ADD M(9)
# 21 ADD M(31) ADD M(32)
# 22 ADD M(33 ADD M(34)
# 23 ADD M(35) ADD M(36)
# 23 ADD M(37) ADD M(38)
# 24 STOR M(40) NOF
# END
  
  
  
  
  
while(True):
    count_data+=1#Not used in the program
    w=""
    if(f==1):
        break
    instructions=input().split()
    if(instructions[0]=="start"):
        while(True):
            w=""
            instructions=input().split()
            if(instructions[0]!="start" and instructions[0]!="END"):
                operation.append(instructions[1])
                if(instructions[3]!="NOF"):
                    operation.append(instructions[3])
            if(instructions[0]=="END"):
                f=1
                break
            if(instructions[1]+instructions[2]=='LOADMQ'):
                w=w+opcode["LOAD MQ"]
                w=w+"0"*12
            if(instructions[1]+instructions[2][0:2]=='ADDM('):
                w=w+opcode["ADD M(X)"]
            if(instructions[1]+instructions[2][0:2]=='LOADM('):
                w=w+opcode["LOAD M(X)"]
            if(instructions[1]+instructions[2][0:2]=='STORM('):
                w=w+opcode["STOR M(X)"]
            if(instructions[1]+instructions[2][0:2]=='DIVM('):
                w=w+opcode["DIV M(X)"]
            if(instructions[1]+instructions[2][0:2]=='MULM('):
                w=w+opcode["MUL M(X)"]
            if(instructions[1]+instructions[2][0:5]=="LOADMQ,M("):
                w=w+opcode["LOAD MQ M(X)"]
            if(instructions[1]+instructions[2][0:2]=='SUBM('):
                w=w+opcode["SUB M(X)"]
            if(instructions[1]+instructions[2][0:2]+instructions[2][-6:]=='JUMPM(,0:19)'):
                w=w+opcode["JUMP M(X,0:19)"]
            if(instructions[1]+instructions[2][0:2]+instructions[2][-7:]=='JUMPM(,20:39)'):
                w=w+opcode["JUMP M(X,20:39)"]
            if(instructions[2][0:2]=='M(' and instructions[1]!='JUMP'):
                x=int(instructions[2][2:-1])
                s=str(bin(x))
                y="0"
                s=s[2:]
                y=y*(12-len(s))
                w=w+y+s
                # print(w)
            if(instructions[2][0:5]=="MQ,M("):
                x=int(instructions[2][5:-1])
                s=str(bin(x))
                y="0"
                s=s[2:]
                y=y*(12-len(s))
                w=w+y+s
            if(instructions[2][0:2]=='M(' and instructions[1]=='JUMP' and instructions[2][-3:-1]=="19"):
                x=int(instructions[2][2:-6])
                s=str(bin(x))
                y="0"
                s=s[2:]
                y=y*(12-len(s))
                w=w+y+s
                # print(w)
            if(instructions[2][0:2]=='M(' and instructions[1]=='JUMP' and instructions[2][-3:-1]=="39"):
                x=int(instructions[2][2:-7])
                s=str(bin(x))
                y="0"
                s=s[2:]
                y=y*(12-len(s))
                w=w+y+s
                # print(w)
            if(instructions[3]!="NOF"):
                if(instructions[3]+instructions[4]=='LOADMQ'):
                    w=w+opcode["LOAD MQ"]
                    w=w+"0"*12
                if(instructions[3]+instructions[4][0:2]=='ADDM('):
                    w=w+opcode["ADD M(X)"]
                if(instructions[3]+instructions[4][0:2]=='LOADM('):
                    w=w+opcode["LOAD M(X)"]
                if(instructions[3]+instructions[4][0:2]=='STORM('):
                    w=w+opcode["STOR M(X)"]
                if(instructions[3]+instructions[4][0:2]=='DIVM('):
                    w=w+opcode["DIV M(X)"]
                if(instructions[3]+instructions[4][0:2]=='MULM('):
                    w=w+opcode["MUL M(X)"]
                if(instructions[3]+instructions[4][0:2]=='SUBM('):
                    w=w+opcode["SUB M(X)"]
                if(instructions[3]+instructions[4][0:2]+instructions[2][-6:]=='JUMPM(,0:19)'):
                    w=w+opcode["JUMP M(X,0:19)"]
                if(instructions[3]+instructions[4][0:2]+instructions[2][-7:]=='JUMPM(,20:39)'):
                    w=w+opcode["JUMP M(X,20:39)"]
                if(instructions[3]+instructions[4][0:5]=="LOADMQ,M("):
                    w=w+opcode["LOAD MQ M(X)"]
                if(instructions[4][0:5]=="MQ,M("):
                    x=int(instructions[4][5:-1])
                    s=str(bin(x))
                    y="0"
                    s=s[2:]
                    y=y*(12-len(s))
                    w=w+y+s
                if(instructions[4][0:2]=='M(' and instructions[3]!='JUMP'):
                    x=int(instructions[4][2:-1])
                    s=str(bin(x))
                    y="0"
                    s=s[2:]
                    y=y*(12-len(s))
                    w=w+y+s
                    # print(w)
                if(instructions[4][0:2]=='M(' and instructions[3]=='JUMP' and instructions[4][-3:-1]=="19"):
                    x=int(instructions[4][2:-6])
                    s=str(bin(x))
                    y="0"
                    s=s[2:]
                    y=y*(12-len(s))
                    w=w+y+s
                    # print(w)
                if(instructions[4][0:2]=='M(' and instructions[3]=='JUMP' and instructions[4][-3:-1]=="39"):
                    x=int(instructions[4][2:-7])
                    s=str(bin(x))
                    y="0"
                    s=s[2:]
                    y=y*(12-len(s))
                    w=w+y+s
            if(instructions[3]=="NOF"):
                w="0"*20+w
            inst.append(w)
            locations.append(int(instructions[0]))
            # print(inst)
        
    else:
        if(instructions[0]!="END" and instructions[0]!="start"):
            inst.append(int(instructions[1]))
            locations.append(int(instructions[0]))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#THIS IS THE PROCESSOR BLOCK
#---------------------------------------------------------------------------------------------------------------------------------------------------------



memory=[0]*1000
print("You have Given Input all the data and Instructions. All the data and Instruction is stored in the memory at your specified Location")
for i in range(len(locations)):
    memory[locations[i]]=inst[i]
print("This is the memory after the input of instructions :", memory)
IBR=""
IR=""
MBR=""
pc=0
cn=0
while(1):
    if(pc==len(inst)):#If pc is equal to the length of instructions
        break
    else:
        MAR=locations[pc]
        if(type(memory[MAR])==int):
            pass
        else:
            MBR=memory[MAR]#This is the fetching  part here wew segregate the MBR into IR , MAR and IBR
            IR=MBR[0:8]
            MAR=MBR[8:20]
            IBR=MBR[20:40]
            i=0
            while(i<2):
                s=[]
                if(i==1):
                    IR=IBR[0:8]#This is the fetching part of Right hand Instruction and segregating IBR into IR, MAR
                    MAR=IBR[8:20]
                for a,b in opcode.items():
                    if(b==IR):
                        s=a.split()#this is the decoding part in which IR is compared to the dictionary and if equal then store in s list 
                                    # We use first element of the list to compare and do respective functoins accordingly
                if(len(s)!=0):
                    if(s[0]=="LOAD" and s[1]=='M(X)'):
                        x=int(MAR,2)
                        y=memory[x]
                        ALU("LOAD",y,0)
                    elif(s[0]=="ADD"):
                        x=memory[int(MAR,2)]
                        ALU("ADD",x,0)
                    elif(s[0]=="SUB"):
                        x=memory[int(MAR,2)]
                        ALU("SUB",x,1)
                    elif(s[0]=="MUL"):
                        x=int(memory[int(MAR,2)])
                        ALU("MUL",x,1)
                    elif(s[0]=="STOR"):
                        x=int(MAR,2)
                        ALU("STOR",1,x)
                    elif(IR=="00001010"):#This is the opcode of  the LOAD MQ operation
                        ALU("LOADMQ",1,1)
                    elif(IR=="00001001"):#This is the opcode for LOAD MQ M(X)
                        x=int(MAR,2)
                        y=memory[x]
                        ALU("LOADMQM(X)",y,1)
                i+=1
    pc+=1
                
                        
            


    

        
    
