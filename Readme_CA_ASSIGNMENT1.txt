============IAS IMPLEMENTATION IN PYTHON LANGUAGUE ============
************COMPUTER ARCHITECTURE ASSIGNMENT 1*****************
************AKSHAY PANDEY (IMT2021074)*************************

In the following assignment we aim to emulate the various ISA instuction set, and process using IAS computer.

The registers involved in IAS computer are:
AC  : Accumulator
	Accumulate/hold results of an ALU operation

IR  : Instructions Register
	8 bit opcode of the instruction to be executed
	
IBR : Instructions Buffer register
	Holds the RHS instruction temporarily

MQ  : Multiplier/Quotioent Register

MBR : Memory BUffer register
	Contains a word to be read/stored in memory or I/O

MAR : Memory Adress register
	Specifies the address in memory of the word to be written/read into MBR

PC  : Program Counter
	Holds the next instruction’s address			

************************************DESCRIPTION************************************************************

This program is to implement IAS using python program my program contains Additon, Multiplication and Divisoin
of any number of numbers.

1. First Part of program is Assembler which convert assembly language into 40 bits binary instructions 
2. In assembler First you have to input all the data on which operations has to be perform.
3. Format for inputing the data is first ("memory location" space "data")
eg. 0 10 
4. Type "start" to start input the instructions
5. Input format of instruction ("memory location"space"Left Instruction"space"Right Instruction")
e.g 1 LOAD M(0) ADD M(1) Here M(0) '0' is the memory location of 10 and ADD M(1) '1' is the location
of another data to be added.
6. If there is no right instruction the type "NOF" after left
e.g 2 STOR M(3) NOF Here for stor m(3) '3'is the memory location at which it is stored the computed result
7. For LOAD MQ M(X) instruction format type is LOAD MQ,M(X) here X is the memory location


************************************EXPLANATION************************************************************

I made assembler which convert assembly language into binary code machine language then I store all the intruction and data to 
memory which has 1000 locations.Then I made a Fetching Part where the 40 bit data from the memory is fetched to the MBR and segregated
into different registers like IR MAR IBR accordingly.Then there is the Decoding part there I iterate a loop where I'd checked for IR == in value
of opcode dictionary.then there is if else condition from there it transfer data to the ALU and there is acumulator variable and MQ variable
for their designated task.

***********************************FUNCTOINS PERFORMED*****************************************************
1.Multiplication of numbers 
2.Addition of two numbers
3.2.Division of numbers
4.Subrtration of two numbers
All the above function can be used only for positive numbers.
Sample Input output is of only of multipilcation and Addition but in my program we can do even subtraction and Division

**********************************SAMPLE INPUT**************************************************************

0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
9 1
30 11
31 12
32 13
33 14
34 15
35 16
36 17
37 18
38 19
start
10 LOAD MQ,M(0) MUL M(1)
11 MUL M(2) MUL M(3)
12 MUL M(4) MUL M(5)
13 MUL M(6) MUL M(7)
14 MUL M(8) MUL M(9)
11 MUL M(31) MUL M(32)
12 MUL M(33) MUL M(34)
13 MUL M(35) MUL M(36)
14 MUL M(37) MUL M(38)
15 LOAD MQ STOR M(41)
16 LOAD M(0) ADD M(1)
17 ADD M(2) ADD M(3)
18 ADD M(4) ADD M(5)
19 ADD M(6) ADD M(7)
20 ADD M(8) ADD M(9)
21 ADD M(31) ADD M(32)
22 ADD M(33 ADD M(34)
23 ADD M(35) ADD M(36)
23 ADD M(37) ADD M(38)
24 STOR M(40) NOF
END