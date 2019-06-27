
# coding: utf-8

# In[10]:


#!/usr/bin/python36

import os
import subprocess as sp


# In[11]:


class Node:
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjacencyList=[]
        self.visited=False
        self.predecessor=None
        


# In[14]:


class BFS:
    def bfs(self,startNode):
        queue=[]
        queue.append(startNode)
        startNode.visited=True
        while queue:
            actualNode=queue.pop(0)
            print(actualNode.vertex)
            for n in actualNode.adjacencyList:
                queue.append(n)
                n.visited=True


# In[15]:


node1=Node("a")
node2=Node("b")
node3=Node("c")
node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)

bfs=BFS()
bfs.bfs(node1)


