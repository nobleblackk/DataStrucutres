#!/usr/bin/python36

import os 
import subprocess as sp

class Node:
	def __init__(self,data):
		self.data=data
		self.leftChild=None
		self.rightChild=None

class BST:
	def __init__(self):
		self.root=None
	def insert(self,data):
		if not self.root:
			self.root=Node(data)
		else:
			self.insertNode(data,self.root)
	def insertNode(self,data,node):
		if data<node.data:
			if node.leftChild is None:
				node.leftChild=Node(data)
			else:
				self.insertNode(data,node.leftChild)
		else:
			if not node.rightChild:
				node.rightChild=Node(data)
			else:
				self.insertNode(data,node.rightChild)
	def getMin(self):
		if self.root:
			return self.getMinValue(self.root)
		else:
			print("tree is empty")
	def getMinValue(self,node):
		if node.leftChild:
			return self.getMinValue(node.leftChild)
		
		return node.data
	def getMax(self):
		if self.root:
			return self.getMaxValue(self.root)
		else:
			print("tree is empty")
	def getMaxValue(self,node):
		if node.rightChild:
			return self.getMaxValue(node.rightChild)
		
		return node.data
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
		return node
	def getPredecessor(self,node):
		if node.rightChild:
			return getPredecessor(node.rightChild)
		return node	
			
		

	

		
