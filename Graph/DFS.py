
# coding: utf-8

# In[1]:


#!/usr/bin/python36

import os 
import subprocess as sp


# In[2]:


class Node:
    def __init__(self,vertex):
        self.vertex=vertex
        self.visited=False
        self.adjacencyList=[]
        self.predecessor=None
        
    


# In[8]:


class DFS:
    def dfs(self,startNode):
        startNode.visited=True
        print(startNode.vertex)
        for n in startNode.adjacencyList:
            self.dfs(n)


# In[9]:


node1=Node("a")


# In[10]:


node2=Node("b")


# In[11]:


node3=Node("c")


# In[12]:


node4=Node("d")
node5=Node("e")
node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node2.adjacencyList.append(node5)
dfs=DFS()
dfs.dfs(node1)

