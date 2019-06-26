#!/usr/bin/python36

import os
import subprocess as sp

class Node:
	def __init__(self,data):
		self.data=data;
		self.nextNode=None
		self.previousNode=None

class LinkedList:
	def __init__(self):
		self.size=0
		self.head=None
		self.tail=None
	def insertStart(self,data):
		self.size+=1;
		newNode=Node(data)
		if not self.head:
			self.head=newNode
			self.tail=newNode
		else:
			temp=self.head
			newNode.nextNode=self.head
			self.head=newNode
			temp.previousNode=newNode
		
	def insertEnd(self,data):
		self.size+=1
		newNode=Node(data)
		if self.tail is None:
			self.head=newNode
			self.tail=newNode
		else:
			temp=self.tail
			newNode.previousNode=self.tail
			self.tail=newNode
			temp.nextNode=newNode
	def traversel(self):
		actualNode=self.head
		print("Elements::")
		while actualNode is not None:
			print(actualNode.data)
			actualNode=actualNode.nextNode
	def length(self):	
		return self.size
	def length2(self):
		size=0
		actualNode=self.head
		while actualNode is not None:
			size+=1
			actualNode=actualNode.nextNode
		return size
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
			



	
