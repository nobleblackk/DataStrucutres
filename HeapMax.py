#!/usr/bin/python36
	
import os 
import subprocess as sp

class HeapMax:
	HeapSize=10
	def __init__(self):
		self.heap=[0]*(HeapMax.HeapSize)
		self.currentPosition=-1
	
	def insertion(self,data):
		if self.isFull():
			print("Heap is full")
			return
		print("now enter")
		self.currentPosition=self.currentPosition+1	
		self.heap[self.currentPosition]=data
		self.heapifyProcess(self.currentPosition)
		print("Elements::")
		for i in range(HeapMax.HeapSize):
			print(self.heap[i])
	#############
	def isFull(self):
		if self.currentPosition == (HeapMax.HeapSize)-1:
			return True
		else:
			print("not")
			print("position", self.currentPosition)
			return False
	#############
	def heapifyProcess(self,index):
		parentIndex=int((index-1)/2)
		while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
			temp=self.heap[parentIndex]
			self.heap[parentIndex]=self.heap[index]
			self.heap[index]=temp
			index=parentIndex
			parentIndex=int((index-1)/2)
	##############
	def heapSort(self):
		for i in range(0,self.currentPosition+1):
			temp=self.heap[0]
			print(temp)
			self.heap[0]=self.heap[self.currentPosition-i]
			self.heap[self.currentPosition-i]=temp
			self.fixDown(0,self.currentPosition-i-1)
	##############
	def fixDown(self,index,upto):
		while index < upto:
			leftChild=2*index+1
			rightChild=2*index+2
			if leftChild <= upto:
				childToSwap=None
				if rightChild > upto:
					childToSwap=leftChild
				else:
					if self.heap[leftChild] > self.heap[rightChild]:
						#print("left")
						#print(childToSwap)
						childToSwap=leftChild
						#print("now left")
						#print(childToSwap)
					else:
						childToSwap=rightChild
				if self.heap[index] < self.heap[childToSwap]:
					temp=self.heap[index]
					self.heap[index]=self.heap[childToSwap]
					self.heap[childToSwap]=temp
				else: 
					break
				index=childToSwap	
			else:
				break

						
			
	
		
	
