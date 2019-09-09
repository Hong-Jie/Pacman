# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def revDir(direction):
    if direction==Directions.NORTH:
        return Directions.SOUTH
    elif direction==Directions.EAST:
        return Directions.WEST
    elif direction==Directions.WEST:
        return Directions.EAST
    elif direction==Directions.SOUTH:
        return Directions.NORTH
    else:
        return None

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    "*** YOUR CODE HERE ***"
    from util import Stack
    start = problem.getStartState();
    fringe = Stack()
    fringe.push((start,None,0));
    visited = set()     # set of viseted dots
    ACT = []            # list of actions
    RACT = []           # list of reverse actions
    branchStep = []     # list of (num of branches, how many steps from branch parent)
    
    while not fringe.isEmpty():
        """ Dot = (position, action, cost) """
        Dot = fringe.pop()
        visited.add(Dot[0])
        ACT.append(Dot[1])
        RACT.append(revDir(Dot[1]))
        if problem.isGoalState(Dot[0]):
            ACT.pop(0)
            return ACT
        else:
            numBranches = 0
            for successor in problem.getSuccessors(Dot[0]):
                if successor[0] not in visited:
                    fringe.push(successor)
                    numBranches+=1
            if numBranches>1:
                """ More than one path, record branches """
                branchStep.append([numBranches, 1])
            elif numBranches==1 and branchStep[-1]:
                """ Only one path to forward, add steps to the current branch """
                branchStep[-1][1]+=1
            elif numBranches==0:
                """ No path forward, follow reversed action to go back to branch """
                if not branchStep[-1]:
                    print("No solution!")
                    return ACT
                """ 
                If all branches are traversed, pop out the branch record
                and reverse steps to the branch parent 
                """
                reverseSteps=0
                while branchStep[-1][0]==1:
                    reverseSteps += branchStep[-1][1]
                    branchStep.pop()
                
                reverseSteps += branchStep[-1][1]
                branchStep[-1][0]-=1        # Decrease number of branches
                branchStep[-1][1]=1         # Initialize steps from branch parent to 1
                for x in range(reverseSteps):
                    ACT.append(RACT.pop())
    
    print("No solution!")
    return ACT

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue 
    start = problem.getStartState();
    fringe = Queue()
    fringe.push((start,None,0));
    visited = set()     # set of viseted dots
    ACT = []            # list of actions
    RACT = []           # list of reverse actions
    branchStep = []     # list of (num of branches, how many steps from branch parent)
    
    while not fringe.isEmpty():
        """ Dot = (position, action, cost) """
        Dot = fringe.pop()
        visited.add(Dot[0])
        ACT.append(Dot[1])
        RACT.append(revDir(Dot[1]))
        if problem.isGoalState(Dot[0]):
            ACT.pop(0)
            return ACT
        else:
            numBranches = 0
            for successor in problem.getSuccessors(Dot[0]):
                if successor[0] not in visited:
                    fringe.push(successor)
                    numBranches+=1
            if numBranches>1:
                """ More than one path, record branches """
                branchStep.append([numBranches, 1])
            elif numBranches==1 and branchStep[-1]:
                """ Only one path to forward, add steps to the current branch """
                branchStep[-1][1]+=1
            elif numBranches==0:
                """ No path forward, follow reversed action to go back to branch """
                if not branchStep[-1]:
                    print("No solution!")
                    return ACT
                """ 
                If all branches are traversed, pop out the branch record
                and reverse steps to the branch parent 
                """
                reverseSteps=0
                while branchStep[-1][0]==1:
                    reverseSteps += branchStep[-1][1]
                    branchStep.pop()
                
                reverseSteps += branchStep[-1][1]
                branchStep[-1][0]-=1        # Decrease number of branches
                branchStep[-1][1]=1         # Initialize steps from branch parent to 1
                for x in range(reverseSteps):
                    ACT.append(RACT.pop())
    
    print("No solution!")

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
