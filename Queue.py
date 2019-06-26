#!/usr/bin/python36
	
import os 
impost subprocess as sp

class Queue:
	def __init__(self):
		self.queue=[]
	def enqueue(self,data):
		self.queue.append(data)
	def dequeue(self):
		data=self.queue[0]
		del self.queue[0]
		return data
	def peek(self):
		data=self.queue[0]
		return data
