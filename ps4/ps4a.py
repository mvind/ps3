# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import math

def get_permutations(sequence):
    if len(sequence) == 1:
        return list(sequence)

    perms = []

    for e in get_permutations(sequence[:-1]):
        for i in range(len(e)+1):
            perms.append(e[:i] + sequence[-1] + e[i:])

    return perms


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
    print(permutations)


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
    #partway_permuation('abd','c')
    print(get_permutations('abcd'))
