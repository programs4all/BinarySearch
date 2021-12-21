# needs work

def binarySearch(array, search_term):
    print(len(array))
    top = len(array)-1
    bot = 0
    operations = 0
    while top >= bot:
        mid = round((top+bot)/2)
        operations += 1

        if array[mid] < search_term:
            bot = mid + 1
        elif array[mid] > search_term:
            top = mid - 1
        else:
            return mid, operations
        print(operations, ", mid = ", mid)
    return None, operations


li = [1,2,3,4,5,6,7,8,9,10,11,12,14,17,18]
term = int(input("what term are you looking for "))
index, ops = binarySearch(li, term)


if index:
    print(f'{li[index]} is at index {index} and the program looked at {ops} different indexes')
else:
    print(f"Search term not found after looking at {ops} indexes")