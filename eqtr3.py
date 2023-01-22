import numpy as np
import math

def eqtr3(node, elem):
    """
    Assembles the equilibrium matrix of any 3d truss 

    Inputs:
        Node - Has shape [num_nodes x 6]
            Stores x,y,z coordinates of each node in the first half of the
            output vector. Stores the x,y,z constraints in the second half. A
            constraint value of 0 corresponds to a free direction and a
            constraint value of 1 corresponds to a constrained direction

        Elem - Has shape [num_elements x 2]
            Stores the element node number in columns 1 and 2

    Adapted from code created by S.Pellegrino in May 1988 (mod Feb 1990).
    Provided by M. Sakovsky in Apr 2022. Modified by S. Akinwande in Apr 2022
    """

    #Extract number of nodes, input dimensions, and number of constraints
    numNodes, varSize,numElems = node.shape[0],node.shape[1],elem.shape[0]

    #elem -= 1 #To fix indexing errors between MATLAB and python

    #Ensure input node matrix has correct dimensions
    if varSize != 6:
        raise ValueError("Node Matrix of Incorrect Size")

    #Compute degrees of freedom
    unconFlag = np.where(node[:,3:] == 0, 1,0)
    nDof = np.sum(unconFlag)

    #Form a matrix to help form equilibrium matrix
    count = 0
    rowNo = np.zeros(node[:,3:].shape)
    for i in range(rowNo.shape[0]):
        for j in range(rowNo.shape[1]):
            if node[i,3+j] == 0:
                count +=1
                rowNo[i,j] = count

    

    #Verify the nDof matches the DOF obtained from loop
    if count != nDof:
        raise ValueError("Error in computation of degrees of freedom")
        

    eqMat = np.zeros((nDof, numElems))
    count = 0
    for elemInd in range(numElems):
        count += 1

        nLoc = node[elem[elemInd,0]-1,0:3].tolist() + node[elem[elemInd,1]-1,0:3].tolist()

        #Bar Length
        barLen = np.sqrt((nLoc[0] - nLoc[3])**2 + (nLoc[1] - nLoc[4]) ** 2 + (nLoc[2] - nLoc[5])**2) 

        #Equilibrium Contributions
        x = (nLoc[0] - nLoc[3])/barLen
        y = (nLoc[1] - nLoc[4])/barLen
        z = (nLoc[2] - nLoc[5])/barLen

        equilOne = [x, y, z, -x, -y, -z]

        coun2 = 0
        for i in range(2): #Iterate over each node connected to bar
            for j in range(3): #Iterate over each DOF at node
                coun2 += 1

                rowCheck = rowNo[elem[elemInd,i]-1,j]
                if rowCheck > 0:
                    eqMat[int(rowCheck)-1,count-1] = equilOne[coun2-1]

    return eqMat



# =============================================================================
#     
#     print('Example 1: Lecture 4, slide 14')
#     testNode = np.array([[0, 1, 0, 1, 1, 1],[0, 0, 0, 1, 1, 1],
#                          [1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1],
#                          [2, 1, 0, 0, 0, 1], [2, 0, 0, 0, 0, 1]])
# 
#     testElem = np.array([[1,3],[2,4],[2,3],[3,4],[3,5],[4,6],[4,5],[5,6]])
# 
#     A = eqtr3(testNode, testElem)
#     
#     r = np.linalg.matrix_rank(A)
#     print('Equilibrium matrix rank is = ', r)
#     
#     # number of mechanisms and state of self stress
#     s = 8 - r
#     m = (3*6 - 10) - r # note that k = 10 as the structure is constrained from moving out of plane
#     
#     print('Number of mechanisms = ', m)
#     print('Number of states of self-stress = ', s)
#     
#     print('Example 2: Lecture 4, slide 15')
#     testNode = np.array([[0, 1, 0, 1, 1, 1],[0, 0, 0, 1, 1, 1],
#                         [1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1],
#                         [2, 1, 0, 0, 0, 1], [2, 0, 0, 0, 0, 1]])
# 
#     testElem = np.array([[1,3],[2,4],[3,4],[3,5],[4,6],[3,6],[4,5],[5,6]])
# 
#     A = eqtr3(testNode, testElem)
# 
#     r = np.linalg.matrix_rank(A)
#     print('Equilibrium matrix rank is = ', r)
#     
#     # number of mechanisms and state of self stress
#     s = 8 - r
#     m = (3*6 - 10) - r
#     
#     print('Number of mechanisms = ', m)
#     print('Number of states of self-stress = ', s)
# =============================================================================
    
def problem1():
    # first structure
    first_node = np.array([[-1,-1,0,0,0,0],[-1,1,0,0,0,0],[1,1,0,0,0,0],
                           [1,-1,0,0,0,0],[-1,-1,2,1,1,1],[-1,1,2,1,1,1],
                           [1,1,2,1,1,1],[1,-1,2,1,1,1]])
    first_elem = np.array([[1,2],[1,4],[1,5],[1,6],[2,3],[2,6],[2,7],[3,4],
                           [3,7],[3,8],[4,5],[4,8],[5,6],[5,8],[6,7],[7,8]])
    
    A = eqtr3(first_node, first_elem)
    r = np.linalg.matrix_rank(A)
    print('Equilibrium matrix rank is = ', r)  
   
    # number of mechanisms and state of self stress
    s = 12 - r
    m = (3*8 - 12) - r 
    
    print('1st Structure: Number of mechanisms = ', m)
    print('1st Structure: Number of states of self-stress = ', s)
    
    
    # second structure
    first_node = np.array([[1,-1,0,0,0,0],[-1,-1,0,0,0,0],[-1,1,0,0,0,0],
                           [1,1,0,0,0,0],[0,-math.sqrt(2),1,1,1,1],
                           [-math.sqrt(2),0,1,1,1,1],
                           [0,math.sqrt(2),1,1,1,1],
                           [math.sqrt(2),0,1,1,1,1]])
    first_elem = np.array([[1,2],[1,4],[1,5],[1,6],[2,3],[2,6],[2,7],[3,4],
                           [3,7],[3,8],[4,5],[4,8],[5,6],[5,8],[6,7],[7,8]])
    
    A = eqtr3(first_node, first_elem)
    r = np.linalg.matrix_rank(A)
    print('Equilibrium matrix rank is = ', r)  
   
    # number of mechanisms and state of self stress
    s = 12 - r
    m = (3*8 - 12) - r 
    
    print('2nd Structure: Number of mechanisms = ', m)
    print('2nd Structure: Number of states of self-stress = ', s)


def problem2b():
    # JWST deployed (pin joint)
    # approx distance between node 3 and 4 = 1.5 m
    first_node = np.array([[0,0,0,1,1,1],[0,3.25,6,0,0,0],[1.5,6.5,0,1,1,1],
                           [-1.5,6.5,0,1,1,1],[0,1.625,3,0,0,0]])
    first_elem = np.array([[1,5],[2,5],[2,3],[2,4]])
    
    A = eqtr3(first_node, first_elem)
    r = np.linalg.matrix_rank(A)
    print('Equilibrium matrix rank is = ', r)  
   
    # number of mechanisms and state of self stress
    s = 4 - r # 4 bars
    m = (3*5 - 9) - r # 5 joints, 9 kinematic constraints
    
    print('JWST_pin: Number of mechanisms = ', m)
    print('JWST_pin: Number of states of self-stress = ', s)
    
    
    # JWST deployed (locked joint)
    # approx distance between node 3 and 4 = 1.5 m
    first_node = np.array([[0,0,0,1,1,1],[0,3.25,6,0,0,0],[1.5,6.5,0,1,1,1],
                           [-1.5,6.5,0,1,1,1]])
    first_elem = np.array([[1,2],[2,3],[2,4]])
    
    A = eqtr3(first_node, first_elem)
    r = np.linalg.matrix_rank(A)
    print('Equilibrium matrix rank is = ', r)  
   
    # number of mechanisms and state of self stress
    s = 3 - r # 3 bars
    m = (3*4 - 9) - r # 4 joints, 9 kinematic constraints
    
    print('JWST_locked: Number of mechanisms = ', m)
    print('JWST_locked: Number of states of self-stress = ', s)

    
if __name__ == "__main__":
    problem1()