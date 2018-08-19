"""
Missionaries and Cannibals crossing the river:
- Develop working state
- Implement search through nodes with Breadth First Search (BFS) and possibly Depth First Search (DFS) and Iterative Deepening Search (IDS)
    Establish adjacency list to collect neighboring states
    Establish solved list to collect previous states while searching 
- Implement custom print of the solution
- Create main sequence to call all functions in correct order
"""

class RiverPuzzle():
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None

    #check for final goal to be met
    def is_goal(self):
        if self.cannibalLeft == 0 and self.missionaryLeft == 0:
            return True
        else:
            return False

    #check if move is valid or fail if cannibals overpower the missionaries
    def is_valid(self):
        #valid state is when all variables are greater than zero and missionaries outnumber cannibals on the left or right banks
        if self.missionaryLeft >= 0 and self.missionaryRight >= 0 and self.cannibalLeft >= 0 and self.cannibalRight >= 0 and \
           (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) and \
           (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
            return True
        else:
            return False

    #custom equal function to test if current values are equal to another node
    def __eq__(self, other):
        return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft and \
               self.boat == other.boat and self.cannibalRight == other.cannibalRight and self.missionaryRight == other.missionaryRight

    #hash the variables
    def __hash__(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

#get successor states for the given state, successors create nodes for each step of the sequence
def successors(cur_state):
    #create empty dictionary to hold children nodes
    children = [];
    #check state to find the positions of the missionaries, cannibals, and the boat (left bank is starting point, right bank is goal)
    if cur_state.boat == 'left':
        new_state = RiverPuzzle(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right', cur_state.cannibalRight, cur_state.missionaryRight + 2)
        ## Two missionaries cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right', cur_state.cannibalRight + 2, cur_state.missionaryRight)
        ## Two cannibals cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right', cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
        ## One missionary and one cannibal cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right', cur_state.cannibalRight, cur_state.missionaryRight + 1)
        ## One missionary crosses left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right', cur_state.cannibalRight + 1, cur_state.missionaryRight)
        ## One cannibal crosses left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    else:
        new_state = RiverPuzzle(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left', cur_state.cannibalRight, cur_state.missionaryRight - 2)
        ## Two missionaries cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left', cur_state.cannibalRight - 2, cur_state.missionaryRight)
        ## Two cannibals cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left', cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
        ## One missionary and one cannibal cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left', cur_state.cannibalRight, cur_state.missionaryRight - 1)
        ## One missionary crosses right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = RiverPuzzle(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left', cur_state.cannibalRight - 1, cur_state.missionaryRight)
        ## One cannibal crosses right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    return children

#Implementation of the BFS     
def breadth_first_search(canleft, misleft, boat, canright, misright):
    #create variable 'initial_state' with sequence in beginning state 
    start_state = RiverPuzzle(canleft, misleft, boat, canright, misright)
    #check if the initial state is at the goal state and return the goal
    if start_state.is_goal():
        return start_state
    #Collect list of next layer of nodes to test
    frontier = list()
    #Create list of explored nodes
    explored = set()
    #Add new nodes to the frontier list starting with the initial state
    frontier.append(start_state)
    """while processing the frontier list, intialize variable 'state' and pop the last value to check against goal. \
    If it does not match the goal add it to the explored list. Create additional nodes by checking against successors states.
    If the value has been checked already skip it, otherwise add it as a new node to the frontier list."""
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None

#Create report of the solution showing the validated path
def print_solution(solution):
    #Establish empty directory to collect valid nodes
    validpath = []
    #Add entries from the solution
    validpath.append(solution)
    #Initialize parent variable to move valid node to previous state
    parent = solution.parent
    while parent:
        validpath.append(parent)
        parent = parent.parent

    #run through path dictionary and print each value with custom formatting
    for node in range(len(validpath)):
        state = validpath[len(validpath) - node - 1]
        print ("Move #{}".format(node), str(state.cannibalLeft) + "," + str(state.missionaryLeft) + "," + state.boat + "," + str(state.cannibalRight) + "," + str(state.missionaryRight))

def main():
    #starting problem set with 3 missionaries, 3 cannibals, and the boat on the left bank, nothing on the right bank
    goaltest = breadth_first_search(0, 0, 'right', 3, 3)
    print("Test started with final goal, nothing to do, print solution")
    print_solution(goaltest)
    print()

    problem331 = breadth_first_search(3, 3, 'left', 0, 0)
    print("Missionaries and Cannibals solution:")
    print_solution(problem331)

main()