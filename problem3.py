GOAL = 289326

def get_adj_sum(d, cur):
    # Sums all of the possible neighbors
    # there's a cleaner way to do this
    # a cleaner way to do this is:
    # return sum(d.get((cur[0] + i, cur[1] + j), 0) for i in range(-1, 2) for j in range(-1, 2))
    return (
        d.get((cur[0] - 1, cur[1]), 0) +
        d.get((cur[0] + 1, cur[1]), 0) +
        d.get((cur[0], cur[1] - 1), 0) +
        d.get((cur[0], cur[1] + 1), 0) +
        d.get((cur[0] - 1, cur[1] - 1), 0) +
        d.get((cur[0] - 1, cur[1] + 1), 0) +
        d.get((cur[0] + 1, cur[1] - 1), 0) +
        d.get((cur[0] + 1, cur[1] + 1), 0)
    )

if __name__ == "__main__":
    # PART 1
    # initialize the spiral
    spiral_set = {(0, 0), (1, 0)}
    # set the current mark
    cur = (1, 0)
    # once there are `GOAL` # of elements in the set then we break because we made it
    while len(spiral_set) < GOAL:
        # if there's something to the left and nothing above then go up
        if (cur[0] - 1, cur[1]) in spiral_set and (cur[0], cur[1] + 1) not in spiral_set:
            cur = (cur[0], cur[1] + 1)
        # if there's something below and nothing to the left then go left 
        elif (cur[0], cur[1] - 1) in spiral_set and (cur[0] - 1, cur[1]) not in spiral_set:
            cur = (cur[0] - 1, cur[1])
        # if there's something to the right and nothing below then go down
        elif (cur[0] + 1, cur[1]) in spiral_set and (cur[0], cur[1] - 1) not in spiral_set:
            cur = (cur[0], cur[1] - 1)
        # if none of those are the case then go right
        else:
            cur = (cur[0] + 1, cur[1])
        # add the new `cur` to the set and move on
        spiral_set.add(cur)
    print(abs(cur[0]) + abs(cur[1]))

    # instead of just a set we have to keep track of the numbers in each part of the spiral
    spiral_dict = {(0, 0): 1, (1, 0): 1}
    cur = (1, 0)
    # instead of size of the spiral we use the current value in the spiral
    while spiral_dict[cur] <= GOAL:
        # follow the same rules as part 1
        if (cur[0] - 1, cur[1]) in spiral_dict and (cur[0], cur[1] + 1) not in spiral_dict:
            cur = (cur[0], cur[1] + 1)
        elif (cur[0] - 1, cur[1]) not in spiral_dict and (cur[0], cur[1] - 1) in spiral_dict:
            cur = (cur[0] - 1, cur[1])
        elif (cur[0] + 1, cur[1]) in spiral_dict and (cur[0], cur[1] - 1) not in spiral_dict:
            cur = (cur[0], cur[1] - 1)
        else:
            cur = (cur[0] + 1, cur[1])
        # get the sum of all adjacent spots and assign it
        spiral_dict[cur] = get_adj_sum(spiral_dict, cur)
    print(spiral_dict[cur])
