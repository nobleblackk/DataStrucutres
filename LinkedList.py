#!/usr/bin/python36

import os 
import subprocess as sp

class Node:
	def __init__(self,data):
		self.data=data
		self.nextNode=None

class LinkedList:
	def __init__(self):
		self.head=None
		self.size=0
		#print(self.size)
	
	def insertStart(self,data):
		self.size+=1
		#print(self.size)
		newNode=Node(data)		
		
		if not self.head:
			self.head=newNode
		#	print("first")
		else:
			newNode.nextNode=self.head
			self.head=newNode
		#	print("not first")	
	def length(self):
		return self.size
	def length2(self):
		size=0
		actualNode=self.head
		while actualNode is not None:
			size+=1
			actualNode=actualNode.nextNode
		return size	
	def insertEnd(self,data):
		self.size+=1
		newNode=Node(data)
		actualNode=self.head
		#print("starting")	
		while actualNode.nextNode is not None:
			#print("1")
			actualNode=actualNode.nextNode
		actualNode.nextNode=newNode
	def traversel(self):
		actualNode=self.head
		print("Elements::",end='\n')
		while actualNode is not None:
			print(actualNode.data)
			actualNode=actualNode.nextNode
	def removel(self,data):
		currentNode=self.head
		previousNode=None
		while currentNode.data != data:
			previousNode=currentNode
			currentNode=currentNode.nextNode
		if previousNode is None:
			self.head=currentNode.nextNode
		else:
			previousNode.nextNode=currentNode.nextNode
		














	







