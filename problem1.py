# this if only runs when the file is run using `python problem1.py` from the commandline
if __name__ == '__main__':
    # with blocks handle opening and closing things
    # instead of doing something like:
    #   f = open('problem1_input.txt')
    #   inp = f.read().strip()
    #   f.close()
    with open('problem1_input.txt') as f:
        inp = f.read().strip()
    # just store the 2 sums in a list
    parts = [0, 0]

    # save a few characters by getting the length and the offset
    l = len(inp)
    o = l/2

    # iterate from i = 0 to l-1
    for i in range(l):
        # for part 1 just check if the next element is equal
        # the `%` is to circle back around
        # for part 1 it only helps for when i == l-1
        # in that case without the `%` it would be inp[l] which would be an index error
        if inp[i] == inp[int((i + 1) % l)]:
            parts[0] += int(inp[i])
        # same as part 1 except with the offset
        # the `%` helps avoid index errors for all i >= l/2
        # `if` instead of `elif` because we want both of these `if` blocks to run every time
        # `elif` here wouldn't run if the part 1 `if` were true
        if inp[i] == inp[int((i + o) % l)]:
            parts[1] += int(inp[i])

    # pretty print the answer
    # %s just acts as a placeholder for the arguments included after the %
    print("Part 1: %s" % parts[0])
    print("Part 2: %s" % parts[1])
