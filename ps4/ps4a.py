# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import math

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return list(sequence)

#   abc
#   ab ba
#   cab acb abc cba bca bac
#
    #permutations = [[sequence[0]]]
    buffer_list = [[sequence[0]]]
    permutation_list = []

    for p in range(1,len(sequence)):
        #print(buffer_list[0])
        #pointer = depth(buffer_list)
        #print('Pointer: ', pointer)
        for i in range(len(buffer_list[0])):
            if i > 1:
                for g in range(len(buffer_list[0])-1):
                    permutation_list.append(partway_permuation(''.join(buffer_list[g][i]), sequence[p]))

                #print(buffer_list[pointer][i])
                #pointer += 1
            permutation_list.append(partway_permuation(''.join(buffer_list[0][i]), sequence[p]))
        print(permutation_list)
        buffer_list = permutation_list
        permutation_list = []


    #Just clean of up the return data.
    for i in range(len(buffer_list[0])-1):
        for j in range(len(buffer_list[i])):
            #print(buffer_list[i][j])
            permutation_list.append(buffer_list[i][j])

    print('Length: ', str(len(permutation_list)), 'Len: ', str(math.factorial(len(sequence))))


def partway_permuation(slice,c):
    "Returns all permuations by inserting c into slice"
    permutations = []
    li = list(slice)

    #First case
    permutations.append([c]+li)

    #Rest of cases
    for i in range(1,len(slice)+1):
        #print(li[0:i]+[c]+li[i:])
        permutations.append(li[0:i]+[c]+li[i:])
    #print(permutations)
    return permutations


def depth(li):
    "Returns the amount of nested lists in a list"
    count = 0
    depthlist = []
    for char in str(li):

        if  char == "[":
            count += 1
            depthlist.append(count)

        elif char == "]":
            count -= 1
            depthlist.append(count)

    return(max(depthlist))

if __name__ == '__main__':
    print(depth([['hej']]))
    get_permutations('abcd')
    pass #delete this line and replace with your code here
