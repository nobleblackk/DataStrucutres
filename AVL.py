#!/usr/bin/python36

import os 
import subprocess as sp

class Node:
	def __init__(self,data):
		self.data=data
		self.height=0
		self.leftChild=None
		self.rightChild=None

class AVL:
	def __init__(self):
		self.root=None
	
	def getHeight(self,node):
		if not node:
			return -1;
		return node.height
	### if balance > 1 --> left heavy tree --> right rotation
	### if balance < 1 --> right heavy tree --> left rotation
	def getBalance(self,node):
		if not node:
			return 0;
		return self.getHeight(node.leftChild)-self.getHeight(node.rightChild)
	
	### rotating to the right on the node...
	def rotationRight(self,node):
		tempLeftChild=node.leftChild
		t=tempLeftChild.rightChild
		
		tempLeftChild.rightChild=node
		node.leftChild=t
		node.height=max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))+1
		tempLeftChild.height=max(self.getHeight(tempLeftChild.leftChild),self.getHeight(tempLeftChild.rightChild))+1
		return tempLeftChild;
	### rotating to the left on the node...
	def rotationLeft(self,node):
		tempRightChild=node.rightChild
		t=tempRightChild.leftChild
		tempRightChild.leftChild=node
		node.rightChild=t
		node.height=max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))+1
		tempRightChild.height=max(self.getHeight(tempRightChild.leftChild),self.getHeight(tempRightChild.rightChild))+1
		return tempRightChild
	def insert(self,data):
		self.root=self.insertNode(data,self.root)
	def insertNode(self,data,node):
		if not node:
			return Node(data)
		if data < node.data:
			node.leftChild=self.insertNode(data,node.leftChild)
		else:
			node.rightChild=self.insertNode(data,node.rightChild)
		node.height=max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))+1
		
		return self.settleViolation(data,node)
	def settleViolation(self,data,node):
		balance=self.getBalance(node)
		### case 1 --> left left heavy situation --> single right rotation
		if balance > 1 and data < node.leftChild.data:
			print("left left heavy situation...")
			return self.rotationRight(node)
		### case 2 --> right right heavy situation --> single left rotation
		if balance < -1 and data > node.rightChild.data:
			print("right right heavy situation")
			return self.rotationLeft(node)
		### case 3 --> left right heavy situation --> 
		### --> two rotations --> 1.left rotation 2.right rotation
		if balance > 1 and data > node.leftChild.data:
			print("left right heavy rotation")
			node.leftChild=self.rotationLeft(node.leftChild)
			return self.rotationRight(node)
		### case 4 --> right left heavy situation -->
		### --> two rotations --> 1.right rotation 2.left rotation
		if balance < -1 and data < node.rightChild.data:
			print("right left heavy rotation")
			node.rightChild=self.rotationRight(node.rightChild)
			return self.rotationLeft(node)
		return node   ### if it is the first node or the it is already balanced tree after insertion
	###traversal method
	def traversal(self):
		if self.root:
			print("""
			1.InOrder Traversal
			2.PreOrder Traversal
			3.PostOrder Traversal
			""")
			choice=int(input("Please enter your choice::"))
			if choice == 1:
				self.traversalInOrder(self.root)
			elif choice == 2:
				self.traversalPreOrder(self.root)
			elif choice == 3:
				self.traversalPostOrder(self.root)
			else: 
				print("Wrong choice")
	def traversalInOrder(self,node):
		if node.leftChild:
			self.traversalInOrder(node.leftChild)
		print(node.data)
		if node.rightChild:
			self.traversalInOrder(node.rightChild)
	def traversalPreOrder(self,node):
		print(node.data)
		if node.leftChild:
			self.traversalPreOrder(node.leftChild)
		if node.rightChild:
			self.traversalPreOrder(node.rightChild)
	def traversalPostOrder(self,node):
		if node.leftChild:
			self.traversalPostOrder(node.leftChild)
		if node.rightChild:
			self.traversalPostOrder(node.rightChild)
		print(node.data)
	def removal(self,data):
		if self.root:
			self.root=self.removalNode(data,self.root)
	def removalNode(self,data,node):
		#if not node:
		#	return node
		if data < node.data:
			node.leftChild=self.removalNode(data,node.leftChild)
		elif data > node.data:
			node.rightChild=self.removalNode(data,node.rightChild)
		else:
			if not node.leftChild and not node.rightChild:
				print("Lead node removing...")
				del node
				return None
			if not node.rightChild:
				print("Removing Node With Left Child...")
				tempNode=node.leftChild
				del node
				return tempNode
			elif not node.leftChild:
				print("Removing Node With Right Child...")
				tempNode=node.rightChild
				del node
				return tempNode
			print("Removing Node With Both Child...")
			tempNode=self.getPredecessor(node.leftChild)
			node.data=tempNode.data
			node.leftChild=self.removalNode(tempNode.data,node.leftChild)
		if not node: ####it means it is the only single nod present...so now None 
			return node
		node.height=max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))+1
		balance=self.getBalance(node)
		### case 1 --> doubly left case
		if balance > 1 and self.getBalance(node.leftChild) >= 0:
			return self.rotationRight(node)
		### case 3 --> left right situation --> 1.LR 2.RR
		if balance > 1 and self.getBalance(node.leftChild) < 0:
			node.leftChild=self.rotationLeft(node.leftChild)
			return self.rotationRight(node)
		### case 2 --> doubly right case
		if balance < -1 and self.getBalance(node.rightChild) <= 0:
			return self.rotationLeft(node)
		### case 4 --> right left situation --> 1.RR 2.LR
		if balance < -1 and self.getBalance(node.rightChild) > 0:
			node.rightChild=self.rotationRight(node.rightChild)
			return self.rotationLeft(node)
		return node ###it means it is already balanced tree ...no need to balance ...just return	
	def getPredecessor(self,node):
		if node.rightChild:
			return getPredecessor(node.rightChild)
		return node
		

			

		
	
