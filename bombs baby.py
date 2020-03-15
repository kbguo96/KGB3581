def solution(x, y):
    # takes 2 non-negative integers as strings
    # indcating required number of bombs of each type
    # returns the minimum number of generations required to produce
    # required bomb count as a string
    # returns the string "impossible" if required number of bombs
    # cannot be achieved

    # store integer typed objects of inputs for ease of use
    mach = int(x)
    facula = int(y)

    # account for possibiltiy of inputs of 0
    if mach == 0:
        return "impossible"
    if facula == 0:
        return "impossible"

    # the only time where mach == facula is allows is the base case of 1,1
    if mach == facula:
        if mach == 1:
            return "0"
        else:
            return "impossible"
    # otherwise if mach > facula
    elif mach > facula:
        # in case facula is just 1, special case to expidite runtime
        if facula == 1:
            return str(mach - 1)
        # otherwise
        mach2 = mach - (mach % facula)  # getting rid of any remander

        # this is the number of times facula must be subtracted from Mach before
        # either a base case or facula > than the new mach
        increment = (mach2 / facula)

        # evaluate the solution to the reduced problem
        situation = solution(str(int(mach - facula * increment)), str(facula))
        # if solution does not exist
        if situation == "impossible":
            return situation
        # otherwise add the number of times previously calculated to the running total
        else:
            return str(int(situation) + increment)
    # ditto/reverse situation from where mach > facula
    else:
        if mach == 1:
            return str(facula - 1)
        facula2 = facula - (facula % mach)
        increment = facula2 / mach
        situation = solution(str(mach), str(int(facula - mach * increment)))
        if situation == "impossible":
            return situation
        else:
            return str(int(situation) + increment)
    return "fail"
