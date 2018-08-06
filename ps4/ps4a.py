# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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

    permutations = []

    #init
    slice1 = sequence[0:2]
    slice2 = slice1[-1]+slice1[0]
    print(slice1, slice2)


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
    #print(li)




partway_permuation('abc','d')

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)
    #get_permutations('abc')
    pass #delete this line and replace with your code here
