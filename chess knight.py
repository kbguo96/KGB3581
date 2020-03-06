def solution(src, dest):
    #solution strategy relies on defining an adjacency matrix that represents
    #a discrete markov chain
    #takes 2 integers between 0 and 63 inclusive, representing the starting and
    #end states
    #returns a non-negative integer, representing the minimum number of steps needed
    #to move between the two states
    if isinstance(src,int) == False:
        print("src should be an integer between 0 and 63 inclusive")
        return
    elif src < 0 or src>63:
        print("src should be an integer between 0 and 63 inclusive")
        return
    if isinstance(dest,int) == False:
        print("dest should be an integer between 0 and 63 inclusive")
        return
    elif dest < 0 or dest>63:
        print("dest should be an integer between 0 and 63 inclusive")
        return
    #if the chess piece is already at the end
    if src == dest:
        return 0
    #initializing an adjacency matrix object as a list of lists full of zeros
    adj_matrix = zeros_matrix(64,64)

    #initializing the possible moves by the knight as a list of tuples
    #first entry represents changes to the row number (verticle movement)
    #second entry represents changes to the column number (horizantal movement)
    moves = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]

    #building the adjacency matrix
    for i in range(64):
        #finding the coordinates on the chessboard
        i_i, i_j = convert_to_chess(i)
        for m in moves:
            #for each move, check to see the new coordinates after the move
            j_i = i_i +m[0]
            j_j = i_j +m[1]
            #only storing value moves as edges/entries in the adjacency matrix
            if (j_i in range(8)) & (j_j in range(8)):
                j_coord = int(j_i*8 + j_j)
                adj_matrix[i][j_coord] = 1
    #creating a copy of the adjacency matrix for seperate manipulation
    state_matrix = copy_matrix(adj_matrix)
    #creating a counter for how many steps taken
    steps_taken = 1
    while state_matrix [src][dest] == 0:
        steps_taken += 1
        state_matrix = my_matrix_multiplier(copy_matrix(state_matrix),adj_matrix)
    return steps_taken

def copy_matrix(M):
    # returns a copy of a matriz for seperate manipulation
    # taks a matrix M implemented as a list of lists
    # returns a seperate but identical list of lists

    if isinstance(M,list) == False:
        print("Make sure M is a list of lists")
        return
    if all(isinstance(x, list) for x in M) == False:
        print("Make sure M is a list of lists")
        return
    #Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    #Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)

    #Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def my_matrix_multiplier(A,B):
    #computes the product of two matricies in the order AB
    #Takes two matricies both implemented as lists of lists
    #Returns P, the product of the two matricies as a list of lists
    if isinstance(A,list) == False:
        print("Make sure A is a list of lists")
        return
    if all(isinstance(x, list) for x in A) == False:
        print("Make sure A is a list of lists")
        return
    if isinstance(B,list) == False:
        print("Make sure B is a list of lists")
        return
    if all(isinstance(B, list) for x in B) == False:
        print("Make sure B is a list of lists")
        return
    if len(A[0]) != len(B):
        print("The inner dimensions of A and B do not match")
        return
    #Intializing P as a zeros matrix
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    P = zeros_matrix(rowsA, colsB)

    for i in range(len(A[0])):
        for j in range(len(B[0])):
            total = 0
            for ii in range(len(A)):
                total += A[i][ii] * B[ii][j]
            P[i][j] = total
    return P

def zeros_matrix(rows, cols):
    # creates a matrix of zeros of specified dimentions
    # taks two positive integers
    # returns a matrix of zeros implemented as a list of lists
    if isinstance(rows,int) == False:
        print("rows should be a positive integer")
        return
    elif rows <1:
        print("rows should be a positive integer")
        return
    if isinstance(cols,int) == False:
        print("cols should be a positive integer")
        return
    elif cols <1:
        print("cols should be a positive integer")
        return
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M

def convert_to_chess(a_int):
    #a helper function that takes an integer from 0 to 63 and returns
    #the corresponding i,j index of that number on the 8x8 array described in the problem
    #i and j both range from 0 to 7
    if isinstance(a_int,int) == False:
        print("a_int should be an integer between 0 and 63 inclusive")
        return
    elif a_int < 0 or a_int>63:
        print("a_int should be an integer between 0 and 63 inclusive")
        return
    #computing the row number
    my_i = (a_int)//8
    #computing the column number
    my_j = (a_int)%8
    return my_i, my_j
