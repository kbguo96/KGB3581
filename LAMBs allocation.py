import math

def solution(total_lambs):
    # Your code here
    # computes the positive integer Hmax such that Hmax henchmen are each paid the maximum
    # amount allowed under the specified rules
    # computes the positive integer Hmin such that Hmin henchmen are each paid the minimum
    # amount allowed under the specified rules
    # returns the quantity Hmin-Hmax, which should be a non-negative integer
    if isinstance(total_lambs, int) == False:
        print("total_lambs must be a positive integer integer")
        return
    elif total_lambs <=0:
        print("total_lambs must be a positive integer integer")
        return
    Hmax = math.floor(math.log(total_lambs+1,2))
    #Hmax is the length of the longest sequence of terms that double, who sum to less
    #than total_lambs
    #Since the sum of terms of such a series has a closed form expression,
    #the value of Hmax can be computed analytically so to speak

    if total_lambs == 1:
        Hmin = 1
        #since myfib assumes at least 2 henchmen being paid
        #I list total_lambs == 1 as a special seperate case
    elif total_lambs >= 2:
        Hmin = myfib(total_lambs)
    return int(Hmin-Hmax)

def myfib(a_num):
    #Helper fuction which computes length of the longest sequence of fibonachi numbers
    #that sum to less than a positive integer a_num
    #returns a positive integer counter
    p1 = 1 #the previous term in the sequence, initiallize at 1
    p2 = 1 #the term immediately preceeding the p1, initialized at 1
    mysum = 2 #the sum of the sequence at the current iteration, initialized as 2
    counter = 1 #sequence length counter for output, assumes total_lambs >= 2
    while mysum <= a_num:
        p0 = p1+p2 #the "current" term in the sequence
        #updating all the values
        mysum += p0
        p2 = p1
        p1 = p0
        counter +=1
    return counter

print(solution(1))
