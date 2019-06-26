#!/usr/bin/python36

import math
import keyword
import os
import subprocess as sp

end=-1
p=[0 for i in range(3)]
length=2

def Resize():
	global end
	global length
	global p
	p1=[0 for i in range((2*length)+1)]
	length=length*2
	print("New Length: ",length)
	for temp in range(end+1):
		 p1[temp]=p[temp]
	p=p1
	input("Enter to continue")
	#os.system("clear")

def Add(n1):
	global end
	global length
	global p
	if((end+1)==length):
		Resize()
	p[end+1]=n1
	end=end+1
	for i in range(length):
		print(p[i],end=" ")
	print("\nValue of End: ",end)
	print("Value of Length: ",length)
	#os.system("clear")
	input("Enter to continue")

def Insert(n1,n2):
	global end
	global length
	global p
	#print("n1:",n1)
	#print("n2:",n2)
	if((end+1)==length):
		Resize()
	for i in range((length-1),(n1-1),-1):
		p[i]=p[i-1]
	p[n1]=n2
	end=end+1
	for i in range(length):
		print(p[i],end=" ")
	print("\nValue of End: ",end)
	print("\nValue of Length: ",length)
	#os.system("clear")
	input("Enter to continue")

def Delete(n1):
	global end
	global length
	global p
	for i in range(n1,(length-1),1):
		p[i]=p[i+1]
	p[end]=0
	length=length-1
	end=end-1
	for i in range(length):
		print(p[i],end="")
	print("\nValue of End: ",end)
	print("Value of Length: ",length)
	#os.system("clear")
	input("Enter to continue")

while True:
	print("""
	LIST IMPLEMENTATION:::
	1.Add element
	2.Insert element
	3.Delete element
	4.Resize array
	5.To Exit
	""")
	choice=int(input("enter value"))
 
	if choice==1:
		
		n1=int(input("enter element"))
		Add(n1)
		os.system("clear")

			
	elif choice==2:
		n2=int(input("enter index no"))
		n3=int(input("enter element"))
		Insert(n2,n3)
		os.system("clear")
			
	elif choice==3:
		n4=int(input("enter index to be deleted"))
		Delete(n4)
		os.system("clear")

	elif choice==4:
		Resize()
		os.system("clear")
				
	elif choice==5:
		exit()
	
	#input("Enter to continue...")
	#sp.getoutput("clear")	

	
	











