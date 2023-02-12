# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
"""


"""
Implement your search algorithsm here
"""

import operator

def depthFirstSearch(problem):
  """
  Your search algorithm needs to return a list of actions that reaches the goal
  Strategy: Search the deepest nodes in the search tree first
  """
  "*** YOUR CODE HERE ***"
  print ("Start:", problem.getStartState())
  closed=[]
  x=0
  start=problem.getStartState()
  fringe=[[start,[],0]]
  while True:
      if len(fringe)==0:      
        print('No solution found')
        return []
      c_node=fringe.pop()
      p=c_node[1]
      act=c_node[2]
      closed.append(c_node[0])
      #x+=1
      if problem.isGoalState(c_node[0]):
          print("Solution found")
          print("no. of nodes traversed:",x)
          print('cost:',act)
          return c_node[1]    
      else:
          for state,action,cost in problem.getSuccessors(c_node[0]):
            if state not in closed:
              x+=1
              print(x)
              a=p+[action]
              act1=act+int(cost)
              c=[state,a,act1]
              fringe.append(c)
 

def breadthFirstSearch(problem):
  """
  Your search algorithm needs to return a list of actions that reaches the goal
  Strategy: Search the shallowest nodes in the search tree first.
  """
  "*** YOUR CODE HERE ***"
  print ("Start:", problem.getStartState())
  visited=[[False for i in range(20)]for i in range(16)]
  x=0
  start=problem.getStartState()
  fringe=[[start,[],0]]
  while True:
      if len(fringe)==0:      
        print('No solution found')
        return []
      c_node=fringe.pop(0)
      p=c_node[1]
      cos=c_node[2]
      #closed.append(c_node[0])
      visited[c_node[0][0]][c_node[0][1]]=True
      #x+=1
      if problem.isGoalState(c_node[0]):
          print("Solution found")
          print("no. of nodes traversed:",x)
          print('cost:',cos)
          return c_node[1]    
      else:
          for state,action,cost in problem.getSuccessors(c_node[0]):
            if visited[state[0]][state[1]]==False:
              x+=1
              print(visited)
              a=p+[action]
              cos1=cos+int(cost)
              c=[state,a,cos1]
              fringe.append(c)
  
def uniformCostSearch(problem):
  """
  Your search algorithm needs to return a list of actions that reaches the goal
  Strategy: Search the node of least total cost first.
  """
  "*** YOUR CODE HERE ***"
  