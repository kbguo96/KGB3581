def solution(data, n):
    # data is a list of 0-99 integers
    # n is an integer
    # returns a list of integers which show up in data less than
    # or equal to n times
    if isinstance(n, int) == False:
        print("n is not an integer")
        return
    elif n < 0:
        print("n is negative, please use non-negative integer")
        return
    elif isinstance(data, list) == False:
        print("data is not a list")
        return
    elif all(isinstance(item, int) for item in data) == False:
        print("make sure data only contains integers")
        return
    else:
        unique_int = set(data)
        for u_int in unique_int:
            print(u_int)
            if data.count(u_int) > n:
                print(data)
                data = [elem for elem in data if elem != u_int]
                print(data)

    return data