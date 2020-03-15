def solution(l):
    # l is a list of positive integers
    # returns a non negative integer

    # initialize an adjacency matrix
    multiple_storage = zeros_matrix(len(l), len(l))

    set_l = set(l)
    sorted_l = list(set_l).sort()

    # build out state transition rules in adjacency matrix
    # a valid triple is a successive transition between 3 states
    # represents a directed graph
    for i in xrange(len(l) - 1):
        for j in xrange(len(l)):
            if j > i:
                if (l[j] % l[i]) == 0:
                    # edge exists from A to B if B is a multiple of A
                    multiple_storage[i][j] = 1
    # intermediate sum values for how many valid triples remain
    # conditional on the second element of the triple being fixed
    semi = [sum(x) for x in multiple_storage]
    running_tot = 0
    for row in multiple_storage:
        # final sum for each possible initial transition
        running_tot += sum([A * B for A, B in zip(semi, row)])
    return int(running_tot)


def zeros_matrix(rows, cols):
    # creates a matrix of zeros of specified dimentions

    # taks two positive integers

    # returns a matrix of zeros implemented as a list of lists

    if isinstance(rows, int) == False:

        print("rows should be a positive integer")

        return

    elif rows < 1:

        print("rows should be a positive integer")

        return

    if isinstance(cols, int) == False:

        print("cols should be a positive integer")

        return

    elif cols < 1:

        print("cols should be a positive integer")

        return

    M = []

    while len(M) < rows:

        M.append([])

        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M
