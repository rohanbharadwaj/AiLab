# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
from duplicity.path import Path
from __builtin__ import str

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  from game import Directions
  from util import Stack
  n=Directions.NORTH
  s=Directions.SOUTH
  e=Directions.EAST
  w=Directions.WEST
  explored=[]
  frontier=Stack()
  frontierSet=[]
  start_node=problem.getStartState()
  if problem.isGoalState(start_node)==True:
    return []
  frontier.push((start_node,[]))
  while frontier.isEmpty()==False:
      visit_node=frontier.pop()
      coord=visit_node[0]
      actions=visit_node[1]
      if(problem.isGoalState(coord)==True):
          print actions
          return actions
      explored.extend(coord)
      successors=problem.getSuccessors(coord)
      for successor in successors:
          succCoord=successor[0]
          succAction=successor[1]
          if succCoord not in explored and succCoord not in frontierSet:
              frontierSet.append(succCoord)
              tempPath=list(actions)
              if(succAction=='North'):
                tempPath.append(n)
              elif(succAction=='East'):
                tempPath.append(e)
              elif(succAction=='South'):
                tempPath.append(s)
              elif(succAction=='West'):
                tempPath.append(w)
              frontier.push((succCoord,tempPath))
  return []            

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  from game import Directions
  from util import Queue
  n=Directions.NORTH
  s=Directions.SOUTH
  e=Directions.EAST
  w=Directions.WEST
  explored=[]
  frontier=Queue()
  frontierSet=[]
  start_node=problem.getStartState()
  if problem.isGoalState(start_node)==True:
    return []
  frontier.push((start_node,[]))
  while frontier.isEmpty()==False:
      visit_node=frontier.pop()
      coord=visit_node[0]
      actions=visit_node[1]
      if(problem.isGoalState(coord)==True):
          print actions
          return actions
      explored.extend(str(coord))
      successors=problem.getSuccessors(coord)
      for successor in successors:
          succCoord=successor[0]
          succAction=successor[1]
          if succCoord not in explored and succCoord not in frontierSet:
              frontierSet.append(str(succCoord))
              tempPath=list(actions)
              if(succAction=='North'):
                tempPath.append(n)
              elif(succAction=='East'):
                tempPath.append(e)
              elif(succAction=='South'):
                tempPath.append(s)
              elif(succAction=='West'):
                tempPath.append(w)
              frontier.push((succCoord,tempPath))
  return []            
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  from game import Directions   
  from util import PriorityQueue
  n=Directions.NORTH
  s=Directions.SOUTH
  e=Directions.EAST
  w=Directions.WEST
  explored=[]
  frontier=PriorityQueue()
  frontierSet={}
  dist=0 # dist = g(n)
  start_node=problem.getStartState()
  if problem.isGoalState(start_node)==True:
    return []
  frontier.push((start_node,[],dist),dist)
  while frontier.isEmpty()==False:
      visit_node=frontier.pop()
      parentCoord=visit_node[0] # The node to be explored
      parentAction=visit_node[1] # Action required to reach to this node.
      parentDistance=visit_node[2] # Distance to this node 
      if(parentCoord in explored):
          continue
      if(problem.isGoalState(parentCoord)==True):
          print parentAction
          return parentAction
      explored.append(str(parentCoord))
      successors=problem.getSuccessors(parentCoord)
      for successor in successors:
          succCoord=successor[0]
          succAction=successor[1]
          succDistance=parentDistance+1
          tempPath=list(parentAction)
          if(succAction=='North'):
            tempPath.append(n)
          elif(succAction=='East'):
            tempPath.append(e)
          elif(succAction=='South'):
            tempPath.append(s)
          elif(succAction=='West'):
            tempPath.append(w)    
          if str(succCoord) in explored:
              continue
          dictkey = str(succCoord)
          #print dictkey

          # dictkey=','.join([succCoord[0],succCoord[1]])                
          if dictkey in frontierSet:
              oldDistance = frontierSet[dictkey]
              if succDistance > oldDistance:
                  succDistance=oldDistance
          frontierSet[dictkey]=succDistance
          frontier.push((succCoord,tempPath,succDistance),succDistance)
  return []           

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  from searchAgents import manhattanHeuristic
  return manhattanHeuristic(state,problem)
  #return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  from game import Directions   
  from util import PriorityQueue
  n=Directions.NORTH
  s=Directions.SOUTH
  e=Directions.EAST
  w=Directions.WEST
  explored=[]
  frontier=PriorityQueue()
  frontierSet={}
  dist=0 # dist = g(n)
  start_node=problem.getStartState()
  if problem.isGoalState(start_node)==True:
    return []
  frontier.push((start_node,[],dist),dist)
  while frontier.isEmpty()==False:
      visit_node=frontier.pop()
      parentCoord=visit_node[0] # The node to be explored
      parentAction=visit_node[1] # Action required to reach to this node.
      parentDistance=visit_node[2] # Distance to this node 
      if(parentCoord in explored):
          continue
      if(problem.isGoalState(parentCoord)==True):
          print parentAction
          return parentAction
      explored.append(str(parentCoord))
      successors=problem.getSuccessors(parentCoord)
      for successor in successors:
          succCoord=successor[0]
          succAction=successor[1]
          gDistance=parentDistance+1
          heuristicdistance=heuristic(succCoord,problem)
          totaldistance=gDistance+heuristicdistance
          tempPath=list(parentAction)
          if(succAction=='North'):
            tempPath.append(n)
          elif(succAction=='East'):
            tempPath.append(e)
          elif(succAction=='South'):
            tempPath.append(s)
          elif(succAction=='West'):
            tempPath.append(w)    
          if str(succCoord) in explored:
              continue
          dictkey = str(succCoord)
          #print dictkey

          # dictkey=','.join([succCoord[0],succCoord[1]])                
          if dictkey in frontierSet:
              oldDistance = frontierSet[dictkey]
              if totaldistance > oldDistance:
                  totaldistance=oldDistance
          frontierSet[dictkey]=totaldistance
          frontier.push((succCoord,tempPath,totaldistance),totaldistance)
  return []
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch